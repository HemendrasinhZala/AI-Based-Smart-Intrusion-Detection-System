"""
==========================================================
AI Intrusion Detection System
System Status Panel
==========================================================
"""

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout
)

from PySide6.QtCore import Qt

from ui.styles import *

from ui.widgets.threat_score_card import ThreatScoreCard
from ui.widgets.large_status_card import LargeStatusCard
from ui.widgets.small_status_card import SmallStatusCard


class SystemStatus(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("SystemStatus")

        self.setMinimumWidth(500)
        self.setMaximumWidth(540)

        self.setStyleSheet(f"""
        QFrame#SystemStatus {{
            background:{PANEL};
            border:1px solid {BORDER};
            border-radius:12px;
        }}
        QLabel {{
            border:none;
            color:white;
        }}
        """)

        self.build_ui()

    # ==================================================

    def build_ui(self):

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(18, 18, 18, 18)
        main_layout.setSpacing(16)

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        title = QLabel("SYSTEM STATUS")

        title.setStyleSheet("""
            font-size:17px;
            font-weight:700;
            color:white;
        """)

        main_layout.addWidget(title)

        # =================================================
        # Top Row
        # =================================================

        top_layout = QHBoxLayout()
        top_layout.setSpacing(12)

        # Threat Gauge

        self.gauge = ThreatScoreCard()

        # Threat Level

        self.threat = LargeStatusCard(
            title="THREAT LEVEL",
            icon_name="fa6s.shield-halved",
            value="HIGH",
            subtitle="Take Action",
            icon_color="#FF453A",
            value_color="#FF453A"
        )

        # Human Count

        self.human = LargeStatusCard(
            title="HUMAN COUNT",
            icon_name="fa6s.user",
            value="2",
            subtitle="Detected",
            icon_color="#3B82F6",
            value_color="#FFFFFF"
        )
        top_layout.addWidget(self.gauge)
        top_layout.addWidget(self.threat)
        top_layout.addWidget(self.human)

        main_layout.addLayout(top_layout)

        # =================================================
        # Bottom Row
        # =================================================

        bottom = QGridLayout()

        bottom.setHorizontalSpacing(10)
        bottom.setVerticalSpacing(10)

        self.motion = SmallStatusCard(
            "MOTION",
            "fa6s.person-running",
            "DETECTED",
            "#22C55E",
            "#22C55E"
        )

        self.pir = SmallStatusCard(
            "PIR SENSOR",
            "fa6s.tower-broadcast",
            "ACTIVE",
            "#22C55E",
            "#22C55E"
        )

        self.door = SmallStatusCard(
            "DOOR STATUS",
            "fa6s.door-open",
            "OPEN",
            "#FF453A",
            "#FF453A"
        )

        self.recording = SmallStatusCard(
            "RECORDING",
            "fa6s.circle-dot",
            "ON",
            "#FF453A",
            "#FF453A"
        )

        bottom.addWidget(self.motion, 0, 0)
        bottom.addWidget(self.pir, 0, 1)
        bottom.addWidget(self.door, 0, 2)
        bottom.addWidget(self.recording, 0, 3)

        main_layout.addLayout(bottom)

        main_layout.addStretch()

    # ==================================================
    # Update Methods
    # ==================================================

    def update_threat_score(self, score):
        self.gauge.setScore(score)

    def update_threat_level(self, level):
        self.threat.setValue(level)

    def update_human_count(self, count):
        self.human.setValue(str(count))

    def update_motion(self, value):
        self.motion.setValue(value)

    def update_pir(self, value):
        self.pir.setValue(value)

    def update_door(self, value):
        self.door.setValue(value)

    def update_recording(self, value):
        self.recording.setValue(value)