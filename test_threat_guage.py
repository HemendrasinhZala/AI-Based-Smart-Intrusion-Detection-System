import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from PySide6.QtWidgets import QApplication
from ui.widgets.threat_gauge import ThreatGauge #type:ignore

app = QApplication([])

gauge = ThreatGauge()
gauge.show()

app.exec()