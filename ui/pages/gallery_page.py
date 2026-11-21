"""
==========================================================
AI Intrusion Detection System
Gallery Page
==========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QPushButton,
    QListWidget,
    QSizePolicy
)

from PySide6.QtCore import Qt

from ui.styles import CARD, BORDER, PANEL, ACCENT


class GalleryPage(QWidget):

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

        title = QLabel("GALLERY")

        title.setStyleSheet("""
            color:white;
            font-size:26px;
            font-weight:700;
            border:none;
        """)

        main_layout.addWidget(title)

        # ==================================================
        # Content
        # ==================================================

        content_layout = QHBoxLayout()
        content_layout.setSpacing(15)

        # ==================================================
        # Left Panel
        # ==================================================

        left_panel = QFrame()

        left_panel.setStyleSheet(f"""
        QFrame{{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:12px;
        }}
        """)

        left_layout = QVBoxLayout(left_panel)

        left_layout.setContentsMargins(15,15,15,15)

        left_title = QLabel("Captured Images")

        left_title.setStyleSheet("""
            color:white;
            font-size:18px;
            font-weight:bold;
            border:none;
        """)

        left_layout.addWidget(left_title)

        self.image_list = QListWidget()

        self.image_list.setStyleSheet(f"""
        QListWidget{{
            background:{PANEL};
            border:1px solid {BORDER};
            border-radius:8px;
            color:white;
            font-size:13px;
            padding:6px;
        }}
        """)

        left_layout.addWidget(self.image_list)

        # ==================================================
        # Right Panel
        # ==================================================

        right_panel = QFrame()

        right_panel.setStyleSheet(f"""
        QFrame{{
            background:{CARD};
            border:1px solid {BORDER};
            border-radius:12px;
        }}
        """)

        right_layout = QVBoxLayout(right_panel)

        right_layout.setContentsMargins(15,15,15,15)

        preview_title = QLabel("Image Preview")

        preview_title.setStyleSheet("""
            color:white;
            font-size:18px;
            font-weight:bold;
            border:none;
        """)

        right_layout.addWidget(preview_title)

        self.preview = QLabel("No Image Selected")

        self.preview.setAlignment(Qt.AlignCenter)

        self.preview.setMinimumHeight(420)

        self.preview.setStyleSheet(f"""
        QLabel{{
            background:{PANEL};
            border:1px solid {BORDER};
            border-radius:10px;
            color:#9BA6B2;
            font-size:18px;
        }}
        """)

        right_layout.addWidget(self.preview)

        # ==================================================
        # Buttons
        # ==================================================

        button_layout = QHBoxLayout()

        self.open_btn = QPushButton("Open")

        self.delete_btn = QPushButton("Delete")

        self.refresh_btn = QPushButton("Refresh")

        for btn in [self.open_btn, self.delete_btn, self.refresh_btn]:

            btn.setMinimumHeight(42)

            btn.setStyleSheet(f"""
            QPushButton{{
                background:{ACCENT};
                color:white;
                border:none;
                border-radius:8px;
                font-size:14px;
                font-weight:bold;
            }}

            QPushButton:hover{{
                background:#2563EB;
            }}
            """)

            button_layout.addWidget(btn)

        right_layout.addLayout(button_layout)

        # ==================================================
        # Sizes
        # ==================================================

        left_panel.setMaximumWidth(350)

        left_panel.setSizePolicy(
            QSizePolicy.Fixed,
            QSizePolicy.Expanding
        )

        content_layout.addWidget(left_panel)

        content_layout.addWidget(right_panel)

        main_layout.addLayout(content_layout)