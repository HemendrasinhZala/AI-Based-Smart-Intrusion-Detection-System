"""
==========================================================
AI Intrusion Detection System
Dashboard Layout

Author : Hemendrasinh Zala
==========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
    QFrame,
    QVBoxLayout
)

from ui.widgets.live_camera import LiveCamera
from ui.widgets.system_status import SystemStatus

from ui.styles import CARD_STYLE


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    # -------------------------------------------------------
    # Placeholder Panel
    # -------------------------------------------------------

    def placeholder(self, title):

        panel = QFrame()

        panel.setStyleSheet(CARD_STYLE)

        layout = QVBoxLayout(panel)

        label = QLabel(title)

        label.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
            color:white;
        """)

        layout.addWidget(label)

        layout.addStretch()

        return panel

    # -------------------------------------------------------

    def build_ui(self):

        layout = QGridLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        layout.setHorizontalSpacing(18)
        layout.setVerticalSpacing(18)

        # ==================================================
        # Widgets
        # ==================================================

        self.camera = LiveCamera()

        self.system_status = SystemStatus()

        self.timeline = self.placeholder("Event Timeline")

        self.gallery = self.placeholder("Recent Captures")

        self.recordings = self.placeholder("Recent Recordings")

        self.controls = self.placeholder("System Controls")

        # ==================================================
        # Layout
        # ==================================================

        # Row 1

        layout.addWidget(self.camera, 0, 0)

        layout.addWidget(self.system_status, 0, 1)

        # Row 2

        layout.addWidget(self.timeline, 1, 0)

        layout.addWidget(self.gallery, 1, 1)

        # Row 3

        layout.addWidget(self.recordings, 2, 1)

        # Row 4

        layout.addWidget(self.controls, 3, 0, 1, 2)

        # ==================================================
        # Stretch Factors
        # ==================================================

        layout.setColumnStretch(0, 6)

        layout.setColumnStretch(1, 4)

        layout.setRowStretch(0, 5)

        layout.setRowStretch(1, 2)

        layout.setRowStretch(2, 2)

        layout.setRowStretch(3, 1)