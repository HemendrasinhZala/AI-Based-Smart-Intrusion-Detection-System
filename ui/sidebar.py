"""
==========================================================
AI Intrusion Detection System
sidebar.py

Left Navigation Sidebar

Author : Hemendrasinh Zala
==========================================================
"""

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)

from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt

from ui.sidebar_button import SidebarButton
from ui.styles import *


class Sidebar(QFrame):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(270)
        self.setObjectName("Sidebar")

        self.setStyleSheet(f"""
        QFrame#Sidebar{{
            background-color:{SIDEBAR};
            border-right:1px solid {BORDER};
        }}
        """)

        self.build_ui()

    # ----------------------------------------------------
    # Build Sidebar
    # ----------------------------------------------------

    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        # ==========================================
        # Logo + Project Title
        # ==========================================

        header_layout = QHBoxLayout()
        header_layout.setSpacing(12)

        logo = QLabel()
        logo.setFixedSize(48, 48)

        pixmap = QPixmap("assets/icons/logo.svg")
        logo.setPixmap(
            pixmap.scaled(
                48,
                48,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        title = QLabel("AI Intrusion")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setStyleSheet(f"color:{TEXT};")

        subtitle = QLabel("Detection System")
        subtitle.setFont(QFont("Segoe UI", 11))
        subtitle.setStyleSheet(f"color:{TEXT_SECONDARY};")

        text_layout = QVBoxLayout()
        text_layout.setSpacing(0)
        text_layout.addWidget(title)
        text_layout.addWidget(subtitle)

        header_layout.addWidget(logo)
        header_layout.addLayout(text_layout)

        header_widget = QWidget()
        header_widget.setLayout(header_layout)

        layout.addWidget(header_widget)

        layout.addSpacing(25)

        # ==========================================
        # Navigation Buttons
        # ==========================================

        self.dashboard_btn = SidebarButton(
            "Dashboard",
            "assets/icons/dashboard.svg"
        )

        self.camera_btn = SidebarButton(
            "Camera",
            "assets/icons/camera.svg"
        )

        self.gallery_btn = SidebarButton(
            "Gallery",
            "assets/icons/gallery.svg"
        )

        self.database_btn = SidebarButton(
            "Database",
            "assets/icons/database.svg"
        )

        self.logs_btn = SidebarButton(
            "Logs",
            "assets/icons/logs.svg"
        )

        self.alerts_btn = SidebarButton(
            "Alerts",
            "assets/icons/alerts.svg"
        )

        self.settings_btn = SidebarButton(
            "Settings",
            "assets/icons/settings.svg"
        )

        self.about_btn = SidebarButton(
            "About",
            "assets/icons/about.svg"
        )

        # Default Active Button
        self.dashboard_btn.set_active(True)

        buttons = [
            self.dashboard_btn,
            self.camera_btn,
            self.gallery_btn,
            self.database_btn,
            self.logs_btn,
            self.alerts_btn,
            self.settings_btn,
            self.about_btn
        ]

        for button in buttons:
            layout.addWidget(button)

        layout.addStretch()

        # ==========================================
        # Footer
        # ==========================================

        footer = QLabel("AI Intrusion Detection System\nVersion 1.0")

        footer.setAlignment(Qt.AlignCenter)

        footer.setStyleSheet(f"""
            color:{TEXT_SECONDARY};
            font-size:11px;
        """)

        layout.addWidget(footer)

        # ==========================================
        # Navigation Connections
        # ==========================================

        self.buttons = buttons

        for btn in self.buttons:
            btn.clicked.connect(
                lambda checked, b=btn: self.change_active_button(b)
            )

    # ----------------------------------------------------
    # Change Active Button
    # ----------------------------------------------------

    def change_active_button(self, selected_button):

        for btn in self.buttons:
            btn.setChecked(False)

        selected_button.setChecked(True)