# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.springs.valueChanged.connect(self.newSprings)
        self.ui.nodes.valueChanged.connect(self.newNodes)
 
    def addSprings(self):
        new = QWidget()
        grid = QGridLayout()
        newSNA = QSpinBox(new)
        newSNB = QSpinBox(new)
        newBCA = QCheckBox(new)
        newBCB = QCheckBox(new)
        neweqk = QCheckBox(new)
        newLayout = QHBoxLayout(new)
        newImg = QLabel(new)
        
        newSNA.setMinimum(1)
        newSNB.setMinimum(1)
        newSNA.setMaximum(self.ui.nodes.value())
        newSNB.setMaximum(self.ui.nodes.value())
        
        newBCA.setText('Fijo')
        newBCB.setText('Fijo')
        neweqk.setText('Iguales')
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newImg.sizePolicy().hasHeightForWidth())
        newImg.setSizePolicy(sizePolicy)
        newImg.setMaximumSize(QSize(213, 96))
        newImg.setPixmap(QPixmap(u"src/spring.png"))
        newImg.setScaledContents(True)
        
        grid.addWidget(QLabel('Nodo A:'), 0, 0, 1, 1)
        grid.addWidget(QLabel('k:'), 1, 0, 1, 1)
        grid.addWidget(QLabel('Nodo B:'), 2, 0, 1, 1)
        grid.addWidget(newSNA, 0, 1, 1, 1)
        grid.addWidget(QLineEdit(), 1, 1, 1, 1)
        grid.addWidget(newSNB, 2, 1, 1, 1)
        grid.addWidget(newBCA, 0, 2, 1, 1)
        grid.addWidget(neweqk, 1, 2, 1, 1)
        grid.addWidget(newBCB, 2, 2, 1, 1)
        
        newLayout.addLayout(grid)
        newLayout.addWidget(newImg)
        
        self.ui.tabWidget.addTab(new, f"Resorte {self.ui.tabWidget.count() + 1}")
    
    def deleteSprings(self):
        self.ui.tabWidget.removeTab(self.ui.tabWidget.count() - 1)
        print('delete spring')

    def newSprings(self):
        opts = self.ui.springs.value()
        now = self.ui.tabWidget.count()
        while self.ui.springs.value() > self.ui.tabWidget.count():
            self.addSprings()
        while self.ui.springs.value() < self.ui.tabWidget.count():
            self.deleteSprings()
 
    def newNodes(self):
        opts = self.ui.nodes.value()
        if opts > 1:
            self.ui.SNA.setMaximum(opts)
            self.ui.SNB.setMaximum(opts)
            self.ui.FN.setMaximum(opts)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
