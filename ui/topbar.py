"""
==========================================================
AI Intrusion Detection System
topbar.py

Top Navigation Bar

Author : Hemendrasinh Zala
==========================================================
"""

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
)

from PySide6.QtCore import Qt, QTimer, QDateTime
from PySide6.QtGui import QFont

from ui.styles import *


class TopBar(QFrame):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(80)
        self.setObjectName("TopBar")

        self.setStyleSheet(f"""
        QFrame#TopBar {{
            background-color: {PANEL};
            border: 1px solid {BORDER};
            border-radius: 12px;
        }}
        """)

        self.build_ui()

        # Timer for live clock
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)

        self.update_datetime()

    # ----------------------------------------------------
    # Build UI
    # ----------------------------------------------------

    def build_ui(self):

        main_layout = QHBoxLayout(self)

        main_layout.setContentsMargins(20, 10, 20, 10)
        main_layout.setSpacing(20)

        # ============================
        # Left Section (Page Title)
        # ============================

        self.page_title = QLabel("Dashboard")
        self.page_title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        self.page_title.setStyleSheet(f"color:{TEXT};")

        main_layout.addWidget(self.page_title)

        main_layout.addStretch()

        # ============================
        # Status
        # ============================

        self.status = QLabel("🟢 System Online")
        self.status.setFont(QFont("Segoe UI", 11))
        self.status.setStyleSheet(f"""
            color:{GREEN};
            font-weight:bold;
        """)

        main_layout.addWidget(self.status)

        # ============================
        # Date & Time
        # ============================

        datetime_layout = QVBoxLayout()
        datetime_layout.setSpacing(2)

        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignRight)

        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignRight)

        self.date_label.setStyleSheet(f"""
            color:{TEXT_SECONDARY};
            font-size:12px;
        """)

        self.time_label.setStyleSheet(f"""
            color:{TEXT};
            font-size:16px;
            font-weight:bold;
        """)

        datetime_layout.addWidget(self.date_label)
        datetime_layout.addWidget(self.time_label)

        main_layout.addLayout(datetime_layout)

    # ----------------------------------------------------
    # Update Date & Time
    # ----------------------------------------------------

    def update_datetime(self):

        current = QDateTime.currentDateTime()

        self.date_label.setText(
            current.toString("dddd, dd MMMM yyyy")
        )

        self.time_label.setText(
            current.toString("hh:mm:ss AP")
        )

    # ----------------------------------------------------
    # Change Page Title
    # ----------------------------------------------------

    def set_page_title(self, title):

        self.page_title.setText(title)

    # ----------------------------------------------------
    # Change System Status
    # ----------------------------------------------------

    def set_system_status(self, online=True):

        if online:
            self.status.setText("🟢 System Online")
            self.status.setStyleSheet(f"""
                color:{GREEN};
                font-weight:bold;
            """)
        else:
            self.status.setText("🔴 System Offline")
            self.status.setStyleSheet(f"""
                color:{RED};
                font-weight:bold;
            """)