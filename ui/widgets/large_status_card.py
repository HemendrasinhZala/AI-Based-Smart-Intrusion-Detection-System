"""
==========================================================
AI Intrusion Detection System
Large Status Card
==========================================================
"""

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

import qtawesome as qta

from ui.styles import *


class LargeStatusCard(QFrame):

    def __init__(
        self,
        title,
        icon_name,
        value,
        subtitle,
        icon_color="#ffffff",
        value_color="#ffffff"
    ):
        super().__init__()

        self.setObjectName("LargeStatusCard")

        self.setMinimumSize(180, 205)
        self.setMaximumHeight(205)

        self.setStyleSheet(f"""
        QFrame#LargeStatusCard {{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:10px;
        }}
        QLabel {{
            border:none;
        }}
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)

        # --------------------------------------------------
        # Title
        # --------------------------------------------------

        self.title = QLabel(title)

        self.title.setAlignment(Qt.AlignCenter)

        self.title.setFont(QFont("Segoe UI", 11, QFont.Bold))

        self.title.setStyleSheet("""
            color:white;
        """)

        layout.addWidget(self.title)

        # --------------------------------------------------
        # Icon
        # --------------------------------------------------

        self.icon = QLabel()

        self.icon.setAlignment(Qt.AlignCenter)

        icon = qta.icon(
            icon_name,
            color=icon_color
        )

        self.icon.setPixmap(icon.pixmap(72, 72))

        layout.addWidget(self.icon)

        # --------------------------------------------------
        # Value
        # --------------------------------------------------

        self.value = QLabel(value)

        self.value.setAlignment(Qt.AlignCenter)

        self.value.setFont(QFont("Segoe UI", 18, QFont.Bold))

        self.value.setStyleSheet(f"""
            color:{value_color};
        """)

        layout.addWidget(self.value)

        # --------------------------------------------------
        # Subtitle
        # --------------------------------------------------

        self.subtitle = QLabel(subtitle)

        self.subtitle.setAlignment(Qt.AlignCenter)

        self.subtitle.setFont(QFont("Segoe UI", 10))

        self.subtitle.setStyleSheet("""
            color:#D6DCE7;
        """)

        layout.addWidget(self.subtitle)

        layout.addStretch()

    # =====================================================

    def setValue(self, value):
        self.value.setText(value)

    def setSubtitle(self, text):
        self.subtitle.setText(text)

    def setIcon(self, icon_name, color):
        icon = qta.icon(icon_name, color=color)
        self.icon.setPixmap(icon.pixmap(72, 72))