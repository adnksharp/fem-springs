from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap

class newItems(QWidget):
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
        
    def addForces(self, n):
        new = QWidget()
        grid = QGridLayout()
        newLayout = QHBoxLayout(new)
        newforce = QSpinBox(new)
        newFN = QSpinBox(new)
        
        newforce.setMinimum(0)
        newFN.setMinimum(-1000000000)
        newforce.setMaximum(1000000000)
        newFN.setMaximum(self.ui.nodes.value())
        
        grid.addWidget(QLabel('Fuerza:'), 0, 0, 1, 1)
        grid.addWidget(QLabel('Nodo de aplicación:'), 1, 0, 1, 1)
        grid.addWidget(newforce, 0, 1, 1, 1)
        grid.addWidget(newFN, 1, 1, 1, 1)
        
        newLayout.addLayout(grid)
        
        self.ui.tabWidget_2.addTab(new, f"Fuerza {n}")
        
        self.forces.append(newforce)
        self.nff.append(newFN)