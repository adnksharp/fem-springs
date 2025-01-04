# This Python file uses the following encoding: utf-8
import sys
from notifypy import Notify as noty
import pyperclip as xclip

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from form_injection import newItems
import fem

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.noty = noty()

        self.sna = [self.ui.SNA]
        self.snb = [self.ui.SNB]
        self.bcuia = [self.ui.BCA]
        self.bcuib = [self.ui.BCB]
        self.kui = [self.ui.eqk]
        self.kedit = [self.ui.Sk]
        self.bc = [False, False]
        self.forces = [self.ui.force]
        self.nff = [self.ui.FN]

        self.ui.run.clicked.connect(self.toCalc)
        self.ui.copy.clicked.connect(self.copyConf)
        self.ui.springs.valueChanged.connect(self.newSprings)
        self.ui.nodes.valueChanged.connect(self.newNodes)
        self.ui.forces.valueChanged.connect(self.newForces)
        self.ui.SNA.valueChanged.connect(lambda x:self.settingNodes(False, 1))
        self.ui.SNB.valueChanged.connect(lambda x:self.settingNodes(True, 1))
        self.ui.BCA.stateChanged.connect(lambda x:self.settingBC(False, 1))
        self.ui.BCB.stateChanged.connect(lambda x:self.settingBC(True, 1))
        self.ui.eqk.stateChanged.connect(lambda x:self.settingK(1))
 
    def toCalc(self):
        elements = self.ui.springs.value()
        n = self.ui.nodes.value()
        nodes = []
        for i in range(len(self.sna)):
            nodes.append([
              self.sna[i].value() - 1,
              self.snb[i].value() - 1
            ])
        forces = [x.value() for x in self.forces]
        findex = [x.value() for x in self.nff]
        k = []
        for i in self.kedit:
            try:
                k.append(int(i.text()))
            except:
                k.append(0)
        bc = []
        for i in range(len(self.bc)):
            if self.bc[i]:
                bc.append(i)
        fem.calculate(elements, n, nodes, forces, findex, k, bc)

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
        
    def deleteForces(self):
        self.ui.tabWidget_2.removeTab(self.ui.tabWidget_2.count() - 1)
        self.forces = self.forces[:-1]
        self.nff = self.nff[:-1]

    def newSprings(self):
        while self.ui.springs.value() > self.ui.tabWidget.count():
            now = self.ui.tabWidget.count()
            newItems.addSprings(self, now + 1)
        while self.ui.springs.value() < self.ui.tabWidget.count():
            self.deleteSprings()
            
    def newForces(self):
        while self.ui.forces.value() > self.ui.tabWidget_2.count():
            now = self.ui.tabWidget_2.count()
            newItems.addForces(self, now +  1)
        while self.ui.forces.value() < self.ui.tabWidget_2.count():
            self.deleteForces()
 
    def newNodes(self):
        opts = self.ui.nodes.value()
        if opts > 1:
            for i in self.sna:
                i.setMaximum(opts)
            for i in self.snb:
                i.setMaximum(opts)
            for i in self.nff:
                i.setMaximum(opts)
        while len(self.bc) < opts:
            self.bc.append(False)
        while len(self.bc) > opts:
            self.bc = self.bc[:-1]
            
    def copyConf(self):
        self.noty.title = 'FEM Springs'
        self.noty.message = 'Variables copiadas al portapapeles'
        
        clone = '"springs":\n{'
        clone += f'\t"count": {self.ui.springs.value()},\n'
        for i in range(self.ui.springs.value()):
            clone += "\t{\n"
            clone += f'\t\t"nodes": [{self.sna[i].value()}, {self.snb[i].value()}],\n\t\t"k": {int(self.kedit[i].text())}\n'
            if i < self.ui.springs.value() - 1:
                clone += "\t},\n"
            else:
                clone += "\t}\n"
        clone += '}\n"forces":\n{\n'
        
        clone += f'\t"count": {self.ui.forces.value()},\n'
        for i in range(self.ui.forces.value()):
            clone += "\t{\n"
            clone += f'\t\t"node": {self.nff[i].value()},\n\t\t"k": {self.forces[i].text()}\n'
            if i < self.ui.forces.value() - 1:
                clone += "\t},\n"
            else:
                clone += "\t}\n}"

        xclip.copy(clone)
        self.noty.send()              

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
