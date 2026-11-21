from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout

from ui.widgets.large_status_card import LargeStatusCard

app = QApplication([])

window = QWidget()
window.setWindowTitle("Large Status Card Test")
window.resize(500, 250)

layout = QHBoxLayout(window)

threat = LargeStatusCard(
    "THREAT LEVEL",
    "fa6s.shield-halved",
    "HIGH",
    "Take Action",
    "#ff3b30",
    "#ff3b30"
)

human = LargeStatusCard(
    "HUMAN COUNT",
    "fa6s.user",
    "2",
    "Detected",
    "#3B82F6",
    "white"
)

layout.addWidget(threat)
layout.addWidget(human)

window.show()

app.exec()