# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'journal_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JournalWidget(object):
    def setupUi(self, JournalWidget):
        JournalWidget.setObjectName("JournalWidget")
        JournalWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(JournalWidget)
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_journal = QtWidgets.QGroupBox(JournalWidget)
        self.groupBox_journal.setObjectName("groupBox_journal")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_journal)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_journal)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_journal)

        self.retranslateUi(JournalWidget)
        QtCore.QMetaObject.connectSlotsByName(JournalWidget)

    def retranslateUi(self, JournalWidget):
        _translate = QtCore.QCoreApplication.translate
        JournalWidget.setWindowTitle(_translate("JournalWidget", "Form"))
        self.groupBox_journal.setTitle(_translate("JournalWidget", "Журнал"))
