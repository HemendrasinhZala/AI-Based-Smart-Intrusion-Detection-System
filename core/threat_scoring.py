"""
===========================================================
AI Intrusion Detection System
Threat Scoring Module

Author : Hemendrasinh Zala

This module calculates the threat score based on
multiple inputs from the AI Intrusion Detection System.

Current Inputs
--------------
1. Motion Detection
2. Human Detection
3. Human Detection Confidence
4. Number of Humans

Future Inputs
-------------
1. PIR Sensor
2. Door Sensor
3. Time of Day
4. Face Recognition
5. Weapon Detection

Threat Levels
-------------
0 - 30   : LOW
31 - 70  : MEDIUM
71 - 100 : HIGH
===========================================================
"""

from core.logger import Logger


class ThreatScoring:
    """
    Calculates the threat score.
    """

    def __init__(self):
        """
        Initialize threat scoring.
        """

        self.logger = Logger()

        self.score = 0

        self.level = "LOW"

        self.logger.info(
            "Threat Scoring Initialized Successfully."
        )

    # =======================================================
    # CALCULATE THREAT SCORE
    # =======================================================

    def calculate_score(
        self,
        motion_detected=False,
        human_detected=False,
        confidence=0.0,
        human_count=0,
    ):
        """
        Calculate the threat score.

        Parameters
        ----------
        motion_detected : bool

        human_detected : bool

        confidence : float

        human_count : int

        Returns
        -------
        int
        """

        score = 0

        # ------------------------------------------
        # Motion Detection
        # ------------------------------------------

        if motion_detected:

            score += 20

        # ------------------------------------------
        # Human Detection
        # ------------------------------------------

        if human_detected:

            score += 50

        # ------------------------------------------
        # Human Detection Confidence
        # ------------------------------------------

        if confidence >= 0.90:

            score += 20

        elif confidence >= 0.80:

            score += 15

        elif confidence >= 0.70:

            score += 10

        # ------------------------------------------
        # Multiple Humans
        # ------------------------------------------

        if human_count >= 2:

            score += 10

        if score > 100:

            score = 100

        self.score = score

        self.level = self.get_level(score)

        self.logger.info(
            f"Threat Score : {score} | Level : {self.level}"
        )

        return score
    
        # =======================================================
    # GET THREAT LEVEL
    # =======================================================

    def get_level(self, score):
        """
        Determine the threat level based on score.

        Parameters
        ----------
        score : int

        Returns
        -------
        str
        """

        if score <= 30:

            return "LOW"

        elif score <= 70:

            return "MEDIUM"

        else:

            return "HIGH"

    # =======================================================
    # GET CURRENT SCORE
    # =======================================================

    def get_score(self):
        """
        Return the current threat score.

        Returns
        -------
        int
        """

        return self.score

    # =======================================================
    # GET CURRENT LEVEL
    # =======================================================

    def get_threat_level(self):
        """
        Return the current threat level.

        Returns
        -------
        str
        """

        return self.level

    # =======================================================
    # HIGH THREAT CHECK
    # =======================================================

    def is_high_threat(self):
        """
        Check whether the current threat level is HIGH.

        Returns
        -------
        bool
        """

        return self.level == "HIGH"

    # =======================================================
    # RESET
    # =======================================================

    def reset(self):
        """
        Reset threat score.
        """

        self.score = 0

        self.level = "LOW"

        self.logger.info(
            "Threat score reset successfully."
        )