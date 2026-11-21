"""
==========================================================
AI Intrusion Detection System
styles.py

This file contains all reusable UI styles.
Every UI file imports styles from here.

Author : Hemendrasinh Zala
==========================================================
"""

# ==========================================================
# COLOR PALETTE
# ==========================================================

# Main Background
BACKGROUND = "#0B1220"

# Panels
PANEL = "#121B2D"

# Cards
CARD = "#162238"

# Sidebar
SIDEBAR = "#0D1626"

# Borders
BORDER = "#27344D"

# Text
TEXT = "#FFFFFF"
TEXT_SECONDARY = "#A8B3C7"

# Accent Colors
BLUE = "#2563EB"
BLUE_HOVER = "#3B82F6"

GREEN = "#22C55E"
GREEN_HOVER = "#16A34A"

RED = "#EF4444"
RED_HOVER = "#DC2626"

ORANGE = "#F59E0B"
ORANGE_HOVER = "#D97706"

YELLOW = "#FACC15"

CYAN = "#06B6D4"

PURPLE = "#8B5CF6"

# ==========================================================
# FONTS
# ==========================================================

FONT_FAMILY = "Segoe UI"

TITLE_FONT = 30
HEADER_FONT = 22
SUBHEADER_FONT = 18
BODY_FONT = 14
SMALL_FONT = 12

# ==========================================================
# BORDER RADIUS
# ==========================================================

WINDOW_RADIUS = 15
CARD_RADIUS = 14
BUTTON_RADIUS = 10

# ==========================================================
# PADDING
# ==========================================================

SMALL_PADDING = 6
NORMAL_PADDING = 10
LARGE_PADDING = 15

# ==========================================================
# ICON SIZE
# ==========================================================

SIDEBAR_ICON = 24
CARD_ICON = 42
TOPBAR_ICON = 28

# ==========================================================
# BUTTON HEIGHT
# ==========================================================

BUTTON_HEIGHT = 48

# ==========================================================
# WINDOW STYLESHEET
# ==========================================================

MAIN_WINDOW_STYLE = f"""

QMainWindow {{
    background-color: {BACKGROUND};
}}

QWidget {{
    background-color: transparent;
    color: {TEXT};
    font-family: "{FONT_FAMILY}";
    font-size: {BODY_FONT}px;
}}

"""

# ==========================================================
# SIDEBAR STYLE
# ==========================================================

SIDEBAR_STYLE = f"""

QFrame {{
    background-color: {SIDEBAR};
    border: 1px solid {BORDER};
    border-radius: 15px;
}}

"""

# ==========================================================
# CARD STYLE
# ==========================================================

CARD_STYLE = f"""

QFrame {{
    background-color: {CARD};
    border: 1px solid {BORDER};
    border-radius: 14px;
}}

"""

# ==========================================================
# TITLE LABEL STYLE
# ==========================================================

TITLE_STYLE = f"""

QLabel {{
    color: {TEXT};
    font-size: {TITLE_FONT}px;
    font-weight: bold;
}}

"""

# ==========================================================
# HEADING STYLE
# ==========================================================

HEADING_STYLE = f"""

QLabel {{
    color: {TEXT};
    font-size: {HEADER_FONT}px;
    font-weight: 600;
}}

"""

# ==========================================================
# SUBHEADING STYLE
# ==========================================================

SUBHEADING_STYLE = f"""

QLabel {{
    color: {TEXT_SECONDARY};
    font-size: {SUBHEADER_FONT}px;
}}

"""

# ==========================================================
# PRIMARY BUTTON
# ==========================================================

PRIMARY_BUTTON = f"""

QPushButton {{

    background-color: {BLUE};
    color: white;
    border: none;
    border-radius: {BUTTON_RADIUS}px;
    padding: 10px;
    min-height: {BUTTON_HEIGHT}px;
    font-weight: bold;

}}

QPushButton:hover {{

    background-color: {BLUE_HOVER};

}}

QPushButton:pressed {{

    padding-top: 2px;

}}

"""

# ==========================================================
# SUCCESS BUTTON
# ==========================================================

SUCCESS_BUTTON = f"""

QPushButton {{

    background-color: {GREEN};
    color: white;
    border: none;
    border-radius: {BUTTON_RADIUS}px;
    padding: 10px;
    min-height: {BUTTON_HEIGHT}px;
    font-weight: bold;

}}

QPushButton:hover {{

    background-color: {GREEN_HOVER};

}}

"""

# ==========================================================
# DANGER BUTTON
# ==========================================================

DANGER_BUTTON = f"""

QPushButton {{

    background-color: {RED};
    color: white;
    border: none;
    border-radius: {BUTTON_RADIUS}px;
    padding: 10px;
    min-height: {BUTTON_HEIGHT}px;
    font-weight: bold;

}}

QPushButton:hover {{

    background-color: {RED_HOVER};

}}

"""

# ==========================================================
# WARNING BUTTON
# ==========================================================

WARNING_BUTTON = f"""

QPushButton {{

    background-color: {ORANGE};
    color: white;
    border: none;
    border-radius: {BUTTON_RADIUS}px;
    padding: 10px;
    min-height: {BUTTON_HEIGHT}px;
    font-weight: bold;

}}

QPushButton:hover {{

    background-color: {ORANGE_HOVER};

}}

"""

# ==========================================================
# STATUS LABELS
# ==========================================================

ONLINE_STYLE = f"""
QLabel {{
    color: {GREEN};
    font-weight: bold;
}}
"""

OFFLINE_STYLE = f"""
QLabel {{
    color: {RED};
    font-weight: bold;
}}
"""

WARNING_STYLE = f"""
QLabel {{
    color: {ORANGE};
    font-weight: bold;
}}
"""

# ==========================================================
# LINE EDIT STYLE
# ==========================================================

LINE_EDIT_STYLE = f"""

QLineEdit {{

    background-color: {PANEL};
    border: 1px solid {BORDER};
    border-radius: 8px;
    padding: 8px;
    color: {TEXT};

}}

QLineEdit:focus {{

    border: 1px solid {BLUE};

}}

"""

# ==========================================================
# SCROLL BAR
# ==========================================================

SCROLLBAR_STYLE = f"""

QScrollBar:vertical {{

    border: none;
    background: {BACKGROUND};
    width: 10px;
    margin: 0px;

}}

QScrollBar::handle:vertical {{

    background: {BLUE};
    border-radius: 5px;

}}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{

    height: 0px;

}}

"""

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def panel_style():
    """Return panel/card stylesheet."""
    return CARD_STYLE


def sidebar_style():
    """Return sidebar stylesheet."""
    return SIDEBAR_STYLE


def primary_button():
    """Return primary button stylesheet."""
    return PRIMARY_BUTTON


def success_button():
    """Return success button stylesheet."""
    return SUCCESS_BUTTON


def danger_button():
    """Return danger button stylesheet."""
    return DANGER_BUTTON


def warning_button():
    """Return warning button stylesheet."""
    return WARNING_BUTTON