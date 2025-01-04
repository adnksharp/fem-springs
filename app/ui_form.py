# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(517, 423)
        Widget.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(Widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.springs = QSpinBox(Widget)
        self.springs.setObjectName(u"springs")
        self.springs.setMinimum(1)
        self.springs.setMaximum(255)

        self.horizontalLayout.addWidget(self.springs)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.nodes = QSpinBox(Widget)
        self.nodes.setObjectName(u"nodes")
        self.nodes.setMinimum(2)
        self.nodes.setMaximum(255)

        self.horizontalLayout_2.addWidget(self.nodes)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.eqk = QCheckBox(self.tab)
        self.eqk.setObjectName(u"eqk")

        self.gridLayout.addWidget(self.eqk, 1, 2, 1, 1)

        self.Sk = QLineEdit(self.tab)
        self.Sk.setObjectName(u"Sk")

        self.gridLayout.addWidget(self.Sk, 1, 1, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.BCA = QCheckBox(self.tab)
        self.BCA.setObjectName(u"BCA")

        self.gridLayout.addWidget(self.BCA, 0, 2, 1, 1)

        self.BCB = QCheckBox(self.tab)
        self.BCB.setObjectName(u"BCB")

        self.gridLayout.addWidget(self.BCB, 2, 2, 1, 1)

        self.SNA = QSpinBox(self.tab)
        self.SNA.setObjectName(u"SNA")
        self.SNA.setMinimum(1)
        self.SNA.setMaximum(2)

        self.gridLayout.addWidget(self.SNA, 0, 1, 1, 1)

        self.SNB = QSpinBox(self.tab)
        self.SNB.setObjectName(u"SNB")
        self.SNB.setMinimum(1)
        self.SNB.setMaximum(2)

        self.gridLayout.addWidget(self.SNB, 2, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QSize(213, 96))
        self.label_6.setPixmap(QPixmap(u"src/spring.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_20 = QLabel(Widget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_9.addWidget(self.label_20)

        self.forces = QSpinBox(Widget)
        self.forces.setObjectName(u"forces")
        self.forces.setMinimum(1)
        self.forces.setMaximum(255)

        self.horizontalLayout_9.addWidget(self.forces)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.tabWidget_2 = QTabWidget(Widget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.force = QSpinBox(self.tab_3)
        self.force.setObjectName(u"force")
        self.force.setMinimum(0)
        self.force.setMaximum(1000000000)

        self.gridLayout_3.addWidget(self.force, 0, 1, 1, 1)

        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1)

        self.FN = QSpinBox(self.tab_3)
        self.FN.setObjectName(u"FN")
        self.FN.setMinimum(1)
        self.FN.setMaximum(2)

        self.gridLayout_3.addWidget(self.FN, 1, 1, 1, 1)

        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout_3)

        self.tabWidget_2.addTab(self.tab_3, "")

        self.verticalLayout_5.addWidget(self.tabWidget_2)

        self.copy = QPushButton(Widget)
        self.copy.setObjectName(u"copy")

        self.verticalLayout_5.addWidget(self.copy)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Resortes", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Resortes:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Nodos", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_4.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("Widget", u"Nodo A:", None))
        self.eqk.setText(QCoreApplication.translate("Widget", u"Iguales", None))
        self.Sk.setPlaceholderText(QCoreApplication.translate("Widget", u"M\u00f3dulo elastico", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"k:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Nodo B:", None))
        self.BCA.setText(QCoreApplication.translate("Widget", u"Fijo", None))
        self.BCB.setText(QCoreApplication.translate("Widget", u"Fijo", None))
        self.label_6.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Resorte 1", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"Fuerzas", None))
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_16.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_16.setText(QCoreApplication.translate("Widget", u"Fuerza:", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"Nodo de aplicaci\u00f3n:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"Fuerza 1", None))
        self.copy.setText(QCoreApplication.translate("Widget", u"Copiar", None))
    # retranslateUi

