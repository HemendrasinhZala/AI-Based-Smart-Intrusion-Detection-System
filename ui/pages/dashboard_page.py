"""
==========================================================
AI Intrusion Detection System
Dashboard Page
==========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)

from ui.dashboard import Dashboard


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    # ======================================================

    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Dashboard Widget
        self.dashboard = Dashboard()

        layout.addWidget(self.dashboard)