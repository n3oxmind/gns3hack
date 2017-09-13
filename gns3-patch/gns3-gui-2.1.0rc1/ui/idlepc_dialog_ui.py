# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Programs/gns3/gns3-gui-2.1.0b2/gns3/ui/idlepc_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IdlePCDialog(object):
    def setupUi(self, IdlePCDialog):
        IdlePCDialog.setObjectName("IdlePCDialog")
        IdlePCDialog.resize(382, 116)
        IdlePCDialog.setStyleSheet("\n"
"QWidget {\n"
"    background-color: #fae8b7;\n"
"    color: #586e75;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border:0px;\n"
"}\n"
"\n"
"QGraphicsView, QTextEdit, QPlainTextEdit, QTreeWidget, QListWidget, QLineEdit, QSpinBox, QComboBox {\n"
"    background-color: #fdf6e3;\n"
"}\n"
"\n"
"QLabel, QMenu, QStatusBar {\n"
"  color: #586e75;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: #fae8b7;\n"
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
"    color: #586e75;\n"
"    font: bold 12px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"\n"
"QAbstractScrollArea::corner {\n"
"    background: #fae8b7;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"    selection-color: #f2f2f2;\n"
"    selection-background-color: #fae8b7;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #fdf6e3;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar, QPushButton, QToolButton, QTabWidget, QHeaderView::section {\n"
"    color: #586e75;\n"
"    font: bold 11px;\n"
"}\n"
"\n"
"QTabBar {\n"
"    color: #586e75;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #586e75;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"// bg-color=#fdf6e3\n"
"// fg-color=#586e75\n"
"// tool-bar=#fae8b7\n"
"// selection-bg=#383838 \n"
"// selection-fg=#f2f2f2\n"
" ")
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

