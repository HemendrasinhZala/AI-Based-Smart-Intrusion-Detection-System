"""
==========================================================
AI Intrusion Detection System
Logs Page
==========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QPushButton,
    QLineEdit,
    QTextEdit
)

from ui.styles import *


class LogsPage(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    # ======================================================

    def build_ui(self):

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(15)

        # ==================================================
        # Title
        # ==================================================

        title = QLabel("SYSTEM LOGS")

        title.setStyleSheet("""
            color:white;
            font-size:26px;
            font-weight:700;
            border:none;
        """)

        main_layout.addWidget(title)

        # ==================================================
        # Toolbar
        # ==================================================

        toolbar = QHBoxLayout()

        self.search_box = QLineEdit()

        self.search_box.setPlaceholderText("Search logs...")

        self.search_box.setMinimumHeight(40)

        self.search_box.setStyleSheet(f"""
        QLineEdit {{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:8px;
            color:white;
            padding-left:12px;
            font-size:14px;
        }}
        """)

        toolbar.addWidget(self.search_box)

        self.refresh_btn = QPushButton("Refresh")
        self.clear_btn = QPushButton("Clear")
        self.save_btn = QPushButton("Save")

        for btn in [
            self.refresh_btn,
            self.clear_btn,
            self.save_btn
        ]:

            btn.setMinimumHeight(40)

            btn.setStyleSheet("""
            QPushButton {
                background:#2563EB;
                color:white;
                border:none;
                border-radius:8px;
                padding:0px 18px;
                font-size:14px;
                font-weight:bold;
            }

            QPushButton:hover {
                background:#2563EB;
            }
            """)

            toolbar.addWidget(btn)

        main_layout.addLayout(toolbar)

        # ==================================================
        # Log Viewer
        # ==================================================

        frame = QFrame()

        frame.setStyleSheet(f"""
        QFrame {{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:12px;
        }}
        """)

        frame_layout = QVBoxLayout(frame)

        frame_layout.setContentsMargins(15,15,15,15)

        self.log_view = QTextEdit()

        self.log_view.setReadOnly(True)

        self.log_view.setStyleSheet(f"""
        QTextEdit {{
            background:{PANEL};
            border:none;
            color:#E5E7EB;
            font-family:Consolas;
            font-size:13px;
            padding:10px;
        }}
        """)

        frame_layout.addWidget(self.log_view)

        main_layout.addWidget(frame)

        # ==================================================
        # Temporary Logs
        # ==================================================

        self.load_sample_logs()

    # ======================================================

    def load_sample_logs(self):

        logs = [
            "[INFO]  Camera initialized successfully.",
            "[INFO]  Motion detection started.",
            "[WARNING] Motion detected near main entrance.",
            "[INFO]  Human detected (Confidence: 94%).",
            "[INFO]  Image captured successfully.",
            "[INFO]  Video recording started.",
            "[ERROR] Network connection unavailable.",
            "[INFO]  Threat Level: HIGH (82/100).",
            "[INFO]  Alert sent successfully."
        ]

        self.log_view.setPlainText("\n".join(logs))

    # ======================================================

    def append_log(self, message):

        self.log_view.append(message)

    # ======================================================

    def clear_logs(self):

        self.log_view.clear()