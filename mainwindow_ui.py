# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import mainwindow_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1306, 930)
        MainWindow.setMinimumSize(QSize(1306, 930))
        MainWindow.setMaximumSize(QSize(1306, 930))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/Image/windowico.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLabel#source, #division{\n"
"    color: #CBCBCB;\n"
"	border: 2px solid #3194D1;\n"
"	background: #FFFFFF\n"
"}\n"
"\n"
"QListWidget#listWidget{\n"
"	border: 2px solid #3194D1;\n"
"	background: #FFFFFF\n"
"}\n"
"\n"
"QListWidget::item:hover#listWidget{\n"
"	border: 2px solid #006363\n"
"}\n"
"\n"
"QListWidget::item:selected#listWidget{\n"
"	color:black;\n"
"	background:#60D6A7\n"
"}\n"
"\n"
"QTableWidget#tableWidget{\n"
"	border: 2px solid #3194D1;\n"
"}")
        self.file = QAction(MainWindow)
        self.file.setObjectName(u"file")
        font1 = QFont()
        self.file.setFont(font1)
        self.location = QAction(MainWindow)
        self.location.setObjectName(u"location")
        self.number = QAction(MainWindow)
        self.number.setObjectName(u"number")
        self.repetition = QAction(MainWindow)
        self.repetition.setObjectName(u"repetition")
        self.output = QAction(MainWindow)
        self.output.setObjectName(u"output")
        self.select = QAction(MainWindow)
        self.select.setObjectName(u"select")
        self.information = QAction(MainWindow)
        self.information.setObjectName(u"information")
        self.selects = QAction(MainWindow)
        self.selects.setObjectName(u"selects")
        self.clear = QAction(MainWindow)
        self.clear.setObjectName(u"clear")
        self.select_camera = QAction(MainWindow)
        self.select_camera.setObjectName(u"select_camera")
        self.close_camera = QAction(MainWindow)
        self.close_camera.setObjectName(u"close_camera")
        self.select_video = QAction(MainWindow)
        self.select_video.setObjectName(u"select_video")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1306, 900))
        self.centralwidget.setMaximumSize(QSize(1306, 900))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_1.setFont(font2)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.source = QLabel(self.centralwidget)
        self.source.setObjectName(u"source")
        self.source.setMinimumSize(QSize(640, 640))
        self.source.setMaximumSize(QSize(640, 640))
        self.source.setFont(font2)
        self.source.setStyleSheet(u"")
        self.source.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.source)

        self.division = QLabel(self.centralwidget)
        self.division.setObjectName(u"division")
        self.division.setMinimumSize(QSize(640, 640))
        self.division.setMaximumSize(QSize(640, 640))
        self.division.setFont(font2)
        self.division.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.division)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(10)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(12)
        self.tableWidget.setFont(font4)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setRowCount(0)

        self.verticalLayout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1306, 24))
        font5 = QFont()
        font5.setFamilies([u"Consolas"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.menubar.setFont(font5)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        font6 = QFont()
        font6.setFamilies([u"Consolas"])
        font6.setPointSize(10)
        font6.setBold(False)
        self.menu.setFont(font6)
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.select)
        self.menu.addAction(self.location)
        self.menu.addAction(self.number)
        self.menu.addSeparator()
        self.menu.addAction(self.selects)
        self.menu.addSeparator()
        self.menu.addAction(self.select_video)
        self.menu.addSeparator()
        self.menu.addAction(self.select_camera)
        self.menu.addAction(self.close_camera)
        self.menu.addSeparator()
        self.menu.addAction(self.clear)
        self.menu.addAction(self.repetition)
        self.menu.addAction(self.output)
        self.menu_2.addAction(self.information)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u8bc6\u522bDemo", None))
        self.file.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.location.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u5b9a\u4f4d", None))
        self.number.setText(QCoreApplication.translate("MainWindow", u"\u53f7\u7801\u63d0\u53d6", None))
        self.repetition.setText(QCoreApplication.translate("MainWindow", u"\u53bb\u91cd", None))
        self.output.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247", None))
        self.information.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f", None))
        self.selects.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.select_camera.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6444\u50cf\u5934", None))
        self.close_camera.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6444\u50cf\u5934", None))
        self.select_video.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u539f\u56fe", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u68c0\u6d4b\u56fe", None))
        self.source.setText(QCoreApplication.translate("MainWindow", u"SOURCE_IMAGE", None))
        self.division.setText(QCoreApplication.translate("MainWindow", u"DIVISION_IMAGE", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5165\u65f6\u95f4", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u53f7", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u8f66\u724c\u7c7b\u578b", None));
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

