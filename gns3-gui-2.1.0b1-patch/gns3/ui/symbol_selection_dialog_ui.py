# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.0.3/gns3/ui/symbol_selection_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SymbolSelectionDialog(object):
    def setupUi(self, SymbolSelectionDialog):
        SymbolSelectionDialog.setObjectName("SymbolSelectionDialog")
        SymbolSelectionDialog.resize(521, 655)
        SymbolSelectionDialog.setStyleSheet("QWidget {\n"
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
        SymbolSelectionDialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SymbolSelectionDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiCustomSymbolRadioButton = QtWidgets.QRadioButton(SymbolSelectionDialog)
        self.uiCustomSymbolRadioButton.setChecked(True)
        self.uiCustomSymbolRadioButton.setObjectName("uiCustomSymbolRadioButton")
        self.horizontalLayout_2.addWidget(self.uiCustomSymbolRadioButton)
        self.uiBuiltInSymbolRadioButton = QtWidgets.QRadioButton(SymbolSelectionDialog)
        self.uiBuiltInSymbolRadioButton.setObjectName("uiBuiltInSymbolRadioButton")
        self.horizontalLayout_2.addWidget(self.uiBuiltInSymbolRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.uiCustomSymbolGroupBox = QtWidgets.QGroupBox(SymbolSelectionDialog)
        self.uiCustomSymbolGroupBox.setObjectName("uiCustomSymbolGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiCustomSymbolGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiSymbolLabel = QtWidgets.QLabel(self.uiCustomSymbolGroupBox)
        self.uiSymbolLabel.setObjectName("uiSymbolLabel")
        self.gridLayout.addWidget(self.uiSymbolLabel, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiSymbolLineEdit = QtWidgets.QLineEdit(self.uiCustomSymbolGroupBox)
        self.uiSymbolLineEdit.setObjectName("uiSymbolLineEdit")
        self.horizontalLayout_7.addWidget(self.uiSymbolLineEdit)
        self.uiSymbolToolButton = QtWidgets.QToolButton(self.uiCustomSymbolGroupBox)
        self.uiSymbolToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiSymbolToolButton.setObjectName("uiSymbolToolButton")
        self.horizontalLayout_7.addWidget(self.uiSymbolToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.uiCustomSymbolGroupBox)
        self.uiBuiltInGroupBox = QtWidgets.QGroupBox(SymbolSelectionDialog)
        self.uiBuiltInGroupBox.setObjectName("uiBuiltInGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiBuiltInGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiBuiltinSymbolOnlyCheckBox = QtWidgets.QCheckBox(self.uiBuiltInGroupBox)
        self.uiBuiltinSymbolOnlyCheckBox.setObjectName("uiBuiltinSymbolOnlyCheckBox")
        self.verticalLayout.addWidget(self.uiBuiltinSymbolOnlyCheckBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiSearchLabel = QtWidgets.QLabel(self.uiBuiltInGroupBox)
        self.uiSearchLabel.setObjectName("uiSearchLabel")
        self.horizontalLayout_3.addWidget(self.uiSearchLabel)
        self.uiSearchLineEdit = QtWidgets.QLineEdit(self.uiBuiltInGroupBox)
        self.uiSearchLineEdit.setObjectName("uiSearchLineEdit")
        self.horizontalLayout_3.addWidget(self.uiSearchLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.uiSymbolListWidget = QtWidgets.QListWidget(self.uiBuiltInGroupBox)
        self.uiSymbolListWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.uiSymbolListWidget.setObjectName("uiSymbolListWidget")
        self.verticalLayout.addWidget(self.uiSymbolListWidget)
        self.label = QtWidgets.QLabel(self.uiBuiltInGroupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.uiBuiltInGroupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(SymbolSelectionDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.horizontalLayout.addWidget(self.uiButtonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.uiBuiltInGroupBox.raise_()
        self.uiCustomSymbolGroupBox.raise_()

        self.retranslateUi(SymbolSelectionDialog)
        self.uiButtonBox.accepted.connect(SymbolSelectionDialog.accept)
        self.uiButtonBox.rejected.connect(SymbolSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SymbolSelectionDialog)

    def retranslateUi(self, SymbolSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        SymbolSelectionDialog.setWindowTitle(_translate("SymbolSelectionDialog", "Symbol selection"))
        self.uiCustomSymbolRadioButton.setText(_translate("SymbolSelectionDialog", "Use a custom symbol"))
        self.uiBuiltInSymbolRadioButton.setText(_translate("SymbolSelectionDialog", "Symbols library"))
        self.uiCustomSymbolGroupBox.setTitle(_translate("SymbolSelectionDialog", "Custom symbol"))
        self.uiSymbolLabel.setText(_translate("SymbolSelectionDialog", "Path:"))
        self.uiSymbolToolButton.setText(_translate("SymbolSelectionDialog", "&Browse..."))
        self.uiBuiltInGroupBox.setTitle(_translate("SymbolSelectionDialog", "Symbols"))
        self.uiBuiltinSymbolOnlyCheckBox.setText(_translate("SymbolSelectionDialog", "Show only built-in symbols"))
        self.uiSearchLabel.setText(_translate("SymbolSelectionDialog", "Search:"))
        self.label.setText(_translate("SymbolSelectionDialog", "You can add your own symbols in the symbols directory."))

from . import resources_rc
