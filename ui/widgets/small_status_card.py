"""
==========================================================
AI Intrusion Detection System
Small Status Card
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


class SmallStatusCard(QFrame):

    def __init__(
        self,
        title,
        icon_name,
        value,
        icon_color="#4CAF50",
        value_color="#FFFFFF"
    ):
        super().__init__()

        self.setObjectName("SmallStatusCard")

        self.setMinimumSize(105, 120)
        self.setMaximumHeight(120)

        self.setStyleSheet(f"""
        QFrame#SmallStatusCard {{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:10px;
        }}

        QLabel {{
            border:none;
        }}
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # ============================================
        # Title
        # ============================================

        self.title = QLabel(title)

        self.title.setAlignment(Qt.AlignCenter)

        self.title.setFont(QFont("Segoe UI", 9, QFont.Bold))

        self.title.setStyleSheet("""
            color:#BFC8D6;
        """)

        layout.addWidget(self.title)

        # ============================================
        # Icon
        # ============================================

        self.icon = QLabel()

        self.icon.setAlignment(Qt.AlignCenter)

        icon = qta.icon(
            icon_name,
            color=icon_color
        )

        self.icon.setPixmap(icon.pixmap(32, 32))

        layout.addWidget(self.icon)

        # ============================================
        # Value
        # ============================================

        self.value = QLabel(value)

        self.value.setAlignment(Qt.AlignCenter)

        self.value.setFont(QFont("Segoe UI", 11, QFont.Bold))

        self.value.setStyleSheet(f"""
            color:{value_color};
        """)

        layout.addWidget(self.value)

        layout.addStretch()

    # ==================================================
    # Update Methods
    # ==================================================

    def setValue(self, text):
        self.value.setText(text)

    def setIcon(self, icon_name, color):

        icon = qta.icon(
            icon_name,
            color=color
        )

        self.icon.setPixmap(icon.pixmap(32, 32))