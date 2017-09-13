# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Programs/gns3/gns3-gui-2.0.3/gns3/ui/configuration_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_configurationDialog(object):
    def setupUi(self, configurationDialog):
        configurationDialog.setObjectName("configurationDialog")
        configurationDialog.resize(585, 454)
        configurationDialog.setStyleSheet("\n"
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
        configurationDialog.setModal(True)
        self.gridlayout = QtWidgets.QGridLayout(configurationDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.splitter = QtWidgets.QSplitter(configurationDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayout = QtWidgets.QWidget(self.splitter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.verticalLayout)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(4)
        self.vboxlayout.setObjectName("vboxlayout")
        self.uiTitleLabel = QtWidgets.QLabel(self.verticalLayout)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.uiTitleLabel.setFont(font)
        self.uiTitleLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.uiTitleLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.uiTitleLabel.setTextFormat(QtCore.Qt.PlainText)
        self.uiTitleLabel.setObjectName("uiTitleLabel")
        self.vboxlayout.addWidget(self.uiTitleLabel)
        self.uiConfigStackedWidget = QtWidgets.QStackedWidget(self.verticalLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiConfigStackedWidget.sizePolicy().hasHeightForWidth())
        self.uiConfigStackedWidget.setSizePolicy(sizePolicy)
        self.uiConfigStackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.uiConfigStackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.uiConfigStackedWidget.setObjectName("uiConfigStackedWidget")
        self.uiEmptyPageWidget = QtWidgets.QWidget()
        self.uiEmptyPageWidget.setObjectName("uiEmptyPageWidget")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.uiEmptyPageWidget)
        self.vboxlayout1.setContentsMargins(0, 4, 0, 0)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.uiConfigStackedWidget.addWidget(self.uiEmptyPageWidget)
        self.vboxlayout.addWidget(self.uiConfigStackedWidget)
        self.gridlayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(configurationDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridlayout.addWidget(self.uiButtonBox, 1, 0, 1, 1)

        self.retranslateUi(configurationDialog)
        self.uiConfigStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(configurationDialog)

    def retranslateUi(self, configurationDialog):
        _translate = QtCore.QCoreApplication.translate
        configurationDialog.setWindowTitle(_translate("configurationDialog", "Configuration"))
        self.uiTitleLabel.setText(_translate("configurationDialog", "Configuration"))

from . import resources_rc
