# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvissuperUIII.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(QtCore.Qt.Window |
                      QtCore.Qt.WindowMinimizeButtonHint |
                      QtCore.Qt.WindowMaximizeButtonHint |
                      QtCore.Qt.WindowCloseButtonHint)

        Dialog.resize(836, 570)
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(0,0,836, 570))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.background.setFont(font)
        self.background.setStyleSheet("background-color:black")
        self.background.setText("")
        self.background.setObjectName("background")
        self.jarvisgui = QtWidgets.QLabel(Dialog)
        self.jarvisgui.setGeometry(QtCore.QRect(0, 10, 371, 351))
        self.jarvisgui.setText("")
        self.jarvisgui.setPixmap(QtGui.QPixmap("C:\\Users\\sanja\\OneDrive\\Desktop\\NewProjects\\assests\\Mr3W.gif"))
        self.jarvisgui.setScaledContents(True)
        self.jarvisgui.setObjectName("jarvisgui")
        self.earth = QtWidgets.QLabel(Dialog)
        self.earth.setGeometry(QtCore.QRect(300, 400, 111, 151))
        self.earth.setText("")
        self.earth.setPixmap(QtGui.QPixmap("C:\\Users\\sanja\\OneDrive\\Desktop\\NewProjects\\assests\\PcOY.gif"))
        self.earth.setScaledContents(True)
        self.earth.setObjectName("earth")
        self.cyborg = QtWidgets.QLabel(Dialog)
        self.cyborg.setGeometry(QtCore.QRect(530, 10, 311, 291))
        self.cyborg.setText("")
        self.cyborg.setPixmap(QtGui.QPixmap("C:\\Users\\sanja\\OneDrive\\Desktop\\NewProjects\\assests\\cyborg.png"))
        self.cyborg.setScaledContents(True)
        self.cyborg.setObjectName("cyborg")
        self.date = QtWidgets.QLabel(Dialog)
        self.date.setGeometry(QtCore.QRect(10, 390, 291, 91))
        self.date.setText("")
        self.date.setPixmap(QtGui.QPixmap("C:\\Users\\sanja\\OneDrive\\Desktop\\NewProjects\\assests\\freepik__adjust__87008.png"))
        self.date.setScaledContents(True)
        self.date.setObjectName("date")
        self.time = QtWidgets.QLabel(Dialog)
        self.time.setGeometry(QtCore.QRect(10, 470, 271, 81))
        self.time.setText("")
        self.time.setPixmap(QtGui.QPixmap("C:\\Users\\sanja\\OneDrive\\Desktop\\NewProjects\\assests\\freepik__adjust__87008.png"))
        self.time.setScaledContents(True)
        self.time.setObjectName("time")
        self.datelabel = QtWidgets.QTextBrowser(Dialog)
        self.datelabel.setGeometry(QtCore.QRect(60, 420, 211, 71))
        self.datelabel.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:white;\n"
"border-radius:none;")
        self.datelabel.setObjectName("datelabel")
        self.timelabel = QtWidgets.QTextBrowser(Dialog)
        self.timelabel.setGeometry(QtCore.QRect(60, 495, 211, 71))
        self.timelabel.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:white;\n"
"border-radius:none;")
        self.timelabel.setObjectName("timelabel")
        self.ironman = QtWidgets.QLabel(Dialog)
        self.ironman.setGeometry(QtCore.QRect(495, 320, 241, 151))
        self.ironman.setText("")
        self.ironman.setPixmap(QtGui.QPixmap("C:\\Users\\sanja\\OneDrive\\Desktop\\NewProjects\\assests\\QNBH.gif"))
        self.ironman.setScaledContents(True)
        self.ironman.setObjectName("ironman")
        self.startlabel = QtWidgets.QLabel(Dialog)
        self.startlabel.setGeometry(QtCore.QRect(455, 470, 151, 71))
        self.startlabel.setText("")
        self.startlabel.setPixmap(QtGui.QPixmap("C:\\Users\\sanja\\OneDrive\\Desktop\\NewProjects\\assests\\Screenshot 2025-04-18 124600.png"))
        self.startlabel.setScaledContents(True)
        self.startlabel.setObjectName("startlabel")
        self.quitlabel = QtWidgets.QLabel(Dialog)
        self.quitlabel.setGeometry(QtCore.QRect(605, 470, 161, 71))
        self.quitlabel.setText("")
        self.quitlabel.setPixmap(QtGui.QPixmap("C:\\Users\\sanja\\OneDrive\\Desktop\\NewProjects\\assests\\Screenshot 2025-04-18 124612.png"))
        self.quitlabel.setScaledContents(True)
        self.quitlabel.setObjectName("quitlabel")
        self.startbutton = QtWidgets.QPushButton(Dialog)
        self.startbutton.setGeometry(QtCore.QRect(370, 400, 81, 31))
        self.startbutton.setStyleSheet("background:transparent;")
        self.startbutton.setText("")
        self.startbutton.setObjectName("startbutton")
        self.quitbutton = QtWidgets.QPushButton(Dialog)
        self.quitbutton.setGeometry(QtCore.QRect(520, 390, 121, 31))
        self.quitbutton.setStyleSheet("background:transparent;")
        self.quitbutton.setText("")
        self.quitbutton.setObjectName("quitbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.datelabel.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Date:18-04-2025</span></p></body></html>"))
        self.timelabel.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Time:12:32</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
