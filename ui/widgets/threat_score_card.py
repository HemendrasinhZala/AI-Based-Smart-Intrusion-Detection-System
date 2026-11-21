"""
==========================================================
AI Intrusion Detection System
Threat Score Card
==========================================================
"""

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from ui.styles import *
from ui.widgets.threat_gauge import ThreatGauge


class ThreatScoreCard(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("ThreatScoreCard")

        self.setMinimumSize(185, 205)
        self.setMaximumHeight(205)

        self.setStyleSheet(f"""
        QFrame#ThreatScoreCard {{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:10px;
        }}

        QLabel {{
            border:none;
        }}
        """)

        self.build_ui()

    # --------------------------------------------------

    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)

        # ------------------------------------------
        # Title
        # ------------------------------------------

        title = QLabel("THREAT SCORE")

        title.setAlignment(Qt.AlignCenter)

        title.setFont(QFont("Segoe UI", 11, QFont.Bold))

        title.setStyleSheet("""
            color:white;
        """)

        layout.addWidget(title)

        # ------------------------------------------
        # Gauge
        # ------------------------------------------

        self.gauge = ThreatGauge()

        self.gauge.setMinimumSize(150, 130)
        self.gauge.setMaximumSize(150, 130)

        layout.addWidget(
            self.gauge,
            alignment=Qt.AlignCenter
        )

        layout.addStretch()

    # --------------------------------------------------

    def setScore(self, score):

        self.gauge.setScore(score)