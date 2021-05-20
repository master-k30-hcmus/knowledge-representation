# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(872, 646)
        icon = QIcon()
        icon.addFile(u"icon/lab-color.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnLab = QPushButton(self.centralwidget)
        self.btnLab.setObjectName(u"btnLab")
        self.btnLab.setGeometry(QRect(390, 320, 101, 161))
        icon1 = QIcon()
        icon1.addFile(u"icon/lab.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLab.setIcon(icon1)
        self.btnLab.setIconSize(QSize(80, 225))
        self.txtTitle = QLineEdit(self.centralwidget)
        self.txtTitle.setObjectName(u"txtTitle")
        self.txtTitle.setGeometry(QRect(210, 20, 441, 41))
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setPointSize(16)
        self.txtTitle.setFont(font)
        self.txtTitle.setCursor(QCursor(Qt.ArrowCursor))
        self.txtTitle.setMouseTracking(False)
        self.txtTitle.setAutoFillBackground(False)
        self.txtTitle.setAlignment(Qt.AlignCenter)
        self.txtTitle.setReadOnly(True)
        self.grpProduceSteps = QGroupBox(self.centralwidget)
        self.grpProduceSteps.setObjectName(u"grpProduceSteps")
        self.grpProduceSteps.setGeometry(QRect(530, 210, 321, 351))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setPointSize(12)
        self.grpProduceSteps.setFont(font1)
        self.txtProduceSteps = QPlainTextEdit(self.grpProduceSteps)
        self.txtProduceSteps.setObjectName(u"txtProduceSteps")
        self.txtProduceSteps.setGeometry(QRect(10, 30, 301, 311))
        self.txtProduceSteps.setReadOnly(True)
        self.grpEquations = QGroupBox(self.centralwidget)
        self.grpEquations.setObjectName(u"grpEquations")
        self.grpEquations.setGeometry(QRect(20, 210, 321, 351))
        self.grpEquations.setFont(font1)
        self.btnInputEquationsFromFile = QToolButton(self.grpEquations)
        self.btnInputEquationsFromFile.setObjectName(u"btnInputEquationsFromFile")
        self.btnInputEquationsFromFile.setGeometry(QRect(10, 30, 121, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.btnInputEquationsFromFile.setFont(font2)
        self.pushButton = QPushButton(self.grpEquations)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 310, 71, 31))
        self.pushButton.setFont(font2)
        self.inputEquations = QTextEdit(self.grpEquations)
        self.inputEquations.setObjectName(u"inputEquations")
        self.inputEquations.setGeometry(QRect(10, 70, 301, 231))
        self.grpProblem = QGroupBox(self.centralwidget)
        self.grpProblem.setObjectName(u"grpProblem")
        self.grpProblem.setGeometry(QRect(180, 90, 501, 91))
        self.grpProblem.setFont(font1)
        self.inputSourceChemistry = QLineEdit(self.grpProblem)
        self.inputSourceChemistry.setObjectName(u"inputSourceChemistry")
        self.inputSourceChemistry.setGeometry(QRect(10, 30, 211, 51))
        self.inputTargetChemistry = QLineEdit(self.grpProblem)
        self.inputTargetChemistry.setObjectName(u"inputTargetChemistry")
        self.inputTargetChemistry.setGeometry(QRect(280, 30, 211, 51))
        self.inputTargetChemistry.setClearButtonEnabled(False)
        self.btnTo = QPushButton(self.grpProblem)
        self.btnTo.setObjectName(u"btnTo")
        self.btnTo.setEnabled(False)
        self.btnTo.setGeometry(QRect(230, 40, 41, 31))
        icon2 = QIcon()
        icon2.addFile(u"icon/right-arrows.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnTo.setIcon(icon2)
        self.btnTo.setIconSize(QSize(26, 16))
        self.btnTo.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.grpProblem.raise_()
        self.grpEquations.raise_()
        self.grpProduceSteps.raise_()
        self.btnLab.raise_()
        self.txtTitle.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 872, 26))
        self.menuAuthors = QMenu(self.menubar)
        self.menuAuthors.setObjectName(u"menuAuthors")
        self.menuRefresh = QMenu(self.menubar)
        self.menuRefresh.setObjectName(u"menuRefresh")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuRefresh.menuAction())
        self.menubar.addAction(self.menuAuthors.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ChemistryLab-Nhom07", None))
        # if QT_CONFIG(tooltip)
        self.btnLab.setToolTip(QCoreApplication.translate("MainWindow", u"Laboratory", None))
        # endif // QT_CONFIG(tooltip)
        self.btnLab.setText("")
        self.txtTitle.setText(
            QCoreApplication.translate("MainWindow", u"\u0110I\u1ec0U CH\u1ebe CH\u1ea4T H\u00d3A H\u1eccC", None))
        self.grpProduceSteps.setTitle(
            QCoreApplication.translate("MainWindow", u"C\u00e1c b\u01b0\u1edbc th\u1ef1c hi\u1ec7n", None))
        self.grpEquations.setTitle(
            QCoreApplication.translate("MainWindow", u"Ph\u01b0\u01a1ng tr\u00ecnh h\u00f3a h\u1ecdc", None))
        # if QT_CONFIG(tooltip)
        self.btnInputEquationsFromFile.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.btnInputEquationsFromFile.setText(
            QCoreApplication.translate("MainWindow", u"Ch\u1ecdn t\u1eeb file", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.grpProblem.setTitle(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec1u ch\u1ebf", None))
        self.btnTo.setText("")
        self.menuAuthors.setTitle(QCoreApplication.translate("MainWindow", u"Nh\u00f3m 07", None))
        self.menuRefresh.setTitle(QCoreApplication.translate("MainWindow", u"Th\u00ed nghi\u1ec7m m\u1edbi", None))
    # retranslateUi
