# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bate-faca.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#    QMetaObject, QObject, QPoint, QRect,
#    QSize, QTime, QUrl, Qt)
#from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#    QFont, QFontDatabase, QGradient, QIcon,
#    QImage, QKeySequence, QLinearGradient, QPainter,
#    QPalette, QPixmap, QRadialGradient, QTransform)
#from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGraphicsView,
#    QHBoxLayout, QLCDNumber, QLabel, QLineEdit,
#    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 391)
        self.frame_5 = QFrame(MainWindow)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(-20, -20, 877, 344))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lcd_bat_a = QLCDNumber(self.frame)
        self.lcd_bat_a.setObjectName(u"lcd_bat_a")

        self.verticalLayout.addWidget(self.lcd_bat_a)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lcd_bat_b = QLCDNumber(self.frame)
        self.lcd_bat_b.setObjectName(u"lcd_bat_b")

        self.verticalLayout.addWidget(self.lcd_bat_b)

        self.btn_adm = QPushButton(self.frame)
        self.btn_adm.setObjectName(u"btn_adm")
        self.btn_adm.setMaximumSize(QSize(250, 60))
        self.btn_adm.setMouseTracking(False)
        self.btn_adm.setIconSize(QSize(90, 90))

        self.verticalLayout.addWidget(self.btn_adm)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphicsView = QGraphicsView(self.frame_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setEnabled(True)
        self.graphicsView.setMaximumSize(QSize(500, 1000))

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(500, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.date_line = QLineEdit(self.frame_4)
        self.date_line.setObjectName(u"date_line")
        self.date_line.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.date_line)

        self.hour_line = QLineEdit(self.frame_4)
        self.hour_line.setObjectName(u"hour_line")
        self.hour_line.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.hour_line)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 20))
        self.frame_6.setMaximumSize(QSize(700, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 0, 191, 16))

        self.verticalLayout_3.addWidget(self.frame_6)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Helsten", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Batimento Lateral A</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Batimento Lateral B</span></p></body></html>", None))
        self.btn_adm.setText(QCoreApplication.translate("MainWindow", u"ADMIN", None))
        self.date_line.setText(QCoreApplication.translate("MainWindow", u"23/06/2023", None))
        self.hour_line.setText(QCoreApplication.translate("MainWindow", u"15:00", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#0000ff;\">Helsten</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Copyright Kerotanz Holders", None))
    # retranslateUi

