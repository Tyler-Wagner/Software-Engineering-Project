from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("IntruWatch Return")
        Form.resize(506, 337)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 191, 41))
        self.label.setStyleSheet("color:blue;")
        self.label.setObjectName("label")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(270, 290, 221, 31))
        self.closeButton.setObjectName("closeButton")
        self.vTotalList = QtWidgets.QListWidget(Form)
        self.vTotalList.setGeometry(QtCore.QRect(20, 60, 471, 221))
        self.vTotalList.setObjectName("vTotalList")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Virus Total</span></p></body></html>"))
        self.closeButton.setText(_translate("Form", "Close"))
