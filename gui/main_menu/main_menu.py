# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(222, 192)
        self.gridLayout = QtWidgets.QGridLayout(MainMenu)
        self.gridLayout.setObjectName("gridLayout")
        self.button_back = QtWidgets.QPushButton(MainMenu)
        self.button_back.setObjectName("button_back")
        self.gridLayout.addWidget(self.button_back, 3, 1, 1, 1)
        self.button_exit = QtWidgets.QPushButton(MainMenu)
        self.button_exit.setObjectName("button_exit")
        self.gridLayout.addWidget(self.button_exit, 4, 1, 1, 1)
        self.button_save = QtWidgets.QPushButton(MainMenu)
        self.button_save.setObjectName("button_save")
        self.gridLayout.addWidget(self.button_save, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.button_new_game = QtWidgets.QPushButton(MainMenu)
        self.button_new_game.setObjectName("button_new_game")
        self.gridLayout.addWidget(self.button_new_game, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(MainMenu)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Главное меню"))
        self.button_back.setText(_translate("MainMenu", "Назад"))
        self.button_exit.setText(_translate("MainMenu", "Выход"))
        self.button_save.setText(_translate("MainMenu", "Сохранить игру"))
        self.button_new_game.setText(_translate("MainMenu", "Новая игра"))
        self.pushButton.setText(_translate("MainMenu", "Загрузить игру"))
