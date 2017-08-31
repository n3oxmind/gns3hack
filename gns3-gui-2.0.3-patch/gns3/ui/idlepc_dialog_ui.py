# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.0.3/gns3/ui/idlepc_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IdlePCDialog(object):
    def setupUi(self, IdlePCDialog):
        IdlePCDialog.setObjectName("IdlePCDialog")
        IdlePCDialog.resize(382, 116)
        IdlePCDialog.setStyleSheet("QWidget {\n"
"    background-color: #323232;\n"
"    color: #BAF73C;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border:0px;\n"
"}\n"
"\n"
"QGraphicsView, QTextEdit, QPlainTextEdit, QTreeWidget, QListWidget, QLineEdit, QSpinBox, QComboBox {\n"
"    background-color: #282828;\n"
"}\n"
"\n"
"QLabel, QMenu, QStatusBar {\n"
"  color: #BAF73C;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #f2f2f2;\n"
"    background-color: #383838;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #383838;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #BAF73C;\n"
"    font: bold 12px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"\n"
"QAbstractScrollArea::corner {\n"
"    background: #323232;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"    selection-color: #f2f2f2;\n"
"    selection-background-color: #323232;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #282828;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar, QPushButton, QToolButton, QTabWidget, QHeaderView::section {\n"
"    color: #BAF73C;\n"
"    font: bold 11px;\n"
"}\n"
"\n"
"QTabBar {\n"
"    color: #BAF73C;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #BAF73C;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"# bg-color=#282828\n"
"# fg-color=#BAF73C\n"
"# tool-bar=#323232\n"
"# selection-bg=#383838 \n"
"# selection-fg=#f2f2f2 ")
        IdlePCDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(IdlePCDialog)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLabel = QtWidgets.QLabel(IdlePCDialog)
        self.uiLabel.setObjectName("uiLabel")
        self.gridLayout.addWidget(self.uiLabel, 0, 0, 1, 1)
        self.uiComboBox = QtWidgets.QComboBox(IdlePCDialog)
        self.uiComboBox.setObjectName("uiComboBox")
        self.gridLayout.addWidget(self.uiComboBox, 1, 0, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(IdlePCDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridLayout.addWidget(self.uiButtonBox, 2, 0, 1, 1)

        self.retranslateUi(IdlePCDialog)
        self.uiButtonBox.accepted.connect(IdlePCDialog.accept)
        self.uiButtonBox.rejected.connect(IdlePCDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(IdlePCDialog)

    def retranslateUi(self, IdlePCDialog):
        _translate = QtCore.QCoreApplication.translate
        IdlePCDialog.setWindowTitle(_translate("IdlePCDialog", "Idle-PC values"))
        self.uiLabel.setText(_translate("IdlePCDialog", "Potentially better Idle-PC values are marked with \'*\'"))

