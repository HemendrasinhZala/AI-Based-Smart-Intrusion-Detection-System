"""
==========================================================
AI Intrusion Detection System
Database Page
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
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from PySide6.QtCore import Qt

from ui.styles import ACCENT, BORDER, CARD, PANEL


class DatabasePage(QWidget):

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

        title = QLabel("DATABASE")

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

        self.search = QLineEdit()

        self.search.setPlaceholderText("Search records...")

        self.search.setMinimumHeight(40)

        self.search.setStyleSheet(f"""
        QLineEdit {{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:8px;
            color:white;
            padding-left:12px;
            font-size:14px;
        }}
        """)

        toolbar.addWidget(self.search)

        self.refresh_btn = QPushButton("Refresh")
        self.export_btn = QPushButton("Export CSV")

        for btn in [self.refresh_btn, self.export_btn]:

            btn.setMinimumHeight(40)

            btn.setStyleSheet(f"""
            QPushButton {{
                background:{ACCENT};
                color:white;
                border:none;
                border-radius:8px;
                padding:0px 20px;
                font-size:14px;
                font-weight:bold;
            }}

            QPushButton:hover {{
                background:#2563EB;
            }}
            """)

            toolbar.addWidget(btn)

        main_layout.addLayout(toolbar)

        # ==================================================
        # Database Table
        # ==================================================

        table_frame = QFrame()

        table_frame.setStyleSheet(f"""
        QFrame {{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:12px;
        }}
        """)

        table_layout = QVBoxLayout(table_frame)

        table_layout.setContentsMargins(15,15,15,15)

        self.table = QTableWidget()

        self.table.setColumnCount(7)

        self.table.setHorizontalHeaderLabels([
            "Date",
            "Time",
            "Threat",
            "Humans",
            "Motion",
            "Door",
            "Status"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.table.verticalHeader().setVisible(False)

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        self.table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        self.table.setStyleSheet(f"""
        QTableWidget {{
            background:{PANEL};
            color:white;
            border:none;
            gridline-color:{BORDER};
            font-size:13px;
        }}

        QHeaderView::section {{
            background:{CARD};
            color:white;
            padding:8px;
            border:none;
            border-bottom:1px solid {BORDER};
            font-weight:bold;
        }}

        QTableWidget::item:selected {{
            background:{ACCENT};
        }}
        """)

        table_layout.addWidget(self.table)

        main_layout.addWidget(table_frame)

        # ==================================================
        # Sample Data (Temporary)
        # ==================================================

        self.load_sample_data()

    # ======================================================

    def load_sample_data(self):

        sample = [
            ["05-07-2026", "10:15:32", "82", "2", "Detected", "Open", "High"],
            ["05-07-2026", "10:08:15", "48", "1", "Detected", "Closed", "Medium"],
            ["05-07-2026", "09:52:41", "20", "0", "None", "Closed", "Low"],
        ]

        self.table.setRowCount(len(sample))

        for row, values in enumerate(sample):

            for col, value in enumerate(values):

                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)

                self.table.setItem(row, col, item)