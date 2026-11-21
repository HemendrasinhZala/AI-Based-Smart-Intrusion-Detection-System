"""
==========================================================
AI Intrusion Detection System
Camera Page
==========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame
)

from PySide6.QtCore import Qt

from ui.styles import *


class CameraPage(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    # ======================================================

    def build_ui(self):

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(15)

        # --------------------------------------------------
        # Page Title
        # --------------------------------------------------

        title = QLabel("CAMERA")

        title.setStyleSheet("""
            color:white;
            font-size:26px;
            font-weight:700;
            border:none;
        """)

        main_layout.addWidget(title)

        # --------------------------------------------------
        # Camera Container
        # --------------------------------------------------

        self.camera_frame = QFrame()

        self.camera_frame.setStyleSheet(f"""
        QFrame {{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:12px;
        }}
        """)

        camera_layout = QVBoxLayout(self.camera_frame)

        camera_layout.setContentsMargins(20,20,20,20)

        self.camera_label = QLabel("Live Camera Feed")

        self.camera_label.setAlignment(Qt.AlignCenter)

        self.camera_label.setStyleSheet("""
            color:#BFC8D6;
            font-size:22px;
            border:none;
        """)

        camera_layout.addWidget(self.camera_label)

        main_layout.addWidget(self.camera_frame)

        # Fill remaining space
        main_layout.addStretch()