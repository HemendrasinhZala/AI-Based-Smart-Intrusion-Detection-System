"""
==========================================================
AI Intrusion Detection System
Threat Gauge Widget
==========================================================
"""

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPainter,
    QPen,
    QColor,
    QFont,
    QConicalGradient
)
from PySide6.QtCore import Qt, QRectF


class ThreatGauge(QWidget):

    def __init__(self):
        super().__init__()

        self.score = 82
        self.maximum = 100

        self.setMinimumSize(180, 170)
        self.setMaximumSize(220, 180)

    # ------------------------------------------------------

    def setScore(self, value):

        self.score = max(0, min(value, self.maximum))
        self.update()

    # ------------------------------------------------------

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()

        size = min(w, h)

        margin = 22

        rect = QRectF(
            (w-size)/2 + margin,
            18,
            size-margin*2,
            size-margin*2
        )

        # --------------------------------------------------
        # Background Arc
        # --------------------------------------------------

        pen = QPen(QColor("#1B2434"))
        pen.setWidth(14)
        pen.setCapStyle(Qt.RoundCap)

        painter.setPen(pen)

        painter.drawArc(
            rect,
            210 * 16,
            -240 * 16
        )

        # --------------------------------------------------
        # Progress Arc
        # --------------------------------------------------

        gradient = QConicalGradient(rect.center(), 210)

        gradient.setColorAt(0.00, QColor("#FF3B30"))
        gradient.setColorAt(0.50, QColor("#FF8C1A"))
        gradient.setColorAt(1.00, QColor("#FFC533"))

        progressPen = QPen()
        progressPen.setBrush(gradient)
        progressPen.setWidth(14)
        progressPen.setCapStyle(Qt.RoundCap)

        painter.setPen(progressPen)

        span = -240 * (self.score/self.maximum)

        painter.drawArc(
            rect,
            210*16,
            int(span*16)
        )

        # --------------------------------------------------
        # Score
        # --------------------------------------------------

        painter.setPen(QColor("white"))

        font = QFont("Segoe UI", 28, QFont.Bold)

        painter.setFont(font)

        painter.drawText(
            QRectF(0, 48, w, 40),
            Qt.AlignCenter,
            str(self.score)
        )

        # --------------------------------------------------
        # /100
        # --------------------------------------------------

        painter.setPen(QColor("#C7D0DD"))

        font = QFont("Segoe UI", 11)

        painter.setFont(font)

        painter.drawText(
            QRectF(0, 90, w, 25),
            Qt.AlignCenter,
            "/100"
        )

        # --------------------------------------------------
        # Status
        # --------------------------------------------------

        painter.setPen(QColor("#FF3B30"))

        font = QFont("Segoe UI", 11, QFont.Bold)

        painter.setFont(font)

        painter.drawText(
            QRectF(0, 122, w, 25),
            Qt.AlignCenter,
            "High Risk"
        )