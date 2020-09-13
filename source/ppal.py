# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vent.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1094, 813)
        MainWindow.setMaximumSize(QSize(1094, 1000))
        font = QFont()
        font.setFamily(u"Nachlieli CLM")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #58626D;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gb_1 = QGroupBox(self.centralwidget)
        self.gb_1.setObjectName(u"gb_1")
        self.gb_1.setGeometry(QRect(0, 0, 1101, 71))
        self.gb_1.setStyleSheet(u"border: transparent;\n"
"background-color: rgb(69, 179, 157);")
        self.push_Mes_1 = QPushButton(self.gb_1)
        self.push_Mes_1.setObjectName(u"push_Mes_1")
        self.push_Mes_1.setGeometry(QRect(690, 10, 75, 51))
        font1 = QFont()
        font1.setPointSize(18)
        self.push_Mes_1.setFont(font1)
        self.push_Mes_1.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Sem_1 = QPushButton(self.gb_1)
        self.push_Sem_1.setObjectName(u"push_Sem_1")
        self.push_Sem_1.setGeometry(QRect(610, 10, 75, 51))
        self.push_Sem_1.setFont(font1)
        self.push_Sem_1.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Dia_1 = QPushButton(self.gb_1)
        self.push_Dia_1.setObjectName(u"push_Dia_1")
        self.push_Dia_1.setGeometry(QRect(530, 10, 75, 51))
        self.push_Dia_1.setFont(font1)
        self.push_Dia_1.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Act_1 = QPushButton(self.gb_1)
        self.push_Act_1.setObjectName(u"push_Act_1")
        self.push_Act_1.setGeometry(QRect(10, 10, 261, 51))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light")
        font2.setPointSize(20)
        self.push_Act_1.setFont(font2)
        self.push_Act_1.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #334CFF;\n"
