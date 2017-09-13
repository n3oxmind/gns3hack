# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Programs/gns3/gns3-gui-2.0.3/gns3/ui/exec_command_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExecCommandDialog(object):
    def setupUi(self, ExecCommandDialog):
        ExecCommandDialog.setObjectName("ExecCommandDialog")
        ExecCommandDialog.resize(651, 343)
        ExecCommandDialog.setStyleSheet("\n"
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
        ExecCommandDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(ExecCommandDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.uiOutputTextEdit = QtWidgets.QPlainTextEdit(ExecCommandDialog)
        self.uiOutputTextEdit.setObjectName("uiOutputTextEdit")
        self.gridLayout.addWidget(self.uiOutputTextEdit, 0, 0, 1, 2)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(ExecCommandDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridLayout.addWidget(self.uiButtonBox, 1, 1, 1, 1)

        self.retranslateUi(ExecCommandDialog)
        self.uiButtonBox.accepted.connect(ExecCommandDialog.accept)
        self.uiButtonBox.rejected.connect(ExecCommandDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExecCommandDialog)

    def retranslateUi(self, ExecCommandDialog):
        _translate = QtCore.QCoreApplication.translate
        ExecCommandDialog.setWindowTitle(_translate("ExecCommandDialog", "Command execution"))

from . import resources_rc
