# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1241, 823)
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(60, 60, 241, 251))
        self.label.setMinimumSize(QtCore.QSize(241, 0))
        self.label.setMaximumSize(QtCore.QSize(241, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/download.jpeg"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.driveon_pb = QtWidgets.QPushButton(Widget)
        self.driveon_pb.setGeometry(QtCore.QRect(350, 50, 75, 71))
        self.driveon_pb.setObjectName("driveon_pb")
        self.pushButton_7 = QtWidgets.QPushButton(Widget)
        self.pushButton_7.setGeometry(QtCore.QRect(490, 180, 75, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_12 = QtWidgets.QPushButton(Widget)
        self.pushButton_12.setGeometry(QtCore.QRect(350, 430, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_21 = QtWidgets.QPushButton(Widget)
        self.pushButton_21.setGeometry(QtCore.QRect(950, 180, 75, 71))
        self.pushButton_21.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_14 = QtWidgets.QPushButton(Widget)
        self.pushButton_14.setGeometry(QtCore.QRect(620, 430, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_5 = QtWidgets.QPushButton(Widget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 310, 75, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(Widget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 180, 75, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line_2 = QtWidgets.QFrame(Widget)
        self.line_2.setGeometry(QtCore.QRect(730, 50, 16, 451))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_8 = QtWidgets.QPushButton(Widget)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 310, 75, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(1260, 620, 61, 61))
        self.label_2.setStyleSheet("QLabel {\n"
"    background-color: red;\n"
"    border-radius: 30%;  /* Set border-radius to 50% for a round appearance */\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QLabel[ledOn=\"true\"] {\n"
"    background-color: green;\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.pushButton_22 = QtWidgets.QPushButton(Widget)
        self.pushButton_22.setGeometry(QtCore.QRect(950, 50, 75, 71))
        self.pushButton_22.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_22.setAutoRepeat(False)
        self.pushButton_22.setObjectName("pushButton_22")
        self.start_pb = QtWidgets.QPushButton(Widget)
        self.start_pb.setGeometry(QtCore.QRect(60, 430, 75, 71))
        self.start_pb.setStyleSheet("")
        self.start_pb.setObjectName("start_pb")
        self.pushButton_10 = QtWidgets.QPushButton(Widget)
        self.pushButton_10.setGeometry(QtCore.QRect(620, 180, 75, 71))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_15 = QtWidgets.QPushButton(Widget)
        self.pushButton_15.setGeometry(QtCore.QRect(780, 430, 75, 71))
        self.pushButton_15.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_15.setObjectName("pushButton_15")
        self.stop_pb = QtWidgets.QPushButton(Widget)
        self.stop_pb.setGeometry(QtCore.QRect(200, 430, 75, 71))
        self.stop_pb.setObjectName("stop_pb")
        self.pushButton_13 = QtWidgets.QPushButton(Widget)
        self.pushButton_13.setGeometry(QtCore.QRect(490, 430, 75, 71))
        self.pushButton_13.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_20 = QtWidgets.QPushButton(Widget)
        self.pushButton_20.setGeometry(QtCore.QRect(950, 310, 75, 71))
        self.pushButton_20.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_20.setObjectName("pushButton_20")
        self.line = QtWidgets.QFrame(Widget)
        self.line.setGeometry(QtCore.QRect(900, 60, 16, 451))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_16 = QtWidgets.QPushButton(Widget)
        self.pushButton_16.setGeometry(QtCore.QRect(780, 310, 75, 71))
        self.pushButton_16.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_23 = QtWidgets.QPushButton(Widget)
        self.pushButton_23.setGeometry(QtCore.QRect(1250, 490, 75, 71))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_19 = QtWidgets.QPushButton(Widget)
        self.pushButton_19.setGeometry(QtCore.QRect(950, 430, 75, 71))
        self.pushButton_19.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_17 = QtWidgets.QPushButton(Widget)
        self.pushButton_17.setGeometry(QtCore.QRect(780, 180, 75, 71))
        self.pushButton_17.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Widget)
        self.pushButton_18.setGeometry(QtCore.QRect(780, 50, 75, 71))
        self.pushButton_18.setStyleSheet("QPushButton:pressed {\n"
"    background-color: green;\n"
"}\n"
"")
        self.pushButton_18.setObjectName("pushButton_18")
        self.z_axislock_pb = QtWidgets.QPushButton(Widget)
        self.z_axislock_pb.setGeometry(QtCore.QRect(490, 50, 75, 71))
        self.z_axislock_pb.setObjectName("z_axislock_pb")
        self.line_3 = QtWidgets.QFrame(Widget)
        self.line_3.setGeometry(QtCore.QRect(320, 50, 16, 451))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.dryrun_pb = QtWidgets.QPushButton(Widget)
        self.dryrun_pb.setGeometry(QtCore.QRect(620, 50, 75, 71))
        self.dryrun_pb.setObjectName("dryrun_pb")
        self.pushButton_11 = QtWidgets.QPushButton(Widget)
        self.pushButton_11.setGeometry(QtCore.QRect(620, 310, 75, 71))
        self.pushButton_11.setObjectName("pushButton_11")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.driveon_pb.setText(_translate("Widget", "DRIVE ON"))
        self.pushButton_7.setText(_translate("Widget", "MDI\n"
" MODE"))
        self.pushButton_12.setText(_translate("Widget", "+"))
        self.pushButton_21.setText(_translate("Widget", "Alarm \n"
"over"))
        self.pushButton_14.setText(_translate("Widget", "-"))
        self.pushButton_5.setText(_translate("Widget", "X"))
        self.pushButton_4.setText(_translate("Widget", "JOG\n"
" MODE"))
        self.pushButton_8.setText(_translate("Widget", "Y"))
        self.label_2.setText(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">Laser</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">Ready</span></p></body></html>"))
        self.pushButton_22.setText(_translate("Widget", "Piershimg\n"
" End"))
        self.start_pb.setText(_translate("Widget", "START"))
        self.pushButton_10.setText(_translate("Widget", "AUTO\n"
" MODE"))
        self.pushButton_15.setText(_translate("Widget", "Retrace \n"
"REV"))
        self.stop_pb.setText(_translate("Widget", "STOP"))
        self.pushButton_13.setText(_translate("Widget", "ZERO"))
        self.pushButton_20.setText(_translate("Widget", "Alarm \n"
"Reset"))
        self.pushButton_16.setText(_translate("Widget", "Retrace \n"
" FWD"))
        self.pushButton_23.setText(_translate("Widget", "Laser ON"))
        self.pushButton_19.setText(_translate("Widget", "Lock \n"
" Reset"))
        self.pushButton_17.setText(_translate("Widget", " NC  \n"
" OFFSET"))
        self.pushButton_18.setText(_translate("Widget", "NC \n"
" REF"))
        self.z_axislock_pb.setText(_translate("Widget", "Z-AXIS \n"
"LOCK"))
        self.dryrun_pb.setText(_translate("Widget", "Dry Run"))
        self.pushButton_11.setText(_translate("Widget", "Z"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
