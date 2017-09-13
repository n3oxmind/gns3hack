# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Programs/gns3/gns3-gui-2.0.3/gns3/ui/capture_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CaptureDialog(object):
    def setupUi(self, CaptureDialog):
        CaptureDialog.setObjectName("CaptureDialog")
        CaptureDialog.setWindowModality(QtCore.Qt.WindowModal)
        CaptureDialog.resize(500, 147)
        CaptureDialog.setMaximumSize(QtCore.QSize(500, 147))
        CaptureDialog.setStyleSheet("\n"
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
        CaptureDialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(CaptureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLinkTypeLabel = QtWidgets.QLabel(CaptureDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLinkTypeLabel.sizePolicy().hasHeightForWidth())
        self.uiLinkTypeLabel.setSizePolicy(sizePolicy)
        self.uiLinkTypeLabel.setScaledContents(False)
        self.uiLinkTypeLabel.setObjectName("uiLinkTypeLabel")
        self.gridLayout.addWidget(self.uiLinkTypeLabel, 0, 0, 1, 1)
        self.uiDataLinkTypeComboBox = QtWidgets.QComboBox(CaptureDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiDataLinkTypeComboBox.sizePolicy().hasHeightForWidth())
        self.uiDataLinkTypeComboBox.setSizePolicy(sizePolicy)
        self.uiDataLinkTypeComboBox.setObjectName("uiDataLinkTypeComboBox")
        self.gridLayout.addWidget(self.uiDataLinkTypeComboBox, 0, 1, 1, 1)
        self.uiFileNameLabel = QtWidgets.QLabel(CaptureDialog)
        self.uiFileNameLabel.setObjectName("uiFileNameLabel")
        self.gridLayout.addWidget(self.uiFileNameLabel, 1, 0, 1, 1)
        self.uiCaptureFileNameLineEdit = QtWidgets.QLineEdit(CaptureDialog)
        self.uiCaptureFileNameLineEdit.setObjectName("uiCaptureFileNameLineEdit")
        self.gridLayout.addWidget(self.uiCaptureFileNameLineEdit, 1, 1, 1, 1)
        self.uiStartCommandCheckBox = QtWidgets.QCheckBox(CaptureDialog)
        self.uiStartCommandCheckBox.setChecked(True)
        self.uiStartCommandCheckBox.setObjectName("uiStartCommandCheckBox")
        self.gridLayout.addWidget(self.uiStartCommandCheckBox, 2, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(CaptureDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiButtonBox.sizePolicy().hasHeightForWidth())
        self.uiButtonBox.setSizePolicy(sizePolicy)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.horizontalLayout.addWidget(self.uiButtonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 244, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)

        self.retranslateUi(CaptureDialog)
        QtCore.QMetaObject.connectSlotsByName(CaptureDialog)

    def retranslateUi(self, CaptureDialog):
        _translate = QtCore.QCoreApplication.translate
        CaptureDialog.setWindowTitle(_translate("CaptureDialog", "Packet capture"))
        self.uiLinkTypeLabel.setText(_translate("CaptureDialog", "Link type:"))
        self.uiFileNameLabel.setText(_translate("CaptureDialog", "File name:"))
        self.uiStartCommandCheckBox.setText(_translate("CaptureDialog", "Start the capture visualization program"))

from . import resources_rc
