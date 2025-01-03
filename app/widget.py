# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)
from PySide6.QtCore import QSize, Qt
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

        self.sna = [self.ui.SNA]
        self.snb = [self.ui.SNB]
        self.bcuia = [self.ui.BCA]
        self.bcuib = [self.ui.BCB]
        self.kui = [self.ui.eqk]
        self.kedit = [self.ui.Sk]
        self.bc = [False, False]

        self.ui.springs.valueChanged.connect(self.newSprings)
        self.ui.nodes.valueChanged.connect(self.newNodes)
        self.ui.SNA.valueChanged.connect(lambda x:self.settingNodes(False, 1))
        self.ui.SNB.valueChanged.connect(lambda x:self.settingNodes(True, 1))
        self.ui.BCA.stateChanged.connect(lambda x:self.settingBC(False, 1))
        self.ui.BCB.stateChanged.connect(lambda x:self.settingBC(True, 1))
        self.ui.eqk.stateChanged.connect(lambda x:self.settingK(1))
 
    def addSprings(self, n):
        new = QWidget()
        grid = QGridLayout()
        newSNA = QSpinBox(new)
        newSNB = QSpinBox(new)
        newBCA = QCheckBox(new)
        newBCB = QCheckBox(new)
        neweqk = QCheckBox(new)
        newLayout = QHBoxLayout(new)
        newImg = QLabel(new)
        newkedit = QLineEdit(new)
        
        newSNA.setMinimum(1)
        newSNB.setMinimum(1)
        newSNA.setMaximum(self.ui.nodes.value())
        newSNB.setMaximum(self.ui.nodes.value())
        
        newBCA.setText('Fijo')
        newBCB.setText('Fijo')
        neweqk.setText('Iguales')
        newBCA.setCheckState(Qt.CheckState.Checked if self.bc[0] else Qt.CheckState.Unchecked)
        newBCB.setCheckState(Qt.CheckState.Checked if self.bc[0] else Qt.CheckState.Unchecked)
        neweqk.setCheckState(Qt.CheckState.Checked if self.kui[0].isChecked() else Qt.CheckState.Unchecked)
        
        if self.kui[0].isChecked():
            newkedit.setEnabled(False)
            newkedit.setText(self.ui.Sk.text())
        
        
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
        grid.addWidget(newkedit, 1, 1, 1, 1)
        grid.addWidget(newSNB, 2, 1, 1, 1)
        grid.addWidget(newBCA, 0, 2, 1, 1)
        grid.addWidget(neweqk, 1, 2, 1, 1)
        grid.addWidget(newBCB, 2, 2, 1, 1)
        
        newLayout.addLayout(grid)
        newLayout.addWidget(newImg)
        
        self.ui.tabWidget.addTab(new, f"Resorte {n}")
        
        newSNA.valueChanged.connect(lambda x:self.settingNodes(False, n))
        newSNB.valueChanged.connect(lambda x:self.settingNodes(True, n))
        newBCA.stateChanged.connect(lambda x:self.settingBC(False, n))
        newBCB.stateChanged.connect(lambda x:self.settingBC(True, n))
        neweqk.stateChanged.connect(lambda x:self.settingK(n))
        
        self.sna.append(newSNA)
        self.snb.append(newSNB)
        self.bcuia.append(newBCA)
        self.bcuib.append(newBCB)
        self.kui.append(neweqk)
        self.kedit.append(newkedit)

    def settingNodes(self, *args):
        if not args[0]:
            self.bcuia[args[1] - 1].setCheckState(Qt.CheckState.Checked if self.bc[self.sna[args[1] - 1].value() - 1] else Qt.CheckState.Unchecked)
        else:
            self.bcuib[args[1] - 1].setCheckState(Qt.CheckState.Checked if self.bc[self.snb[args[1] - 1].value() - 1] else Qt.CheckState.Unchecked)
            
    def settingBC(self, *args):
        if not args[0]:
            self.bc[self.sna[args[1] - 1].value() - 1] = self.bcuia[args[1] - 1].isChecked()
        else:
            self.bc[self.snb[args[1] - 1].value() - 1] = self.bcuib[args[1] - 1].isChecked()
        for i in range(len(self.bcuia)):
            self.bcuia[i].setCheckState(Qt.CheckState.Checked if self.bc[self.sna[i].value() - 1] else Qt.CheckState.Unchecked)
            self.bcuib[i].setCheckState(Qt.CheckState.Checked if self.bc[self.snb[i].value() - 1] else Qt.CheckState.Unchecked)
            
    def settingK(self, arg):
        father, val = self.kui[arg - 1].isChecked(), self.kedit[arg - 1].text()
        for kui in self.kui:
            kui.setCheckState(Qt.CheckState.Checked if father else Qt.CheckState.Unchecked)
        for edit in self.kedit:
            edit.setText(val if father else edit.text())
            edit.setEnabled(not father)
        self.ui.Sk.setEnabled(True)
            
    def deleteSprings(self):
        self.ui.tabWidget.removeTab(self.ui.tabWidget.count() - 1)
        self.sna = self.sna[:-1]
        self.snb = self.snb[:-1]
        self.bcuia = self.bcuia[:-1]
        self.bcuib = self.bcuib[:-1]
        self.kui = self.kui[:-1]
        self.kedit = self.kedit[:-1]

    def newSprings(self):
        opts = self.ui.springs.value()
        while self.ui.springs.value() > self.ui.tabWidget.count():
            now = self.ui.tabWidget.count()
            self.addSprings(now + 1)
        while self.ui.springs.value() < self.ui.tabWidget.count():
            self.deleteSprings()
 
    def newNodes(self):
        opts = self.ui.nodes.value()
        if opts > 1:
            for i in self.sna:
                i.setMaximum(opts)
            for i in self.snb:
                i.setMaximum(opts)
            self.ui.FN.setMaximum(opts)
        while len(self.bc) < opts:
            self.bc.append(False)
        while len(self.bc) > opts:
            self.bc = self.bc[:-1]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
