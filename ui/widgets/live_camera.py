"""
==========================================================
AI Intrusion Detection System
Live Camera Widget
==========================================================
"""

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from PySide6.QtGui import (
    QPixmap,
    QPainter,
    QColor,
    QPen
)

from PySide6.QtCore import (
    Qt,
    QSize
)

from ui.styles import *


# ==========================================================
# Camera Overlay
# ==========================================================

class CameraOverlay(QWidget):
    """
    Draws the corner brackets over the camera view.
    """

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(QColor("white"))
        pen.setWidth(3)

        painter.setPen(pen)

        margin = 18
        length = 28

        w = self.width()
        h = self.height()

        # Top Left
        painter.drawLine(margin, margin, margin + length, margin)
        painter.drawLine(margin, margin, margin, margin + length)

        # Top Right
        painter.drawLine(w-margin, margin, w-margin-length, margin)
        painter.drawLine(w-margin, margin, w-margin, margin+length)

        # Bottom Left
        painter.drawLine(margin, h-margin, margin+length, h-margin)
        painter.drawLine(margin, h-margin, margin, h-margin-length)

        # Bottom Right
        painter.drawLine(w-margin, h-margin, w-margin-length, h-margin)
        painter.drawLine(w-margin, h-margin, w-margin, h-margin-length)


# ==========================================================
# Live Camera Widget
# ==========================================================

class LiveCamera(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("LiveCamera")

        self.setMinimumSize(760, 470)

        self.setStyleSheet(f"""
        QFrame#LiveCamera {{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:12px;
        }}
        """)

        self.build_ui()

    # ======================================================

    def build_ui(self):

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(15,15,15,15)
        main_layout.setSpacing(10)

        # --------------------------------------------------
        # Header
        # --------------------------------------------------

        header = QHBoxLayout()

        title = QLabel("LIVE CAMERA FEED")

        title.setStyleSheet("""
            color:white;
            font-size:18px;
            font-weight:bold;
        """)

        header.addWidget(title)

        header.addStretch()

        self.rec = QLabel("● REC")

        self.rec.setStyleSheet("""
            color:#ff3b30;
            font-size:14px;
            font-weight:bold;
        """)

        header.addWidget(self.rec)

        main_layout.addLayout(header)

        # --------------------------------------------------
        # Camera Container
        # --------------------------------------------------

        container = QFrame()

        container.setStyleSheet("""
        QFrame{
            background:#090D15;
            border:1px solid #263548;
            border-radius:10px;
        }
        """)

        camera_layout = QVBoxLayout(container)

        camera_layout.setContentsMargins(0,0,0,0)

        self.camera = QLabel()

        self.camera.setAlignment(Qt.AlignCenter)

        self.camera.setText("Waiting for Camera...")

        self.camera.setStyleSheet("""
            color:#9BA6B2;
            font-size:18px;
            border:none;
        """)

        camera_layout.addWidget(self.camera)

        self.overlay = CameraOverlay(self.camera)

        main_layout.addWidget(container)

        # --------------------------------------------------
        # Footer
        # --------------------------------------------------

        footer = QHBoxLayout()

        self.time = QLabel("00-00-0000 00:00:00")

        self.time.setStyleSheet("""
            color:#C7D0DD;
            font-size:12px;
        """)

        footer.addWidget(self.time)

        footer.addStretch()

        self.cam_name = QLabel("CAMERA 01")

        self.cam_name.setStyleSheet("""
            color:white;
            font-size:12px;
            font-weight:bold;
        """)

        footer.addWidget(self.cam_name)

        main_layout.addLayout(footer)

    # ======================================================

    def resizeEvent(self, event):

        self.overlay.resize(self.camera.size())

        super().resizeEvent(event)

    # ======================================================

    def set_frame(self, pixmap: QPixmap):

        self.camera.setPixmap(
            pixmap.scaled(
                self.camera.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

    # ======================================================

    def set_timestamp(self, text):

        self.time.setText(text)

    # ======================================================

    def set_camera_name(self, text):

        self.cam_name.setText(text)

    # ======================================================

    def set_recording(self, recording=True):

        if recording:
            self.rec.setText("● REC")
            self.rec.setStyleSheet("""
                color:#ff3b30;
                font-size:14px;
                font-weight:bold;
            """)
        else:
            self.rec.setText("OFFLINE")
            self.rec.setStyleSheet("""
                color:#808080;
                font-size:14px;
                font-weight:bold;
            """)