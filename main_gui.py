"""
===========================================================
AI Intrusion Detection System

Main GUI Application

Author : Hemendrasinh Zala

This is the graphical entry point of the application.

Responsibilities
----------------
1. Initialize the Qt Application.
2. Apply the global UI theme.
3. Create the Main Window.
4. Launch the dashboard.

===========================================================
"""

import sys

from PySide6.QtWidgets import QApplication

from ui.styles import GLOBAL_STYLE
from ui.main_window import MainWindow


# ==========================================================
# MAIN APPLICATION
# ==========================================================

def main():
    """
    Start the GUI application.
    """

    # ------------------------------------------------------
    # Create Application
    # ------------------------------------------------------

    app = QApplication(sys.argv)

    # ------------------------------------------------------
    # Application Information
    # ------------------------------------------------------

    app.setApplicationName(
        "AI Intrusion Detection System"
    )

    app.setOrganizationName(
        "AI Intrusion Detection"
    )

    app.setApplicationVersion(
        "1.0.0"
    )

    # ------------------------------------------------------
    # Apply Global Theme
    # ------------------------------------------------------

    app.setStyleSheet(GLOBAL_STYLE)

    # ------------------------------------------------------
    # Create Main Window
    # ------------------------------------------------------

    window = MainWindow()

    window.show()

    # ------------------------------------------------------
    # Run Application
    # ------------------------------------------------------

    sys.exit(app.exec())


# ==========================================================
# ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print()

        print("Application Closed.")

    except Exception as error:

        print()

        print(f"Unexpected Error : {error}")