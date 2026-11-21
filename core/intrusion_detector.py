"""
===========================================================
AI Intrusion Detection System
Intrusion Detector Module

Author : Hemendrasinh Zala

This module controls the complete intrusion detection
workflow.

Workflow

System Armed
      ↓
Motion Detection
      ↓
Human Detection
      ↓
Threat Scoring
      ↓
Capture Image
      ↓
Record Video
      ↓
Play Alarm (HIGH Threat Only)
      ↓
Save Logs
===========================================================
"""

import time

from config import VIDEO_DURATION

from core.logger import Logger
from core.motion_detector import MotionDetector
from core.human_detector import HumanDetector
from core.recorder import Recorder
from core.sound import Sound
from core.threat_scoring import ThreatScoring
from hardware.led import LED
from hardware.buzzer import Buzzer
from hardware.door_sensor import DoorSensor


class IntrusionDetector:
    """
    Main controller of the AI Intrusion Detection System.
    """

    def __init__(self):
        """
        Initialize all modules.
        """

        self.logger = Logger()

        self.motion_detector = MotionDetector()

        self.human_detector = HumanDetector()

        self.recorder = Recorder()

        self.sound = Sound()

        self.threat_scoring = ThreatScoring()


        # -----------------------------------------
        # Hardware
        # -----------------------------------------

        self.led = LED()
        self.buzzer = Buzzer()
        self.door_sensor = DoorSensor()

        self.previous_door_state = False
        # -------------------------------------------------
        # System State
        # -------------------------------------------------

        self.system_armed = False

        self.intrusion_detected = False

        self.recording_started = False

        self.recording_start_time = None

        self.image_saved = False

        self.threat_score = 0

        self.threat_level = "LOW"

        self.logger.info(
            "Intrusion Detector Initialized Successfully."
        )

    # =====================================================
    # ARM SYSTEM
    # =====================================================

    def arm_system(self):
        """
        Arm the intrusion detection system.
        """

        self.system_armed = True

        self.logger.info("System Armed.")

    # =====================================================
    # DISARM SYSTEM
    # =====================================================

    def disarm_system(self):
        """
        Disarm the intrusion detection system.
        """

        self.system_armed = False

        self.cleanup()

        self.logger.info("System Disarmed.")

    # =====================================================
    # SYSTEM STATUS
    # =====================================================

    def is_system_armed(self):
        """
        Return True if system is armed.
        """

        return self.system_armed

    # =====================================================
    # THREAT SCORE
    # =====================================================

    def get_threat_score(self):
        """
        Return current threat score.
        """

        return self.threat_score

    # =====================================================
    # THREAT LEVEL
    # =====================================================

    def get_threat_level(self):
        """
        Return current threat level.
        """

        return self.threat_level

    # =====================================================
    # PROCESS FRAME
    # =====================================================

    def process_frame(self, frame):
        """
        Process one camera frame.
        """

        # -------------------------------------------------
        # If system is DISARMED, do nothing.
        # -------------------------------------------------

        if not self.system_armed:

            return frame

        # -------------------------------------------------
        # Step 1 : Motion Detection
        # -------------------------------------------------

        motion_detected = self.motion_detector.detect_motion(frame)
        # -----------------------------------------
        # Door Sensor
        # -----------------------------------------

        door_open = self.door_sensor.is_door_open()

        if door_open and not self.previous_door_state:
            print("?? Door Opened!")

        if door_open:
            motion_detected = True

        self.previous_door_state = door_open
        if motion_detected:

            self.motion_detector.draw_motion_boxes(frame)

        # -------------------------------------------------
        # Step 2 : Human Detection
        # -------------------------------------------------

        human_detected = False

        confidence = 0.0

        human_count = 0

        if motion_detected:

            human_detected = self.human_detector.detect_humans(frame)

            if human_detected:

                self.human_detector.draw_boxes(frame)

                human_count = self.human_detector.get_human_count()

                boxes = self.human_detector.get_human_boxes()

                if boxes:

                    confidence = max(
                        box[4] for box in boxes
                    )

            # -------------------------------------------------
        # Step 3 : Calculate Threat Score
        # -------------------------------------------------

        self.threat_score = self.threat_scoring.calculate_score(

            motion_detected=motion_detected,

            human_detected=human_detected,

            confidence=confidence,

            human_count=human_count,

        )

        self.threat_level = (
            self.threat_scoring.get_threat_level()
        )
        # -----------------------------------------
        # LED + Buzzer
        # -----------------------------------------

        if self.threat_level == "LOW":

            self.led.show_low()
            self.buzzer.turn_off()

        elif self.threat_level == "MEDIUM":

            self.led.show_medium()
            self.buzzer.turn_on()

        elif self.threat_level == "HIGH":

            self.led.show_high()
            self.buzzer.turn_on()

        # -------------------------------------------------
        # No Human Detected
        # -------------------------------------------------

        if not human_detected:

            return frame

        # -------------------------------------------------
        # Human Detected
        # -------------------------------------------------

        self.intrusion_detected = True

        # -------------------------------------------------
        # Capture Image (Only Once)
        # -------------------------------------------------

        if not self.image_saved:

            image_path = self.recorder.capture_image(frame)

            self.image_saved = True

        else:

            image_path = self.recorder.image_path

        # -------------------------------------------------
        # Start Video Recording (Only Once)
        # -------------------------------------------------

        if not self.recording_started:

            height, width = frame.shape[:2]

            video_path = self.recorder.start_recording(

                (width, height)

            )

            self.recording_started = True

            self.recording_start_time = time.time()

        else:

            video_path = self.recorder.video_path

        # -------------------------------------------------
        # Continue Recording
        # -------------------------------------------------

        if self.recorder.is_recording():

            self.recorder.update(frame)

        # -------------------------------------------------
        # Play Alarm
        # HIGH Threat Only
        # -------------------------------------------------

        if self.threat_level == "HIGH":

            if not self.sound.is_playing():

                self.sound.play_alarm()

        # -------------------------------------------------
        # Log Intrusion
        # -------------------------------------------------

        self.logger.log_intrusion(

            event=f"Threat Level : {self.threat_level} | Score : {self.threat_score}",

            image_path=image_path,

            video_path=video_path,

        )

        return frame
        # =====================================================
    # UPDATE
    # =====================================================

    def update(self):
        """
        Update the intrusion detector.

        Stops recording and alarm automatically after
        VIDEO_DURATION seconds.
        """

        if not self.recording_started:
            return

        elapsed_time = time.time() - self.recording_start_time

        if elapsed_time >= VIDEO_DURATION:

            # ---------------------------------------------
            # Stop Video Recording
            # ---------------------------------------------

            if self.recorder.is_recording():

                self.recorder.stop_recording()

            # ---------------------------------------------
            # Stop Alarm
            # ---------------------------------------------

            if self.sound.is_playing():

                self.sound.stop_alarm()

            self.logger.info(
                "Intrusion recording completed."
            )

            # ---------------------------------------------
            # Reset Detector
            # ---------------------------------------------

            self.reset()

    # =====================================================
    # RESET
    # =====================================================

    def reset(self):
        """
        Reset the intrusion detector.
        """

        self.intrusion_detected = False

        self.recording_started = False

        self.recording_start_time = None

        self.image_saved = False

        self.threat_score = 0

        self.threat_level = "LOW"

        self.threat_scoring.reset()
        self.buzzer.turn_off()
        self.led.show_low()
        self.logger.info(
            "Intrusion detector reset."
        )

    # =====================================================
    # CLEANUP
    # =====================================================

    def cleanup(self):
        """
        Release all resources before exiting.
        """

        # Stop recording if active
        if self.recorder.is_recording():

            self.recorder.stop_recording()

        # Stop alarm if playing
        if self.sound.is_playing():

            self.sound.stop_alarm()

        # Reset detector state
        self.reset()
        self.led.cleanup()
        self.buzzer.cleanup()
        self.door_sensor.cleanup()

        self.logger.info(
            "Intrusion detector cleaned up successfully."
        )

    # =====================================================
    # INTRUSION STATUS
    # =====================================================

    def is_intrusion_detected(self):
        """
        Return intrusion status.

        Returns
        -------
        bool
        """

        return self.intrusion_detected