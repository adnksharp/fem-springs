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
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(517, 236)
        Widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBox = QSpinBox(Widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(255)

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox_2 = QSpinBox(Widget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimum(2)
        self.spinBox_2.setMaximum(255)

        self.horizontalLayout_2.addWidget(self.spinBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

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

        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.tab)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 0, 2, 1, 1)

        self.checkBox_3 = QCheckBox(self.tab)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 2, 2, 1, 1)

        self.spinBox_3 = QSpinBox(self.tab)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimum(1)

        self.gridLayout.addWidget(self.spinBox_3, 0, 1, 1, 1)

        self.spinBox_4 = QSpinBox(self.tab)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimum(1)

        self.gridLayout.addWidget(self.spinBox_4, 2, 1, 1, 1)


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

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


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
        self.label_4.setText(QCoreApplication.translate("Widget", u"Nodo B:", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"Iguales", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"k:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Nodo A:", None))
        self.checkBox_2.setText(QCoreApplication.translate("Widget", u"Fijo", None))
        self.checkBox_3.setText(QCoreApplication.translate("Widget", u"Fijo", None))
        self.label_6.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Resorte 1", None))
    # retranslateUi