"border-radius: 25px;")
        self.push_reloj_1 = QPushButton(self.gb_1)
        self.push_reloj_1.setObjectName(u"push_reloj_1")
        self.push_reloj_1.setGeometry(QRect(770, 10, 75, 51))
        self.push_reloj_1.setFont(font1)
        self.push_reloj_1.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Config_1 = QPushButton(self.gb_1)
        self.push_Config_1.setObjectName(u"push_Config_1")
        self.push_Config_1.setGeometry(QRect(850, 10, 75, 51))
        self.push_Config_1.setFont(font1)
        self.push_Config_1.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Resta_1 = QPushButton(self.gb_1)
        self.push_Resta_1.setObjectName(u"push_Resta_1")
        self.push_Resta_1.setGeometry(QRect(930, 10, 75, 51))
        self.push_Resta_1.setFont(font1)
        self.push_Resta_1.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_suma_1 = QPushButton(self.gb_1)
        self.push_suma_1.setObjectName(u"push_suma_1")
        self.push_suma_1.setGeometry(QRect(1010, 10, 75, 51))
        self.push_suma_1.setFont(font1)
        self.push_suma_1.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_1 = QLabel(self.gb_1)
        self.label_tiempo_1.setObjectName(u"label_tiempo_1")
        self.label_tiempo_1.setGeometry(QRect(280, 10, 241, 51))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light")
        font3.setPointSize(32)
        self.label_tiempo_1.setFont(font3)
        self.label_tiempo_1.setStyleSheet(u"background: transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_1.setAlignment(Qt.AlignCenter)
        self.label_barra_1 = QLabel(self.gb_1)
        self.label_barra_1.setObjectName(u"label_barra_1")
        self.label_barra_1.setGeometry(QRect(280, 10, 211, 51))
        self.label_barra_1.setFont(font3)
        self.label_barra_1.setStyleSheet(u"background-color: green;\n"
"border-radius: 25px;\n"
"border: transparent;\n"
"")
        self.label_barra_1.setAlignment(Qt.AlignCenter)
        self.label_fondo_1 = QLabel(self.gb_1)
        self.label_fondo_1.setObjectName(u"label_fondo_1")
        self.label_fondo_1.setGeometry(QRect(280, 10, 241, 51))
        self.label_fondo_1.setFont(font3)
        self.label_fondo_1.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #FFFFFF;")
        self.label_fondo_1.setAlignment(Qt.AlignCenter)
        self.label_fondo_1.raise_()
        self.label_barra_1.raise_()
        self.push_Mes_1.raise_()
        self.push_Sem_1.raise_()
        self.push_Dia_1.raise_()
        self.push_Act_1.raise_()
        self.push_reloj_1.raise_()
        self.push_Config_1.raise_()
        self.push_Resta_1.raise_()
        self.push_suma_1.raise_()
        self.label_tiempo_1.raise_()
        self.gb_2 = QGroupBox(self.centralwidget)
        self.gb_2.setObjectName(u"gb_2")
        self.gb_2.setGeometry(QRect(0, 70, 1101, 71))
        self.gb_2.setStyleSheet(u"border: transparent;\n"
"background-color: rgb(205,92,92);")
        self.push_Mes_2 = QPushButton(self.gb_2)
        self.push_Mes_2.setObjectName(u"push_Mes_2")
        self.push_Mes_2.setGeometry(QRect(690, 10, 75, 51))
        self.push_Mes_2.setFont(font1)
        self.push_Mes_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Sem_2 = QPushButton(self.gb_2)
        self.push_Sem_2.setObjectName(u"push_Sem_2")
        self.push_Sem_2.setGeometry(QRect(610, 10, 75, 51))
        self.push_Sem_2.setFont(font1)
        self.push_Sem_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Dia_2 = QPushButton(self.gb_2)
        self.push_Dia_2.setObjectName(u"push_Dia_2")
        self.push_Dia_2.setGeometry(QRect(530, 10, 75, 51))
        self.push_Dia_2.setFont(font1)
        self.push_Dia_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Act_2 = QPushButton(self.gb_2)
        self.push_Act_2.setObjectName(u"push_Act_2")
        self.push_Act_2.setGeometry(QRect(10, 10, 261, 51))
        self.push_Act_2.setFont(font2)
        self.push_Act_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #334CFF;\n"
"border-radius: 25px;")
        self.push_Config_2 = QPushButton(self.gb_2)
        self.push_Config_2.setObjectName(u"push_Config_2")
        self.push_Config_2.setGeometry(QRect(850, 10, 75, 51))
        self.push_Config_2.setFont(font1)
        self.push_Config_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_reloj_2 = QPushButton(self.gb_2)
        self.push_reloj_2.setObjectName(u"push_reloj_2")
        self.push_reloj_2.setGeometry(QRect(770, 10, 75, 51))
        self.push_reloj_2.setFont(font1)
        self.push_reloj_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Resta_2 = QPushButton(self.gb_2)
        self.push_Resta_2.setObjectName(u"push_Resta_2")
        self.push_Resta_2.setGeometry(QRect(930, 10, 75, 51))
        self.push_Resta_2.setFont(font1)
        self.push_Resta_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_suma_2 = QPushButton(self.gb_2)
        self.push_suma_2.setObjectName(u"push_suma_2")
        self.push_suma_2.setGeometry(QRect(1010, 10, 75, 51))
        self.push_suma_2.setFont(font1)
        self.push_suma_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_2 = QLabel(self.gb_2)
        self.label_tiempo_2.setObjectName(u"label_tiempo_2")
        self.label_tiempo_2.setGeometry(QRect(280, 10, 241, 51))
        self.label_tiempo_2.setFont(font3)
        self.label_tiempo_2.setStyleSheet(u"background: transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_2.setAlignment(Qt.AlignCenter)
        self.label_barra_2 = QLabel(self.gb_2)
        self.label_barra_2.setObjectName(u"label_barra_2")
        self.label_barra_2.setGeometry(QRect(280, 10, 211, 51))
        self.label_barra_2.setFont(font3)
        self.label_barra_2.setStyleSheet(u"background-color: green;\n"
"border-radius: 25px;\n"
"border: transparent;\n"
"")
        self.label_barra_2.setAlignment(Qt.AlignCenter)
        self.label_fondo_2 = QLabel(self.gb_2)
        self.label_fondo_2.setObjectName(u"label_fondo_2")
        self.label_fondo_2.setGeometry(QRect(280, 10, 241, 51))
        self.label_fondo_2.setFont(font3)
        self.label_fondo_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #FFFFFF;")
        self.label_fondo_2.setAlignment(Qt.AlignCenter)
        self.label_fondo_2.raise_()
        self.label_barra_2.raise_()
        self.push_Mes_2.raise_()
        self.push_Sem_2.raise_()
        self.push_Dia_2.raise_()
        self.push_Act_2.raise_()
        self.push_Config_2.raise_()
        self.push_reloj_2.raise_()
        self.push_Resta_2.raise_()
        self.push_suma_2.raise_()
        self.label_tiempo_2.raise_()
        self.gb_4 = QGroupBox(self.centralwidget)
        self.gb_4.setObjectName(u"gb_4")
        self.gb_4.setGeometry(QRect(0, 210, 1101, 71))
        self.gb_4.setStyleSheet(u"background-color: #566573;\n"
"border: transparent;\n"
"\n"
"")
        self.push_Mes_4 = QPushButton(self.gb_4)
        self.push_Mes_4.setObjectName(u"push_Mes_4")
        self.push_Mes_4.setGeometry(QRect(690, 10, 75, 51))
        self.push_Mes_4.setFont(font1)
        self.push_Mes_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Sem_4 = QPushButton(self.gb_4)
        self.push_Sem_4.setObjectName(u"push_Sem_4")
        self.push_Sem_4.setGeometry(QRect(610, 10, 75, 51))
        self.push_Sem_4.setFont(font1)
        self.push_Sem_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Dia_4 = QPushButton(self.gb_4)
        self.push_Dia_4.setObjectName(u"push_Dia_4")
        self.push_Dia_4.setGeometry(QRect(530, 10, 75, 51))
        self.push_Dia_4.setFont(font1)
        self.push_Dia_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Act_4 = QPushButton(self.gb_4)
        self.push_Act_4.setObjectName(u"push_Act_4")
        self.push_Act_4.setGeometry(QRect(10, 10, 261, 51))
        self.push_Act_4.setFont(font2)
        self.push_Act_4.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #334CFF;\n"
"border-radius: 25px;")
        self.push_Config_4 = QPushButton(self.gb_4)
        self.push_Config_4.setObjectName(u"push_Config_4")
        self.push_Config_4.setGeometry(QRect(850, 10, 75, 51))
        self.push_Config_4.setFont(font1)
        self.push_Config_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_reloj_4 = QPushButton(self.gb_4)
        self.push_reloj_4.setObjectName(u"push_reloj_4")
        self.push_reloj_4.setGeometry(QRect(770, 10, 75, 51))
        self.push_reloj_4.setFont(font1)
        self.push_reloj_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Resta_4 = QPushButton(self.gb_4)
        self.push_Resta_4.setObjectName(u"push_Resta_4")
        self.push_Resta_4.setGeometry(QRect(930, 10, 75, 51))
        self.push_Resta_4.setFont(font1)
        self.push_Resta_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_suma_4 = QPushButton(self.gb_4)
        self.push_suma_4.setObjectName(u"push_suma_4")
        self.push_suma_4.setGeometry(QRect(1010, 10, 75, 51))
        self.push_suma_4.setFont(font1)
        self.push_suma_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_4 = QLabel(self.gb_4)
        self.label_tiempo_4.setObjectName(u"label_tiempo_4")
        self.label_tiempo_4.setGeometry(QRect(280, 10, 241, 51))
        self.label_tiempo_4.setFont(font3)
        self.label_tiempo_4.setStyleSheet(u"background: transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_4.setAlignment(Qt.AlignCenter)
        self.label_barra_4 = QLabel(self.gb_4)
        self.label_barra_4.setObjectName(u"label_barra_4")
        self.label_barra_4.setGeometry(QRect(280, 10, 211, 51))
        self.label_barra_4.setFont(font3)
        self.label_barra_4.setStyleSheet(u"background-color: green;\n"
"border-radius: 25px;\n"
"border: transparent;\n"
"")
        self.label_barra_4.setAlignment(Qt.AlignCenter)
        self.label_fondo_4 = QLabel(self.gb_4)
        self.label_fondo_4.setObjectName(u"label_fondo_4")
        self.label_fondo_4.setGeometry(QRect(280, 10, 241, 51))
        self.label_fondo_4.setFont(font3)
        self.label_fondo_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #FFFFFF;")
        self.label_fondo_4.setAlignment(Qt.AlignCenter)
        self.label_fondo_4.raise_()
        self.label_barra_4.raise_()
        self.push_Mes_4.raise_()
        self.push_Sem_4.raise_()
        self.push_Dia_4.raise_()
        self.push_Act_4.raise_()
        self.push_Config_4.raise_()
        self.push_reloj_4.raise_()
        self.push_Resta_4.raise_()
        self.push_suma_4.raise_()
        self.label_tiempo_4.raise_()
        self.gb_3 = QGroupBox(self.centralwidget)
        self.gb_3.setObjectName(u"gb_3")
        self.gb_3.setGeometry(QRect(0, 140, 1101, 71))
        self.gb_3.setStyleSheet(u"background-color: #566573;\n"
"border: transparent;\n"
"\n"
"")
        self.push_Mes_3 = QPushButton(self.gb_3)
        self.push_Mes_3.setObjectName(u"push_Mes_3")
        self.push_Mes_3.setGeometry(QRect(690, 10, 75, 51))
        self.push_Mes_3.setFont(font1)
        self.push_Mes_3.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Sem_3 = QPushButton(self.gb_3)
        self.push_Sem_3.setObjectName(u"push_Sem_3")
        self.push_Sem_3.setGeometry(QRect(610, 10, 75, 51))
        self.push_Sem_3.setFont(font1)
        self.push_Sem_3.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Dia_3 = QPushButton(self.gb_3)
        self.push_Dia_3.setObjectName(u"push_Dia_3")
        self.push_Dia_3.setGeometry(QRect(530, 10, 75, 51))
        self.push_Dia_3.setFont(font1)
        self.push_Dia_3.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Act_3 = QPushButton(self.gb_3)
        self.push_Act_3.setObjectName(u"push_Act_3")
        self.push_Act_3.setGeometry(QRect(10, 10, 261, 51))
        self.push_Act_3.setFont(font2)
        self.push_Act_3.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #334CFF;\n"
"border-radius: 25px;")
        self.push_reloj_3 = QPushButton(self.gb_3)
        self.push_reloj_3.setObjectName(u"push_reloj_3")
        self.push_reloj_3.setGeometry(QRect(770, 10, 75, 51))
        self.push_reloj_3.setFont(font1)
        self.push_reloj_3.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Config_3 = QPushButton(self.gb_3)
        self.push_Config_3.setObjectName(u"push_Config_3")
        self.push_Config_3.setGeometry(QRect(850, 10, 75, 51))
        self.push_Config_3.setFont(font1)
        self.push_Config_3.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Resta_3 = QPushButton(self.gb_3)
        self.push_Resta_3.setObjectName(u"push_Resta_3")
        self.push_Resta_3.setGeometry(QRect(930, 10, 75, 51))
        self.push_Resta_3.setFont(font1)
        self.push_Resta_3.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_suma_3 = QPushButton(self.gb_3)
        self.push_suma_3.setObjectName(u"push_suma_3")
        self.push_suma_3.setGeometry(QRect(1010, 10, 75, 51))
        self.push_suma_3.setFont(font1)
        self.push_suma_3.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_3 = QLabel(self.gb_3)
        self.label_tiempo_3.setObjectName(u"label_tiempo_3")
        self.label_tiempo_3.setGeometry(QRect(280, 10, 241, 51))
        self.label_tiempo_3.setFont(font3)
        self.label_tiempo_3.setStyleSheet(u"background: transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_3.setAlignment(Qt.AlignCenter)
        self.label_barra_3 = QLabel(self.gb_3)
        self.label_barra_3.setObjectName(u"label_barra_3")
        self.label_barra_3.setGeometry(QRect(280, 10, 211, 51))
        self.label_barra_3.setFont(font3)
        self.label_barra_3.setStyleSheet(u"background-color: green;\n"
"border-radius: 25px;\n"
"border: transparent;\n"
"")
        self.label_barra_3.setAlignment(Qt.AlignCenter)
        self.label_fondo_3 = QLabel(self.gb_3)
        self.label_fondo_3.setObjectName(u"label_fondo_3")
        self.label_fondo_3.setGeometry(QRect(280, 10, 241, 51))
        self.label_fondo_3.setFont(font3)
        self.label_fondo_3.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #FFFFFF;")
        self.label_fondo_3.setAlignment(Qt.AlignCenter)
        self.label_fondo_3.raise_()
        self.label_barra_3.raise_()
        self.label_tiempo_3.raise_()
        self.push_Mes_3.raise_()
        self.push_Sem_3.raise_()
        self.push_Dia_3.raise_()
        self.push_Act_3.raise_()
        self.push_reloj_3.raise_()
        self.push_Config_3.raise_()
        self.push_Resta_3.raise_()
        self.push_suma_3.raise_()
        self.gb_6 = QGroupBox(self.centralwidget)
        self.gb_6.setObjectName(u"gb_6")
        self.gb_6.setGeometry(QRect(0, 350, 1101, 71))
        self.gb_6.setStyleSheet(u"background-color: #566573;\n"
"border: transparent;\n"
"\n"
"")
        self.push_Mes_6 = QPushButton(self.gb_6)
        self.push_Mes_6.setObjectName(u"push_Mes_6")
        self.push_Mes_6.setGeometry(QRect(690, 10, 75, 51))
        self.push_Mes_6.setFont(font1)
        self.push_Mes_6.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Sem_6 = QPushButton(self.gb_6)
        self.push_Sem_6.setObjectName(u"push_Sem_6")
        self.push_Sem_6.setGeometry(QRect(610, 10, 75, 51))
        self.push_Sem_6.setFont(font1)
        self.push_Sem_6.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Dia_6 = QPushButton(self.gb_6)
        self.push_Dia_6.setObjectName(u"push_Dia_6")
        self.push_Dia_6.setGeometry(QRect(530, 10, 75, 51))
        self.push_Dia_6.setFont(font1)
        self.push_Dia_6.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Act_6 = QPushButton(self.gb_6)
        self.push_Act_6.setObjectName(u"push_Act_6")
        self.push_Act_6.setGeometry(QRect(10, 10, 261, 51))
        self.push_Act_6.setFont(font2)
        self.push_Act_6.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #334CFF;\n"
"border-radius: 25px;")
        self.push_Config_6 = QPushButton(self.gb_6)
        self.push_Config_6.setObjectName(u"push_Config_6")
        self.push_Config_6.setGeometry(QRect(850, 10, 75, 51))
        self.push_Config_6.setFont(font1)
        self.push_Config_6.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_reloj_6 = QPushButton(self.gb_6)
        self.push_reloj_6.setObjectName(u"push_reloj_6")
        self.push_reloj_6.setGeometry(QRect(770, 10, 75, 51))
        self.push_reloj_6.setFont(font1)
        self.push_reloj_6.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Resta_6 = QPushButton(self.gb_6)
        self.push_Resta_6.setObjectName(u"push_Resta_6")
        self.push_Resta_6.setGeometry(QRect(930, 10, 75, 51))
        self.push_Resta_6.setFont(font1)
        self.push_Resta_6.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_suma_6 = QPushButton(self.gb_6)
        self.push_suma_6.setObjectName(u"push_suma_6")
        self.push_suma_6.setGeometry(QRect(1010, 10, 75, 51))
        self.push_suma_6.setFont(font1)
        self.push_suma_6.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_6 = QLabel(self.gb_6)
        self.label_tiempo_6.setObjectName(u"label_tiempo_6")
        self.label_tiempo_6.setGeometry(QRect(280, 10, 241, 51))
        self.label_tiempo_6.setFont(font3)
        self.label_tiempo_6.setStyleSheet(u"background: transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_6.setAlignment(Qt.AlignCenter)
        self.label_barra_6 = QLabel(self.gb_6)
        self.label_barra_6.setObjectName(u"label_barra_6")
        self.label_barra_6.setGeometry(QRect(280, 10, 211, 51))
        self.label_barra_6.setFont(font3)
        self.label_barra_6.setStyleSheet(u"background-color: green;\n"
"border-radius: 25px;\n"
"border: transparent;\n"
"")
        self.label_barra_6.setAlignment(Qt.AlignCenter)
        self.label_fondo_6 = QLabel(self.gb_6)
        self.label_fondo_6.setObjectName(u"label_fondo_6")
        self.label_fondo_6.setGeometry(QRect(280, 10, 241, 51))
        self.label_fondo_6.setFont(font3)
        self.label_fondo_6.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #FFFFFF;")
        self.label_fondo_6.setAlignment(Qt.AlignCenter)
        self.label_fondo_6.raise_()
        self.label_barra_6.raise_()
        self.push_Mes_6.raise_()
        self.push_Sem_6.raise_()
        self.push_Dia_6.raise_()
        self.push_Act_6.raise_()
        self.push_Config_6.raise_()
        self.push_reloj_6.raise_()
        self.push_Resta_6.raise_()
        self.push_suma_6.raise_()
        self.label_tiempo_6.raise_()
        self.gb_5 = QGroupBox(self.centralwidget)
        self.gb_5.setObjectName(u"gb_5")
        self.gb_5.setGeometry(QRect(0, 280, 1101, 71))
        self.gb_5.setStyleSheet(u"background-color: #566573;\n"
"border: transparent;\n"
"\n"
"")
        self.push_Mes_5 = QPushButton(self.gb_5)
        self.push_Mes_5.setObjectName(u"push_Mes_5")
        self.push_Mes_5.setGeometry(QRect(690, 10, 75, 51))
        self.push_Mes_5.setFont(font1)
        self.push_Mes_5.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Sem_5 = QPushButton(self.gb_5)
        self.push_Sem_5.setObjectName(u"push_Sem_5")
        self.push_Sem_5.setGeometry(QRect(610, 10, 75, 51))
        self.push_Sem_5.setFont(font1)
        self.push_Sem_5.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Dia_5 = QPushButton(self.gb_5)
        self.push_Dia_5.setObjectName(u"push_Dia_5")
        self.push_Dia_5.setGeometry(QRect(530, 10, 75, 51))
        self.push_Dia_5.setFont(font1)
        self.push_Dia_5.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Act_5 = QPushButton(self.gb_5)
        self.push_Act_5.setObjectName(u"push_Act_5")
        self.push_Act_5.setGeometry(QRect(10, 10, 261, 51))
        self.push_Act_5.setFont(font2)
        self.push_Act_5.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #334CFF;\n"
"border-radius: 25px;")
        self.push_reloj_5 = QPushButton(self.gb_5)
        self.push_reloj_5.setObjectName(u"push_reloj_5")
        self.push_reloj_5.setGeometry(QRect(770, 10, 75, 51))
        self.push_reloj_5.setFont(font1)
        self.push_reloj_5.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Config_5 = QPushButton(self.gb_5)
        self.push_Config_5.setObjectName(u"push_Config_5")
        self.push_Config_5.setGeometry(QRect(850, 10, 75, 51))
        self.push_Config_5.setFont(font1)
        self.push_Config_5.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Resta_5 = QPushButton(self.gb_5)
        self.push_Resta_5.setObjectName(u"push_Resta_5")
        self.push_Resta_5.setGeometry(QRect(930, 10, 75, 51))
        self.push_Resta_5.setFont(font1)
        self.push_Resta_5.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_suma_5 = QPushButton(self.gb_5)
        self.push_suma_5.setObjectName(u"push_suma_5")
        self.push_suma_5.setGeometry(QRect(1010, 10, 75, 51))
        self.push_suma_5.setFont(font1)
        self.push_suma_5.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_5 = QLabel(self.gb_5)
        self.label_tiempo_5.setObjectName(u"label_tiempo_5")
        self.label_tiempo_5.setGeometry(QRect(280, 10, 241, 51))
        self.label_tiempo_5.setFont(font3)
        self.label_tiempo_5.setStyleSheet(u"background: transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_5.setAlignment(Qt.AlignCenter)
        self.label_barra_5 = QLabel(self.gb_5)
        self.label_barra_5.setObjectName(u"label_barra_5")
        self.label_barra_5.setGeometry(QRect(280, 10, 211, 51))
        self.label_barra_5.setFont(font3)
        self.label_barra_5.setStyleSheet(u"background-color: green;\n"
"border-radius: 25px;\n"
"border: transparent;\n"
"")
        self.label_barra_5.setAlignment(Qt.AlignCenter)
        self.label_fondo_5 = QLabel(self.gb_5)
        self.label_fondo_5.setObjectName(u"label_fondo_5")
        self.label_fondo_5.setGeometry(QRect(280, 10, 241, 51))
        self.label_fondo_5.setFont(font3)
        self.label_fondo_5.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #FFFFFF;")
        self.label_fondo_5.setAlignment(Qt.AlignCenter)
        self.label_fondo_5.raise_()
        self.label_barra_5.raise_()
        self.push_Mes_5.raise_()
        self.push_Sem_5.raise_()
        self.push_Dia_5.raise_()
        self.push_Act_5.raise_()
        self.push_reloj_5.raise_()
        self.push_Config_5.raise_()
        self.push_Resta_5.raise_()
        self.push_suma_5.raise_()
        self.label_tiempo_5.raise_()
        self.gb_8 = QGroupBox(self.centralwidget)
        self.gb_8.setObjectName(u"gb_8")
        self.gb_8.setGeometry(QRect(0, 490, 1101, 71))
        self.gb_8.setStyleSheet(u"background-color: #566573;\n"
"border: transparent;\n"
"\n"
"")
        self.push_Mes_8 = QPushButton(self.gb_8)
        self.push_Mes_8.setObjectName(u"push_Mes_8")
        self.push_Mes_8.setGeometry(QRect(690, 10, 75, 51))
        self.push_Mes_8.setFont(font1)
        self.push_Mes_8.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Sem_8 = QPushButton(self.gb_8)
        self.push_Sem_8.setObjectName(u"push_Sem_8")
        self.push_Sem_8.setGeometry(QRect(610, 10, 75, 51))
        self.push_Sem_8.setFont(font1)
        self.push_Sem_8.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Dia_8 = QPushButton(self.gb_8)
        self.push_Dia_8.setObjectName(u"push_Dia_8")
        self.push_Dia_8.setGeometry(QRect(530, 10, 75, 51))
        self.push_Dia_8.setFont(font1)
        self.push_Dia_8.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Act_8 = QPushButton(self.gb_8)
        self.push_Act_8.setObjectName(u"push_Act_8")
        self.push_Act_8.setGeometry(QRect(10, 10, 261, 51))
        self.push_Act_8.setFont(font2)
        self.push_Act_8.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #334CFF;\n"
"border-radius: 25px;")
        self.push_Config_8 = QPushButton(self.gb_8)
        self.push_Config_8.setObjectName(u"push_Config_8")
        self.push_Config_8.setGeometry(QRect(850, 10, 75, 51))
        self.push_Config_8.setFont(font1)
        self.push_Config_8.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_reloj_8 = QPushButton(self.gb_8)
        self.push_reloj_8.setObjectName(u"push_reloj_8")
        self.push_reloj_8.setGeometry(QRect(770, 10, 75, 51))
        self.push_reloj_8.setFont(font1)
        self.push_reloj_8.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Resta_8 = QPushButton(self.gb_8)
        self.push_Resta_8.setObjectName(u"push_Resta_8")
        self.push_Resta_8.setGeometry(QRect(930, 10, 75, 51))
        self.push_Resta_8.setFont(font1)
        self.push_Resta_8.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_suma_8 = QPushButton(self.gb_8)
        self.push_suma_8.setObjectName(u"push_suma_8")
        self.push_suma_8.setGeometry(QRect(1010, 10, 75, 51))
        self.push_suma_8.setFont(font1)
        self.push_suma_8.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_8 = QLabel(self.gb_8)
        self.label_tiempo_8.setObjectName(u"label_tiempo_8")
        self.label_tiempo_8.setGeometry(QRect(280, 10, 241, 51))
        self.label_tiempo_8.setFont(font3)
        self.label_tiempo_8.setStyleSheet(u"background: transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_8.setAlignment(Qt.AlignCenter)
        self.label_barra_8 = QLabel(self.gb_8)
        self.label_barra_8.setObjectName(u"label_barra_8")
        self.label_barra_8.setGeometry(QRect(280, 10, 211, 51))
        self.label_barra_8.setFont(font3)
        self.label_barra_8.setStyleSheet(u"background-color: green;\n"
"border-radius: 25px;\n"
"border: transparent;\n"
"")
        self.label_barra_8.setAlignment(Qt.AlignCenter)
        self.label_fondo_8 = QLabel(self.gb_8)
        self.label_fondo_8.setObjectName(u"label_fondo_8")
        self.label_fondo_8.setGeometry(QRect(280, 10, 241, 51))
        self.label_fondo_8.setFont(font3)
        self.label_fondo_8.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #FFFFFF;")
        self.label_fondo_8.setAlignment(Qt.AlignCenter)
        self.label_fondo_8.raise_()
        self.label_barra_8.raise_()
        self.push_Mes_8.raise_()
        self.push_Sem_8.raise_()
        self.push_Dia_8.raise_()
        self.push_Act_8.raise_()
        self.push_Config_8.raise_()
        self.push_reloj_8.raise_()
        self.push_Resta_8.raise_()
        self.push_suma_8.raise_()
        self.label_tiempo_8.raise_()
        self.gb_7 = QGroupBox(self.centralwidget)
        self.gb_7.setObjectName(u"gb_7")
        self.gb_7.setGeometry(QRect(0, 420, 1101, 71))
        self.gb_7.setStyleSheet(u"background-color: #566573;\n"
"border: transparent;\n"
"\n"
"")
        self.push_Mes_7 = QPushButton(self.gb_7)
        self.push_Mes_7.setObjectName(u"push_Mes_7")
        self.push_Mes_7.setGeometry(QRect(690, 10, 75, 51))
        self.push_Mes_7.setFont(font1)
        self.push_Mes_7.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Sem_7 = QPushButton(self.gb_7)
        self.push_Sem_7.setObjectName(u"push_Sem_7")
        self.push_Sem_7.setGeometry(QRect(610, 10, 75, 51))
        self.push_Sem_7.setFont(font1)
        self.push_Sem_7.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Dia_7 = QPushButton(self.gb_7)
        self.push_Dia_7.setObjectName(u"push_Dia_7")
        self.push_Dia_7.setGeometry(QRect(530, 10, 75, 51))
        self.push_Dia_7.setFont(font1)
        self.push_Dia_7.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Act_7 = QPushButton(self.gb_7)
        self.push_Act_7.setObjectName(u"push_Act_7")
        self.push_Act_7.setGeometry(QRect(10, 10, 261, 51))
        self.push_Act_7.setFont(font2)
        self.push_Act_7.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #334CFF;\n"
"border-radius: 25px;")
        self.push_reloj_7 = QPushButton(self.gb_7)
        self.push_reloj_7.setObjectName(u"push_reloj_7")
        self.push_reloj_7.setGeometry(QRect(770, 10, 75, 51))
        self.push_reloj_7.setFont(font1)
        self.push_reloj_7.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Config_7 = QPushButton(self.gb_7)
        self.push_Config_7.setObjectName(u"push_Config_7")
        self.push_Config_7.setGeometry(QRect(850, 10, 75, 51))
        self.push_Config_7.setFont(font1)
        self.push_Config_7.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Resta_7 = QPushButton(self.gb_7)
        self.push_Resta_7.setObjectName(u"push_Resta_7")
        self.push_Resta_7.setGeometry(QRect(930, 10, 75, 51))
        self.push_Resta_7.setFont(font1)
        self.push_Resta_7.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_suma_7 = QPushButton(self.gb_7)
        self.push_suma_7.setObjectName(u"push_suma_7")
        self.push_suma_7.setGeometry(QRect(1010, 10, 75, 51))
        self.push_suma_7.setFont(font1)
        self.push_suma_7.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_7 = QLabel(self.gb_7)
        self.label_tiempo_7.setObjectName(u"label_tiempo_7")
        self.label_tiempo_7.setGeometry(QRect(280, 10, 241, 51))
        self.label_tiempo_7.setFont(font3)
        self.label_tiempo_7.setStyleSheet(u"background: transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_7.setAlignment(Qt.AlignCenter)
        self.label_barra_7 = QLabel(self.gb_7)
        self.label_barra_7.setObjectName(u"label_barra_7")
        self.label_barra_7.setGeometry(QRect(280, 10, 211, 51))
        self.label_barra_7.setFont(font3)
        self.label_barra_7.setStyleSheet(u"background-color: green;\n"
"border-radius: 25px;\n"
"border: transparent;\n"
"")
        self.label_barra_7.setAlignment(Qt.AlignCenter)
        self.label_fondo_7 = QLabel(self.gb_7)
        self.label_fondo_7.setObjectName(u"label_fondo_7")
        self.label_fondo_7.setGeometry(QRect(280, 10, 241, 51))
        self.label_fondo_7.setFont(font3)
        self.label_fondo_7.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #FFFFFF;")
        self.label_fondo_7.setAlignment(Qt.AlignCenter)
        self.label_fondo_7.raise_()
        self.label_barra_7.raise_()
        self.push_Mes_7.raise_()
        self.push_Sem_7.raise_()
        self.push_Dia_7.raise_()
        self.push_Act_7.raise_()
        self.push_reloj_7.raise_()
        self.push_Config_7.raise_()
        self.push_Resta_7.raise_()
        self.push_suma_7.raise_()
        self.label_tiempo_7.raise_()
        self.gb_10 = QGroupBox(self.centralwidget)
        self.gb_10.setObjectName(u"gb_10")
        self.gb_10.setGeometry(QRect(0, 630, 1101, 71))
        self.gb_10.setStyleSheet(u"background-color: #566573;\n"
"border: transparent;\n"
"\n"
"")
        self.push_Mes_10 = QPushButton(self.gb_10)
        self.push_Mes_10.setObjectName(u"push_Mes_10")
        self.push_Mes_10.setGeometry(QRect(690, 10, 75, 51))
        self.push_Mes_10.setFont(font1)
        self.push_Mes_10.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Sem_10 = QPushButton(self.gb_10)
        self.push_Sem_10.setObjectName(u"push_Sem_10")
        self.push_Sem_10.setGeometry(QRect(610, 10, 75, 51))
        self.push_Sem_10.setFont(font1)
        self.push_Sem_10.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Dia_10 = QPushButton(self.gb_10)
        self.push_Dia_10.setObjectName(u"push_Dia_10")
        self.push_Dia_10.setGeometry(QRect(530, 10, 75, 51))
        self.push_Dia_10.setFont(font1)
        self.push_Dia_10.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Act_10 = QPushButton(self.gb_10)
        self.push_Act_10.setObjectName(u"push_Act_10")
        self.push_Act_10.setGeometry(QRect(10, 10, 261, 51))
        self.push_Act_10.setFont(font2)
        self.push_Act_10.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #334CFF;\n"
"border-radius: 25px;")
        self.push_Config_10 = QPushButton(self.gb_10)
        self.push_Config_10.setObjectName(u"push_Config_10")
        self.push_Config_10.setGeometry(QRect(850, 10, 75, 51))
        self.push_Config_10.setFont(font1)
        self.push_Config_10.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_reloj_10 = QPushButton(self.gb_10)
        self.push_reloj_10.setObjectName(u"push_reloj_10")
        self.push_reloj_10.setGeometry(QRect(770, 10, 75, 51))
        self.push_reloj_10.setFont(font1)
        self.push_reloj_10.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Resta_10 = QPushButton(self.gb_10)
        self.push_Resta_10.setObjectName(u"push_Resta_10")
        self.push_Resta_10.setGeometry(QRect(930, 10, 75, 51))
        self.push_Resta_10.setFont(font1)
        self.push_Resta_10.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_suma_10 = QPushButton(self.gb_10)
        self.push_suma_10.setObjectName(u"push_suma_10")
        self.push_suma_10.setGeometry(QRect(1010, 10, 75, 51))
        self.push_suma_10.setFont(font1)
        self.push_suma_10.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_10 = QLabel(self.gb_10)
        self.label_tiempo_10.setObjectName(u"label_tiempo_10")
        self.label_tiempo_10.setGeometry(QRect(280, 10, 241, 51))
        self.label_tiempo_10.setFont(font3)
        self.label_tiempo_10.setStyleSheet(u"background: transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_10.setAlignment(Qt.AlignCenter)
        self.label_barra_10 = QLabel(self.gb_10)
        self.label_barra_10.setObjectName(u"label_barra_10")
        self.label_barra_10.setGeometry(QRect(280, 10, 211, 51))
        self.label_barra_10.setFont(font3)
        self.label_barra_10.setStyleSheet(u"background-color: green;\n"
"border-radius: 25px;\n"
"border: transparent;\n"
"")
        self.label_barra_10.setAlignment(Qt.AlignCenter)
        self.label_fondo_10 = QLabel(self.gb_10)
        self.label_fondo_10.setObjectName(u"label_fondo_10")
        self.label_fondo_10.setGeometry(QRect(280, 10, 241, 51))
        self.label_fondo_10.setFont(font3)
        self.label_fondo_10.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #FFFFFF;")
        self.label_fondo_10.setAlignment(Qt.AlignCenter)
        self.label_fondo_10.raise_()
        self.label_barra_10.raise_()
        self.push_Mes_10.raise_()
        self.push_Sem_10.raise_()
        self.push_Dia_10.raise_()
        self.push_Act_10.raise_()
        self.push_Config_10.raise_()
        self.push_reloj_10.raise_()
        self.push_Resta_10.raise_()
        self.push_suma_10.raise_()
        self.label_tiempo_10.raise_()
        self.gb_9 = QGroupBox(self.centralwidget)
        self.gb_9.setObjectName(u"gb_9")
        self.gb_9.setGeometry(QRect(0, 560, 1101, 71))
        self.gb_9.setStyleSheet(u"background-color: #566573;\n"
"border: transparent;\n"
"\n"
"")
        self.push_Mes_9 = QPushButton(self.gb_9)
        self.push_Mes_9.setObjectName(u"push_Mes_9")
        self.push_Mes_9.setGeometry(QRect(690, 10, 75, 51))
        self.push_Mes_9.setFont(font1)
        self.push_Mes_9.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Sem_9 = QPushButton(self.gb_9)
        self.push_Sem_9.setObjectName(u"push_Sem_9")
        self.push_Sem_9.setGeometry(QRect(610, 10, 75, 51))
        self.push_Sem_9.setFont(font1)
        self.push_Sem_9.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Dia_9 = QPushButton(self.gb_9)
        self.push_Dia_9.setObjectName(u"push_Dia_9")
        self.push_Dia_9.setGeometry(QRect(530, 10, 75, 51))
        self.push_Dia_9.setFont(font1)
        self.push_Dia_9.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Act_9 = QPushButton(self.gb_9)
        self.push_Act_9.setObjectName(u"push_Act_9")
        self.push_Act_9.setGeometry(QRect(10, 10, 261, 51))
        self.push_Act_9.setFont(font2)
        self.push_Act_9.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #334CFF;\n"
"border-radius: 25px;")
        self.push_reloj_9 = QPushButton(self.gb_9)
        self.push_reloj_9.setObjectName(u"push_reloj_9")
        self.push_reloj_9.setGeometry(QRect(770, 10, 75, 51))
        self.push_reloj_9.setFont(font1)
        self.push_reloj_9.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Config_9 = QPushButton(self.gb_9)
        self.push_Config_9.setObjectName(u"push_Config_9")
        self.push_Config_9.setGeometry(QRect(850, 10, 75, 51))
        self.push_Config_9.setFont(font1)
        self.push_Config_9.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_Resta_9 = QPushButton(self.gb_9)
        self.push_Resta_9.setObjectName(u"push_Resta_9")
        self.push_Resta_9.setGeometry(QRect(930, 10, 75, 51))
        self.push_Resta_9.setFont(font1)
        self.push_Resta_9.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.push_suma_9 = QPushButton(self.gb_9)
        self.push_suma_9.setObjectName(u"push_suma_9")
        self.push_suma_9.setGeometry(QRect(1010, 10, 75, 51))
        self.push_suma_9.setFont(font1)
        self.push_suma_9.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_9 = QLabel(self.gb_9)
        self.label_tiempo_9.setObjectName(u"label_tiempo_9")
        self.label_tiempo_9.setGeometry(QRect(280, 10, 241, 51))
        self.label_tiempo_9.setFont(font3)
        self.label_tiempo_9.setStyleSheet(u"background: transparent;\n"
"border-radius: 25px;\n"
"border: 1px solid #334CFF;")
        self.label_tiempo_9.setAlignment(Qt.AlignCenter)
        self.label_barra_9 = QLabel(self.gb_9)
        self.label_barra_9.setObjectName(u"label_barra_9")
        self.label_barra_9.setGeometry(QRect(280, 10, 211, 51))
        self.label_barra_9.setFont(font3)
        self.label_barra_9.setStyleSheet(u"background-color: green;\n"
"border-radius: 25px;\n"
"border: transparent;\n"
"")
        self.label_barra_9.setAlignment(Qt.AlignCenter)
        self.label_fondo_9 = QLabel(self.gb_9)
        self.label_fondo_9.setObjectName(u"label_fondo_9")
        self.label_fondo_9.setGeometry(QRect(280, 10, 241, 51))
        self.label_fondo_9.setFont(font3)
        self.label_fondo_9.setStyleSheet(u"background-color: white;\n"
"border-radius: 25px;\n"
"border: 1px solid #FFFFFF;")
        self.label_fondo_9.setAlignment(Qt.AlignCenter)
        self.label_fondo_9.raise_()
        self.label_barra_9.raise_()
        self.push_Mes_9.raise_()
        self.push_Sem_9.raise_()
        self.push_Dia_9.raise_()
        self.push_Act_9.raise_()
        self.push_reloj_9.raise_()
        self.push_Config_9.raise_()
        self.push_Resta_9.raise_()
        self.push_suma_9.raise_()
        self.label_tiempo_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Temporizador", None))
        self.gb_1.setTitle("")
        self.push_Mes_1.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.push_Sem_1.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.push_Dia_1.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.push_Act_1.setText(QCoreApplication.translate("MainWindow", u"Programaci\u00f3n", None))
        self.push_reloj_1.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.push_Config_1.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.push_Resta_1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_suma_1.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_tiempo_1.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_barra_1.setText("")
        self.label_fondo_1.setText("")
        self.gb_2.setTitle("")
        self.push_Mes_2.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.push_Sem_2.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.push_Dia_2.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.push_Act_2.setText(QCoreApplication.translate("MainWindow", u"Programaci\u00f3n", None))
        self.push_Config_2.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.push_reloj_2.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.push_Resta_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_suma_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_tiempo_2.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_barra_2.setText("")
        self.label_fondo_2.setText("")
        self.gb_4.setTitle("")
        self.push_Mes_4.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.push_Sem_4.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.push_Dia_4.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.push_Act_4.setText(QCoreApplication.translate("MainWindow", u"Programaci\u00f3n", None))
        self.push_Config_4.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.push_reloj_4.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.push_Resta_4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_suma_4.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_tiempo_4.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_barra_4.setText("")
        self.label_fondo_4.setText("")
        self.gb_3.setTitle("")
        self.push_Mes_3.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.push_Sem_3.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.push_Dia_3.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.push_Act_3.setText(QCoreApplication.translate("MainWindow", u"Programaci\u00f3n", None))
        self.push_reloj_3.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.push_Config_3.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.push_Resta_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_suma_3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_tiempo_3.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_barra_3.setText("")
        self.label_fondo_3.setText("")
        self.gb_6.setTitle("")
        self.push_Mes_6.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.push_Sem_6.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.push_Dia_6.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.push_Act_6.setText(QCoreApplication.translate("MainWindow", u"Programaci\u00f3n", None))
        self.push_Config_6.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.push_reloj_6.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.push_Resta_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_suma_6.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_tiempo_6.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_barra_6.setText("")
        self.label_fondo_6.setText("")
        self.gb_5.setTitle("")
        self.push_Mes_5.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.push_Sem_5.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.push_Dia_5.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.push_Act_5.setText(QCoreApplication.translate("MainWindow", u"Programaci\u00f3n", None))
        self.push_reloj_5.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.push_Config_5.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.push_Resta_5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_suma_5.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_tiempo_5.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_barra_5.setText("")
        self.label_fondo_5.setText("")
        self.gb_8.setTitle("")
        self.push_Mes_8.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.push_Sem_8.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.push_Dia_8.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.push_Act_8.setText(QCoreApplication.translate("MainWindow", u"Programaci\u00f3n", None))
        self.push_Config_8.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.push_reloj_8.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.push_Resta_8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_suma_8.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_tiempo_8.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_barra_8.setText("")
        self.label_fondo_8.setText("")
        self.gb_7.setTitle("")
        self.push_Mes_7.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.push_Sem_7.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.push_Dia_7.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.push_Act_7.setText(QCoreApplication.translate("MainWindow", u"Programaci\u00f3n", None))
        self.push_reloj_7.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.push_Config_7.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.push_Resta_7.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_suma_7.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_tiempo_7.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_barra_7.setText("")
        self.label_fondo_7.setText("")
        self.gb_10.setTitle("")
        self.push_Mes_10.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.push_Sem_10.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.push_Dia_10.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.push_Act_10.setText(QCoreApplication.translate("MainWindow", u"Programaci\u00f3n", None))
        self.push_Config_10.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.push_reloj_10.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.push_Resta_10.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_suma_10.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_tiempo_10.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_barra_10.setText("")
        self.label_fondo_10.setText("")
        self.gb_9.setTitle("")
        self.push_Mes_9.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.push_Sem_9.setText(QCoreApplication.translate("MainWindow", u"Sem", None))
        self.push_Dia_9.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.push_Act_9.setText(QCoreApplication.translate("MainWindow", u"Programaci\u00f3n", None))
        self.push_reloj_9.setText(QCoreApplication.translate("MainWindow", u"Reloj", None))
        self.push_Config_9.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.push_Resta_9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.push_suma_9.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_tiempo_9.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_barra_9.setText("")
        self.label_fondo_9.setText("")
    # retranslateUi

