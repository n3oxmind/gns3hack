# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.0.3/gns3/ui/snapshots_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SnapshotsDialog(object):
    def setupUi(self, SnapshotsDialog):
        SnapshotsDialog.setObjectName("SnapshotsDialog")
        SnapshotsDialog.setWindowModality(QtCore.Qt.WindowModal)
        SnapshotsDialog.resize(496, 288)
        SnapshotsDialog.setStyleSheet("QWidget {\n"
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
        self.gridLayout = QtWidgets.QGridLayout(SnapshotsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.uiSnapshotsList = QtWidgets.QListWidget(SnapshotsDialog)
        self.uiSnapshotsList.setObjectName("uiSnapshotsList")
        self.gridLayout.addWidget(self.uiSnapshotsList, 0, 0, 1, 4)
        self.uiCreatePushButton = QtWidgets.QPushButton(SnapshotsDialog)
        self.uiCreatePushButton.setObjectName("uiCreatePushButton")
        self.gridLayout.addWidget(self.uiCreatePushButton, 1, 0, 1, 1)
        self.uiRestorePushButton = QtWidgets.QPushButton(SnapshotsDialog)
        self.uiRestorePushButton.setEnabled(False)
        self.uiRestorePushButton.setObjectName("uiRestorePushButton")
        self.gridLayout.addWidget(self.uiRestorePushButton, 1, 2, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(SnapshotsDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridLayout.addWidget(self.uiButtonBox, 1, 3, 1, 1)
        self.uiDeletePushButton = QtWidgets.QPushButton(SnapshotsDialog)
        self.uiDeletePushButton.setEnabled(False)
        self.uiDeletePushButton.setObjectName("uiDeletePushButton")
        self.gridLayout.addWidget(self.uiDeletePushButton, 1, 1, 1, 1)

        self.retranslateUi(SnapshotsDialog)
        self.uiButtonBox.accepted.connect(SnapshotsDialog.accept)
        self.uiButtonBox.rejected.connect(SnapshotsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SnapshotsDialog)

    def retranslateUi(self, SnapshotsDialog):
        _translate = QtCore.QCoreApplication.translate
        SnapshotsDialog.setWindowTitle(_translate("SnapshotsDialog", "Snapshots"))
        self.uiCreatePushButton.setText(_translate("SnapshotsDialog", "&Create"))
        self.uiRestorePushButton.setText(_translate("SnapshotsDialog", "&Restore"))
        self.uiDeletePushButton.setText(_translate("SnapshotsDialog", "&Delete"))

