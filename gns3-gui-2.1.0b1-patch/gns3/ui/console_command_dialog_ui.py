# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.0.3/gns3/ui/console_command_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_uiConsoleCommandDialog(object):
    def setupUi(self, uiConsoleCommandDialog):
        uiConsoleCommandDialog.setObjectName("uiConsoleCommandDialog")
        uiConsoleCommandDialog.resize(544, 405)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(uiConsoleCommandDialog.sizePolicy().hasHeightForWidth())
        uiConsoleCommandDialog.setSizePolicy(sizePolicy)
        uiConsoleCommandDialog.setMinimumSize(QtCore.QSize(0, 0))
        uiConsoleCommandDialog.setStyleSheet("QWidget {\n"
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
        uiConsoleCommandDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(uiConsoleCommandDialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(uiConsoleCommandDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiCommandComboBox = QtWidgets.QComboBox(uiConsoleCommandDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiCommandComboBox.sizePolicy().hasHeightForWidth())
        self.uiCommandComboBox.setSizePolicy(sizePolicy)
        self.uiCommandComboBox.setObjectName("uiCommandComboBox")
        self.horizontalLayout.addWidget(self.uiCommandComboBox)
        self.uiRemovePushButton = QtWidgets.QPushButton(uiConsoleCommandDialog)
        self.uiRemovePushButton.setObjectName("uiRemovePushButton")
        self.horizontalLayout.addWidget(self.uiRemovePushButton)
        self.uiSavePushButton = QtWidgets.QPushButton(uiConsoleCommandDialog)
        self.uiSavePushButton.setObjectName("uiSavePushButton")
        self.horizontalLayout.addWidget(self.uiSavePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(uiConsoleCommandDialog)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.uiCommandPlainTextEdit = QtWidgets.QPlainTextEdit(uiConsoleCommandDialog)
        self.uiCommandPlainTextEdit.setMinimumSize(QtCore.QSize(500, 0))
        self.uiCommandPlainTextEdit.setObjectName("uiCommandPlainTextEdit")
        self.verticalLayout.addWidget(self.uiCommandPlainTextEdit)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(uiConsoleCommandDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.verticalLayout.addWidget(self.uiButtonBox)

        self.retranslateUi(uiConsoleCommandDialog)
        self.uiButtonBox.accepted.connect(uiConsoleCommandDialog.accept)
        self.uiButtonBox.rejected.connect(uiConsoleCommandDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(uiConsoleCommandDialog)

    def retranslateUi(self, uiConsoleCommandDialog):
        _translate = QtCore.QCoreApplication.translate
        uiConsoleCommandDialog.setWindowTitle(_translate("uiConsoleCommandDialog", "Command"))
        self.label_2.setText(_translate("uiConsoleCommandDialog", "Choose a predefined command:"))
        self.uiRemovePushButton.setText(_translate("uiConsoleCommandDialog", "Remove"))
        self.uiSavePushButton.setText(_translate("uiConsoleCommandDialog", "Save"))
        self.label.setText(_translate("uiConsoleCommandDialog", "<html><head/><body><p>Or customize the command in the next input field. <br/>The following variables are replaced by GNS3: </p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%h: console IP or hostname</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%p: console port</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%P: VNC display</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s: path of the serial connection</li></ul><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%d: title of the console</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%i: Project UUID</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%c: GNS3 server connection string (<span style=\" font-style:italic;\">http://user:password@server:port</span>)</li></ul></body></html>"))

