"""
==========================================================
AI Intrusion Detection System
Main Window

Author : Hemendrasinh Zala
==========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget
)

from ui.styles import BACKGROUND
from ui.sidebar import Sidebar
from ui.topbar import TopBar

# Pages
from ui.pages.dashboard_page import DashboardPage
from ui.pages.camera_page import CameraPage
from ui.pages.gallery_page import GalleryPage
from ui.pages.database_page import DatabasePage
from ui.pages.logs_page import LogsPage
from ui.pages.alerts_page import AlertsPage
from ui.pages.settings_page import SettingsPage
from ui.pages.about_page import AboutPage


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Intrusion Detection System")
        self.resize(1600, 900)

        self.setStyleSheet(f"""
        QWidget {{
            background:{BACKGROUND};
        }}
        """)

        self.build_ui()

    # ======================================================

    def build_ui(self):

        # --------------------------------------------------
        # Main Layout
        # --------------------------------------------------

        main_layout = QHBoxLayout(self)

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # --------------------------------------------------
        # Sidebar
        # --------------------------------------------------

        self.sidebar = Sidebar()

        # --------------------------------------------------
        # Right Side
        # --------------------------------------------------

        right_widget = QWidget()

        right_layout = QVBoxLayout(right_widget)

        right_layout.setContentsMargins(20, 15, 20, 20)
        right_layout.setSpacing(18)

        # --------------------------------------------------
        # Top Bar
        # --------------------------------------------------

        self.topbar = TopBar()

        # --------------------------------------------------
        # Stacked Pages
        # --------------------------------------------------

        self.pages = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.camera_page = CameraPage()
        self.gallery_page = GalleryPage()
        self.database_page = DatabasePage()
        self.logs_page = LogsPage()
        self.alerts_page = AlertsPage()
        self.settings_page = SettingsPage()
        self.about_page = AboutPage()

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.camera_page)
        self.pages.addWidget(self.gallery_page)
        self.pages.addWidget(self.database_page)
        self.pages.addWidget(self.logs_page)
        self.pages.addWidget(self.alerts_page)
        self.pages.addWidget(self.settings_page)
        self.pages.addWidget(self.about_page)

        # --------------------------------------------------
        # Add Widgets
        # --------------------------------------------------

        right_layout.addWidget(self.topbar)
        right_layout.addWidget(self.pages)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(right_widget)

        # Sidebar width fixed
        main_layout.setStretch(0, 0)
        main_layout.setStretch(1, 1)

        # --------------------------------------------------
        # Connections
        # --------------------------------------------------

        self.connect_sidebar()

    # ======================================================

    def connect_sidebar(self):

        self.sidebar.dashboard_btn.clicked.connect(
            lambda: self.pages.setCurrentIndex(0)
        )

        self.sidebar.camera_btn.clicked.connect(
            lambda: self.pages.setCurrentIndex(1)
        )

        self.sidebar.gallery_btn.clicked.connect(
            lambda: self.pages.setCurrentIndex(2)
        )

        self.sidebar.database_btn.clicked.connect(
            lambda: self.pages.setCurrentIndex(3)
        )

        self.sidebar.logs_btn.clicked.connect(
            lambda: self.pages.setCurrentIndex(4)
        )

        self.sidebar.alerts_btn.clicked.connect(
            lambda: self.pages.setCurrentIndex(5)
        )

        self.sidebar.settings_btn.clicked.connect(
            lambda: self.pages.setCurrentIndex(6)
        )

        self.sidebar.about_btn.clicked.connect(
            lambda: self.pages.setCurrentIndex(7)
        )