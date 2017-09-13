# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Programs/gns3/gns3-gui-2.0.3/gns3/ui/doctor_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DoctorDialog(object):
    def setupUi(self, DoctorDialog):
        DoctorDialog.setObjectName("DoctorDialog")
        DoctorDialog.setWindowModality(QtCore.Qt.WindowModal)
        DoctorDialog.resize(607, 390)
        DoctorDialog.setStyleSheet("\n"
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
        DoctorDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(DoctorDialog)
        self.verticalLayout.setContentsMargins(-1, -1, 12, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DoctorDialog)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.uiDoctorResultTextEdit = QtWidgets.QTextEdit(DoctorDialog)
        self.uiDoctorResultTextEdit.setObjectName("uiDoctorResultTextEdit")
        self.verticalLayout.addWidget(self.uiDoctorResultTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.uiOkButton = QtWidgets.QDialogButtonBox(DoctorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiOkButton.sizePolicy().hasHeightForWidth())
        self.uiOkButton.setSizePolicy(sizePolicy)
        self.uiOkButton.setOrientation(QtCore.Qt.Horizontal)
        self.uiOkButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.uiOkButton.setObjectName("uiOkButton")
        self.horizontalLayout.addWidget(self.uiOkButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DoctorDialog)
        QtCore.QMetaObject.connectSlotsByName(DoctorDialog)

    def retranslateUi(self, DoctorDialog):
        _translate = QtCore.QCoreApplication.translate
        DoctorDialog.setWindowTitle(_translate("DoctorDialog", "GNS3 Doctor"))
        self.label.setText(_translate("DoctorDialog", "<html><head/><body><p>This will list potential problem in your GNS3 installation:</p></body></html>"))
        self.uiDoctorResultTextEdit.setHtml(_translate("DoctorDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:600; font-style:italic;\">Starting checks...</span></p></body></html>"))

from . import resources_rc
