# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Home_ASB_Tool.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(838, 611)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 351, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lblHistory = QtGui.QLabel(self.tab_3)
        self.lblHistory.setGeometry(QtCore.QRect(10, 40, 791, 411))
        self.lblHistory.setText(_fromUtf8(""))
        self.lblHistory.setObjectName(_fromUtf8("lblHistory"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 151, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 380, 791, 91))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setLineWidth(1)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lblPlsWait = QtGui.QLabel(self.tab_2)
        self.lblPlsWait.setGeometry(QtCore.QRect(260, 40, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPlsWait.setFont(font)
        self.lblPlsWait.setText(_fromUtf8(""))
        self.lblPlsWait.setObjectName(_fromUtf8("lblPlsWait"))
        self.lblWordscloud = QtGui.QLabel(self.tab_2)
        self.lblWordscloud.setGeometry(QtCore.QRect(10, 110, 381, 201))
        self.lblWordscloud.setText(_fromUtf8(""))
        self.lblWordscloud.setObjectName(_fromUtf8("lblWordscloud"))
        self.lblPie = QtGui.QLabel(self.tab_2)
        self.lblPie.setGeometry(QtCore.QRect(420, 110, 381, 201))
        self.lblPie.setText(_fromUtf8(""))
        self.lblPie.setObjectName(_fromUtf8("lblPie"))
        self.lblWCName = QtGui.QLabel(self.tab_2)
        self.lblWCName.setGeometry(QtCore.QRect(130, 80, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lblWCName.setFont(font)
        self.lblWCName.setText(_fromUtf8(""))
        self.lblWCName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWCName.setObjectName(_fromUtf8("lblWCName"))
        self.lblPieName = QtGui.QLabel(self.tab_2)
        self.lblPieName.setGeometry(QtCore.QRect(520, 80, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lblPieName.setFont(font)
        self.lblPieName.setText(_fromUtf8(""))
        self.lblPieName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPieName.setObjectName(_fromUtf8("lblPieName"))
        self.lblgreen = QtGui.QLabel(self.tab_2)
        self.lblgreen.setGeometry(QtCore.QRect(510, 330, 46, 13))
        self.lblgreen.setText(_fromUtf8(""))
        self.lblgreen.setScaledContents(False)
        self.lblgreen.setObjectName(_fromUtf8("lblgreen"))
        self.lblpostiv = QtGui.QLabel(self.tab_2)
        self.lblpostiv.setGeometry(QtCore.QRect(580, 330, 46, 13))
        self.lblpostiv.setText(_fromUtf8(""))
        self.lblpostiv.setObjectName(_fromUtf8("lblpostiv"))
        self.lblred = QtGui.QLabel(self.tab_2)
        self.lblred.setGeometry(QtCore.QRect(640, 330, 46, 13))
        self.lblred.setText(_fromUtf8(""))
        self.lblred.setObjectName(_fromUtf8("lblred"))
        self.lblNegtv = QtGui.QLabel(self.tab_2)
        self.lblNegtv.setGeometry(QtCore.QRect(710, 330, 46, 13))
        self.lblNegtv.setText(_fromUtf8(""))
        self.lblNegtv.setObjectName(_fromUtf8("lblNegtv"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 314, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtnumber = QtGui.QLineEdit(self.tab)
        self.txtnumber.setGeometry(QtCore.QRect(260, 90, 201, 20))
        self.txtnumber.setObjectName(_fromUtf8("txtnumber"))
        self.btnsubmitsettings = QtGui.QPushButton(self.tab)
        self.btnsubmitsettings.setGeometry(QtCore.QRect(490, 90, 101, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnsubmitsettings.setFont(font)
        self.btnsubmitsettings.setObjectName(_fromUtf8("btnsubmitsettings"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(110, 60, 141, 78))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lblSuccess = QtGui.QLabel(self.tab)
        self.lblSuccess.setGeometry(QtCore.QRect(100, 180, 551, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lblSuccess.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblSuccess.setFont(font)
        self.lblSuccess.setText(_fromUtf8(""))
        self.lblSuccess.setObjectName(_fromUtf8("lblSuccess"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose_Application = QtGui.QAction(MainWindow)
        self.actionClose_Application.setObjectName(_fromUtf8("actionClose_Application"))
        self.actionCLOSE = QtGui.QAction(MainWindow)
        self.actionCLOSE.setObjectName(_fromUtf8("actionCLOSE"))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "ASB detection tool", None))
        self.label_4.setText(_translate("MainWindow", "Shows the history of the users browsing behavior :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Log analysis", None))
        self.pushButton.setText(_translate("MainWindow", "Generate report", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Generate report", None))
        self.label_2.setText(_translate("MainWindow", "Get a summary of the report to your mobile", None))
        self.btnsubmitsettings.setText(_translate("MainWindow", "Submit", None))
        self.label_3.setText(_translate("MainWindow", "Enter mobile number :    +94", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Settings", None))
        self.actionClose_Application.setText(_translate("MainWindow", "Close Application", None))
        self.actionCLOSE.setText(_translate("MainWindow", "CLOSE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

