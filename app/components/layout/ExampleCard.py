from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame

from qfluentwidgets import StrongBodyLabel


class ExampleCard(QWidget):
    """Example card"""

    def __init__(self, title, widget: QWidget, sourcePath, stretch=0, parent=None):
        super().__init__(parent=parent)
        self.widget = widget
        self.stretch = stretch
        self.titleLabel = StrongBodyLabel(title, self)
        self.card = QFrame(self)
        self.sourceWidget = QFrame(self.card)
        self.vBoxLayout = QVBoxLayout(self)
        self.cardLayout = QVBoxLayout(self.card)
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QVBoxLayout(self.sourceWidget)

        self.__initWidget()

    def __initWidget(self):
        self.__initLayout()
        self.card.setObjectName("card")
        self.sourceWidget.setObjectName("sourceWidget")

    def __initLayout(self):
        self.vBoxLayout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinimumSize)
        self.cardLayout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinimumSize)
        self.topLayout.setSizeConstraint(QHBoxLayout.SizeConstraint.SetMinimumSize)

        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.setContentsMargins(12, 12, 12, 12)
        self.bottomLayout.setContentsMargins(0, 0, 0, 0)
        self.cardLayout.setContentsMargins(0, 0, 0, 0)

        # self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignTop)
        self.vBoxLayout.addWidget(self.card, 0, Qt.AlignmentFlag.AlignTop)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.cardLayout.setSpacing(0)
        self.cardLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.cardLayout.addLayout(self.topLayout, 0)
        self.cardLayout.addWidget(self.sourceWidget, 0, Qt.AlignmentFlag.AlignBottom)

        self.titleLabel.setParent(self.card)
        self.widget.setParent(self.card)
        self.topLayout.addWidget(self.titleLabel)
        if self.stretch == 0:
            self.topLayout.addStretch(1)

        self.widget.show()
        self.bottomLayout.addWidget(self.widget)
