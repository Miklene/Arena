# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quest_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuestWidget(object):
    def setupUi(self, QuestWidget):
        QuestWidget.setObjectName("QuestWidget")
        QuestWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(QuestWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_name = QtWidgets.QLabel(QuestWidget)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.label_description = QtWidgets.QLabel(QuestWidget)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.label_description)
        self.log = QtWidgets.QPlainTextEdit(QuestWidget)
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)

        self.retranslateUi(QuestWidget)
        QtCore.QMetaObject.connectSlotsByName(QuestWidget)

    def retranslateUi(self, QuestWidget):
        _translate = QtCore.QCoreApplication.translate
        QuestWidget.setWindowTitle(_translate("QuestWidget", "Form"))
        self.label_name.setText(_translate("QuestWidget", "Название квеста"))
        self.label_description.setText(_translate("QuestWidget", "Описание квеста"))
