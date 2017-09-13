# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Programs/gns3/gns3-gui-2.1.0b2/gns3/ui/filter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilterDialog(object):
    def setupUi(self, FilterDialog):
        FilterDialog.setObjectName("FilterDialog")
        FilterDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        FilterDialog.resize(799, 255)
        FilterDialog.setStyleSheet("\n"
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(FilterDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiVerticalLayout = QtWidgets.QVBoxLayout()
        self.uiVerticalLayout.setObjectName("uiVerticalLayout")
        self.groupBox = QtWidgets.QGroupBox(FilterDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimum(-1)
        self.spinBox.setMaximum(500)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.uiVerticalLayout.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.uiVerticalLayout)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(FilterDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.verticalLayout_3.addWidget(self.uiButtonBox)

        self.retranslateUi(FilterDialog)
        self.uiButtonBox.accepted.connect(FilterDialog.accept)
        self.uiButtonBox.rejected.connect(FilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FilterDialog)

    def retranslateUi(self, FilterDialog):
        _translate = QtCore.QCoreApplication.translate
        FilterDialog.setWindowTitle(_translate("FilterDialog", "Packet filters"))
        self.groupBox.setTitle(_translate("FilterDialog", "Delay"))
        self.label_3.setText(_translate("FilterDialog", "Description"))
        self.label.setText(_translate("FilterDialog", "Delay:"))
        self.label_2.setText(_translate("FilterDialog", "ms"))

from . import resources_rc
