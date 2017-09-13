# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Programs/gns3/gns3-gui-2.1.0b2/gns3/ui/edit_compute_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditComputeDialog(object):
    def setupUi(self, EditComputeDialog):
        EditComputeDialog.setObjectName("EditComputeDialog")
        EditComputeDialog.setWindowModality(QtCore.Qt.WindowModal)
        EditComputeDialog.resize(579, 422)
        EditComputeDialog.setStyleSheet("\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(EditComputeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(EditComputeDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiServerPortSpinBox = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServerPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiServerPortSpinBox.setSizePolicy(sizePolicy)
        self.uiServerPortSpinBox.setSuffix(" TCP")
        self.uiServerPortSpinBox.setMaximum(65535)
        self.uiServerPortSpinBox.setProperty("value", 3080)
        self.uiServerPortSpinBox.setObjectName("uiServerPortSpinBox")
        self.gridLayout.addWidget(self.uiServerPortSpinBox, 3, 1, 1, 2)
        self.uiServerProtocolLabel = QtWidgets.QLabel(self.groupBox)
        self.uiServerProtocolLabel.setObjectName("uiServerProtocolLabel")
        self.gridLayout.addWidget(self.uiServerProtocolLabel, 1, 0, 1, 1)
        self.uiServerProtocolComboBox = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiServerProtocolComboBox.sizePolicy().hasHeightForWidth())
        self.uiServerProtocolComboBox.setSizePolicy(sizePolicy)
        self.uiServerProtocolComboBox.setObjectName("uiServerProtocolComboBox")
        self.uiServerProtocolComboBox.addItem("")
        self.uiServerProtocolComboBox.addItem("")
        self.gridLayout.addWidget(self.uiServerProtocolComboBox, 1, 1, 1, 2)
        self.uiServerHostLabel = QtWidgets.QLabel(self.groupBox)
        self.uiServerHostLabel.setObjectName("uiServerHostLabel")
        self.gridLayout.addWidget(self.uiServerHostLabel, 2, 0, 1, 1)
        self.uiServerHostLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiServerHostLineEdit.setObjectName("uiServerHostLineEdit")
        self.gridLayout.addWidget(self.uiServerHostLineEdit, 2, 1, 1, 2)
        self.uiServerPortLabel = QtWidgets.QLabel(self.groupBox)
        self.uiServerPortLabel.setObjectName("uiServerPortLabel")
        self.gridLayout.addWidget(self.uiServerPortLabel, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.uiServerNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiServerNameLineEdit.setObjectName("uiServerNameLineEdit")
        self.gridLayout.addWidget(self.uiServerNameLineEdit, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.uiEnableAuthenticationCheckBox = QtWidgets.QGroupBox(EditComputeDialog)
        self.uiEnableAuthenticationCheckBox.setCheckable(True)
        self.uiEnableAuthenticationCheckBox.setObjectName("uiEnableAuthenticationCheckBox")
        self.formLayout = QtWidgets.QFormLayout(self.uiEnableAuthenticationCheckBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.uiServerUserLabel = QtWidgets.QLabel(self.uiEnableAuthenticationCheckBox)
        self.uiServerUserLabel.setObjectName("uiServerUserLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiServerUserLabel)
        self.uiServerUserLineEdit = QtWidgets.QLineEdit(self.uiEnableAuthenticationCheckBox)
        self.uiServerUserLineEdit.setEnabled(True)
        self.uiServerUserLineEdit.setToolTip("")
        self.uiServerUserLineEdit.setObjectName("uiServerUserLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiServerUserLineEdit)
        self.uiServerPasswordLabel = QtWidgets.QLabel(self.uiEnableAuthenticationCheckBox)
        self.uiServerPasswordLabel.setObjectName("uiServerPasswordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uiServerPasswordLabel)
        self.uiServerPasswordLineEdit = QtWidgets.QLineEdit(self.uiEnableAuthenticationCheckBox)
        self.uiServerPasswordLineEdit.setEnabled(True)
        self.uiServerPasswordLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.uiServerPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiServerPasswordLineEdit.setObjectName("uiServerPasswordLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uiServerPasswordLineEdit)
        self.verticalLayout.addWidget(self.uiEnableAuthenticationCheckBox)
        self.uiWarningLabel = QtWidgets.QLabel(EditComputeDialog)
        self.uiWarningLabel.setWordWrap(True)
        self.uiWarningLabel.setObjectName("uiWarningLabel")
        self.verticalLayout.addWidget(self.uiWarningLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditComputeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditComputeDialog)
        self.buttonBox.accepted.connect(EditComputeDialog.accept)
        self.buttonBox.rejected.connect(EditComputeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditComputeDialog)
        EditComputeDialog.setTabOrder(self.uiServerNameLineEdit, self.uiServerProtocolComboBox)
        EditComputeDialog.setTabOrder(self.uiServerProtocolComboBox, self.uiServerHostLineEdit)
        EditComputeDialog.setTabOrder(self.uiServerHostLineEdit, self.uiServerPortSpinBox)
        EditComputeDialog.setTabOrder(self.uiServerPortSpinBox, self.uiEnableAuthenticationCheckBox)
        EditComputeDialog.setTabOrder(self.uiEnableAuthenticationCheckBox, self.uiServerUserLineEdit)
        EditComputeDialog.setTabOrder(self.uiServerUserLineEdit, self.uiServerPasswordLineEdit)

    def retranslateUi(self, EditComputeDialog):
        _translate = QtCore.QCoreApplication.translate
        EditComputeDialog.setWindowTitle(_translate("EditComputeDialog", "Edit server settings"))
        self.groupBox.setTitle(_translate("EditComputeDialog", "Server settings"))
        self.uiServerProtocolLabel.setText(_translate("EditComputeDialog", "Protocol:"))
        self.uiServerProtocolComboBox.setCurrentText(_translate("EditComputeDialog", "HTTP"))
        self.uiServerProtocolComboBox.setItemText(0, _translate("EditComputeDialog", "HTTP"))
        self.uiServerProtocolComboBox.setItemText(1, _translate("EditComputeDialog", "HTTPS"))
        self.uiServerHostLabel.setText(_translate("EditComputeDialog", "Host:"))
        self.uiServerHostLineEdit.setText(_translate("EditComputeDialog", "192.168.56.101"))
        self.uiServerPortLabel.setText(_translate("EditComputeDialog", "Port:"))
        self.label.setText(_translate("EditComputeDialog", "Name:"))
        self.uiEnableAuthenticationCheckBox.setTitle(_translate("EditComputeDialog", "Enable authentication"))
        self.uiServerUserLabel.setText(_translate("EditComputeDialog", "User:"))
        self.uiServerPasswordLabel.setText(_translate("EditComputeDialog", "Password:"))
        self.uiWarningLabel.setText(_translate("EditComputeDialog", "<html><head/><body><p><span style=\" font-weight:600;\">WARNING</span>: Changing a server with authentication enabled will reset the password.</p></body></html>"))

