# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Dec  3 17:10:42 2010
#      by: PyQt4 UI code generator snapshot-4.8.2-4dddaa7e9c07
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 413)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.mainFrame = QtGui.QFrame(self.centralwidget)
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.gridlayout = QtGui.QGridLayout(self.mainFrame)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.agreeCheckBox = QtGui.QCheckBox(self.mainFrame)
        self.agreeCheckBox.setObjectName(_fromUtf8("agreeCheckBox"))
        self.gridlayout.addWidget(self.agreeCheckBox, 6, 0, 1, 5)
        self.label = QtGui.QLabel(self.mainFrame)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 5, 0, 1, 1)
        self.nameLabel = QtGui.QLabel(self.mainFrame)
        self.nameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.gridlayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.maleRadioButton = QtGui.QRadioButton(self.mainFrame)
        self.maleRadioButton.setObjectName(_fromUtf8("maleRadioButton"))
        self.gridlayout.addWidget(self.maleRadioButton, 1, 1, 1, 1)
        self.passwordLabel = QtGui.QLabel(self.mainFrame)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridlayout.addWidget(self.passwordLabel, 3, 0, 1, 1)
        self.countryCombo = QtGui.QComboBox(self.mainFrame)
        self.countryCombo.setObjectName(_fromUtf8("countryCombo"))
        self.countryCombo.addItem(_fromUtf8(""))
        self.countryCombo.addItem(_fromUtf8(""))
        self.countryCombo.addItem(_fromUtf8(""))
        self.countryCombo.addItem(_fromUtf8(""))
        self.countryCombo.addItem(_fromUtf8(""))
        self.countryCombo.addItem(_fromUtf8(""))
        self.countryCombo.addItem(_fromUtf8(""))
        self.gridlayout.addWidget(self.countryCombo, 4, 1, 1, 4)
        self.ageLabel = QtGui.QLabel(self.mainFrame)
        self.ageLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ageLabel.setObjectName(_fromUtf8("ageLabel"))
        self.gridlayout.addWidget(self.ageLabel, 2, 0, 1, 1)
        self.countryLabel = QtGui.QLabel(self.mainFrame)
        self.countryLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.countryLabel.setObjectName(_fromUtf8("countryLabel"))
        self.gridlayout.addWidget(self.countryLabel, 4, 0, 1, 1)
        self.genderLabel = QtGui.QLabel(self.mainFrame)
        self.genderLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.genderLabel.setObjectName(_fromUtf8("genderLabel"))
        self.gridlayout.addWidget(self.genderLabel, 1, 0, 1, 1)
        self.passwordEdit = QtGui.QLineEdit(self.mainFrame)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.gridlayout.addWidget(self.passwordEdit, 3, 1, 1, 4)
        self.femaleRadioButton = QtGui.QRadioButton(self.mainFrame)
        self.femaleRadioButton.setObjectName(_fromUtf8("femaleRadioButton"))
        self.gridlayout.addWidget(self.femaleRadioButton, 1, 2, 1, 2)
        self.ageSpinBox = QtGui.QSpinBox(self.mainFrame)
        self.ageSpinBox.setMinimum(12)
        self.ageSpinBox.setProperty(_fromUtf8("value"), 22)
        self.ageSpinBox.setObjectName(_fromUtf8("ageSpinBox"))
        self.gridlayout.addWidget(self.ageSpinBox, 2, 1, 1, 2)
        self.nameCombo = QtGui.QComboBox(self.mainFrame)
        self.nameCombo.setEditable(True)
        self.nameCombo.setObjectName(_fromUtf8("nameCombo"))
        self.gridlayout.addWidget(self.nameCombo, 0, 1, 1, 4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(61, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1, 2, 3, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(self.mainFrame)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 7, 3, 1, 2)
        self.professionList = QtGui.QListWidget(self.mainFrame)
        self.professionList.setObjectName(_fromUtf8("professionList"))
        QtGui.QListWidgetItem(self.professionList)
        QtGui.QListWidgetItem(self.professionList)
        QtGui.QListWidgetItem(self.professionList)
        self.gridlayout.addWidget(self.professionList, 5, 1, 1, 4)
        self.vboxlayout.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.exitAction = QtGui.QAction(MainWindow)
        self.exitAction.setObjectName(_fromUtf8("exitAction"))
        self.aboutQtAction = QtGui.QAction(MainWindow)
        self.aboutQtAction.setObjectName(_fromUtf8("aboutQtAction"))
        self.editStyleAction = QtGui.QAction(MainWindow)
        self.editStyleAction.setObjectName(_fromUtf8("editStyleAction"))
        self.aboutAction = QtGui.QAction(MainWindow)
        self.aboutAction.setObjectName(_fromUtf8("aboutAction"))
        self.menu_File.addAction(self.editStyleAction)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.exitAction)
        self.menu_Help.addAction(self.aboutAction)
        self.menu_Help.addAction(self.aboutQtAction)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.label.setBuddy(self.professionList)
        self.nameLabel.setBuddy(self.nameCombo)
        self.passwordLabel.setBuddy(self.passwordEdit)
        self.ageLabel.setBuddy(self.ageSpinBox)
        self.countryLabel.setBuddy(self.countryCombo)

        self.retranslateUi(MainWindow)
        self.countryCombo.setCurrentIndex(6)
        self.professionList.setCurrentRow(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Style Sheet", None, QtGui.QApplication.UnicodeUTF8))
        self.agreeCheckBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Please read the LICENSE file before checking", None, QtGui.QApplication.UnicodeUTF8))
        self.agreeCheckBox.setText(QtGui.QApplication.translate("MainWindow", "I accept the terms and &conditions", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Profession:", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("MainWindow", "&Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.maleRadioButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Check this if you are male", None, QtGui.QApplication.UnicodeUTF8))
        self.maleRadioButton.setText(QtGui.QApplication.translate("MainWindow", "&Male", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("MainWindow", "&Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.countryCombo.setToolTip(QtGui.QApplication.translate("MainWindow", "Specify country of origin", None, QtGui.QApplication.UnicodeUTF8))
        self.countryCombo.setStatusTip(QtGui.QApplication.translate("MainWindow", "Specify country of origin", None, QtGui.QApplication.UnicodeUTF8))
        self.countryCombo.setItemText(0, QtGui.QApplication.translate("MainWindow", "Egypt", None, QtGui.QApplication.UnicodeUTF8))
        self.countryCombo.setItemText(1, QtGui.QApplication.translate("MainWindow", "France", None, QtGui.QApplication.UnicodeUTF8))
        self.countryCombo.setItemText(2, QtGui.QApplication.translate("MainWindow", "Germany", None, QtGui.QApplication.UnicodeUTF8))
        self.countryCombo.setItemText(3, QtGui.QApplication.translate("MainWindow", "India", None, QtGui.QApplication.UnicodeUTF8))
        self.countryCombo.setItemText(4, QtGui.QApplication.translate("MainWindow", "Italy", None, QtGui.QApplication.UnicodeUTF8))
        self.countryCombo.setItemText(5, QtGui.QApplication.translate("MainWindow", "Norway", None, QtGui.QApplication.UnicodeUTF8))
        self.countryCombo.setItemText(6, QtGui.QApplication.translate("MainWindow", "Pakistan", None, QtGui.QApplication.UnicodeUTF8))
        self.ageLabel.setText(QtGui.QApplication.translate("MainWindow", "&Age:", None, QtGui.QApplication.UnicodeUTF8))
        self.countryLabel.setText(QtGui.QApplication.translate("MainWindow", "Country:", None, QtGui.QApplication.UnicodeUTF8))
        self.genderLabel.setText(QtGui.QApplication.translate("MainWindow", "Gender:", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Specify your password", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Specify your password", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordEdit.setText(QtGui.QApplication.translate("MainWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.femaleRadioButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Check this if you are female", None, QtGui.QApplication.UnicodeUTF8))
        self.femaleRadioButton.setText(QtGui.QApplication.translate("MainWindow", "&Female", None, QtGui.QApplication.UnicodeUTF8))
        self.ageSpinBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Specify your age", None, QtGui.QApplication.UnicodeUTF8))
        self.ageSpinBox.setStatusTip(QtGui.QApplication.translate("MainWindow", "Specify your age", None, QtGui.QApplication.UnicodeUTF8))
        self.nameCombo.setToolTip(QtGui.QApplication.translate("MainWindow", "Specify your name", None, QtGui.QApplication.UnicodeUTF8))
        self.professionList.setToolTip(QtGui.QApplication.translate("MainWindow", "Select your profession", None, QtGui.QApplication.UnicodeUTF8))
        self.professionList.setStatusTip(QtGui.QApplication.translate("MainWindow", "Specify your name here", None, QtGui.QApplication.UnicodeUTF8))
        self.professionList.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Specify your name here", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.professionList.isSortingEnabled()
        self.professionList.setSortingEnabled(False)
        self.professionList.item(0).setText(QtGui.QApplication.translate("MainWindow", "Developer", None, QtGui.QApplication.UnicodeUTF8))
        self.professionList.item(1).setText(QtGui.QApplication.translate("MainWindow", "Student", None, QtGui.QApplication.UnicodeUTF8))
        self.professionList.item(2).setText(QtGui.QApplication.translate("MainWindow", "Fisherman", None, QtGui.QApplication.UnicodeUTF8))
        self.professionList.setSortingEnabled(__sortingEnabled)
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAction.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutQtAction.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.editStyleAction.setText(QtGui.QApplication.translate("MainWindow", "Edit &Style...", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutAction.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
