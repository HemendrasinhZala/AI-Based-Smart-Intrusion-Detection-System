"""
==========================================================
AI Intrusion Detection System
sidebar_button.py

Reusable Sidebar Navigation Button

Author : Hemendrasinh Zala
==========================================================
"""

from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt

from ui.styles import *


class SidebarButton(QPushButton):
    """
    Reusable navigation button for the sidebar.
    """

    def __init__(self, text, icon_path):
        super().__init__()

        self.setText(text)

        self.setIcon(QIcon(icon_path))

        self.setIconSize(QSize(22, 22))

        self.setCursor(Qt.PointingHandCursor)

        self.setCheckable(True)

        self.setFixedHeight(52)

        self.setStyleSheet(self.default_style())

    # -------------------------------------------------
    # Default Style
    # -------------------------------------------------

    def default_style(self):

        return f"""
        QPushButton {{

            background: transparent;
            color: {TEXT};

            border: none;
            border-radius: 12px;

            text-align: left;

            padding-left: 18px;

            font-size: 15px;
            font-weight: 500;

        }}

        QPushButton:hover {{

            background-color: rgba(37,99,235,70);

        }}

        QPushButton:checked {{

            background-color: {BLUE};

            color: white;

            font-weight: bold;

        }}

        QPushButton:pressed {{

            background-color: {BLUE_HOVER};

        }}
        """

    # -------------------------------------------------
    # Active State
    # -------------------------------------------------

    def set_active(self, active=True):
        """
        Highlight the selected sidebar button.
        """
        self.setChecked(active)