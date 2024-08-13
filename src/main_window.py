# Main application window.

from PySide6.QtWidgets import ( QMenu, QMenuBar, QStatusBar, QWidget)
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QAction, QCursor)
from daily_attendance_table import Ui_Daily_Attendance_Table
from daily_attendance import Ui_Daily_Attendance_update
from daily_calender import Ui_Calender
from attendance_stats import Ui_Attendance_stats
from attendance_stats_visualization import Ui_Attendance_stats_visualization
from new_routine import Ui_New_Routine
from edit_routine import Ui_Edit_Routine



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 246)
        MainWindow.setStyleSheet(u"""/* Background color for QMainWindow */
                                    QMainWindow {
                                        background-color: rgb(163, 255, 137);
                                    }

                                    /* Styling for QMenuBar */
                                    QMenuBar {
                                        background-color: #4CAF50;
                                        color: white;
                                    }

                                    /* Styling for QMenuBar items */
                                    QMenuBar::item {
                                        background-color: #4CAF50;
                                        color: white;
                                        padding: 10px 15px;
                                    }

                                    /* Styling for selected QMenuBar items */
                                    QMenuBar::item:selected {
                                        background-color: #558b2f;
                                    }

                                    /* Styling for QMenu items */
                                    QMenu::item {
                                        background-color: #4CAF50;
                                        color: white;
                                        padding: 4px 20px;
                                    }

                                    /* Styling for selected QMenu items */
                                    QMenu::item:selected {
                                        background-color: #558b2f;
                                    }
                                    """) # Styles for QMainWindow and menu
        
        # Create actions and connect them to methods
        self.actionASV = QAction(MainWindow)
        self.actionASV.setObjectName(u"actionASV")
        self.actionASV.triggered.connect(self.get_monthly_attendance_statistic)

        self.actionAV = QAction(MainWindow)
        self.actionAV.setObjectName(u"actionAV")
        self.actionAV.triggered.connect(self.get_monthly_attendance_table)

        self.actionDAILY_ATTENDANCE = QAction(MainWindow)
        self.actionDAILY_ATTENDANCE.setObjectName(u"actionDAILY_ATTENDANCE")
        self.actionDAILY_ATTENDANCE.triggered.connect(
            self.daily_attendance_table)

        self.actionNEW_ROUTINE = QAction(MainWindow)
        self.actionNEW_ROUTINE.setObjectName(u"actionNEW_ROUTINE")
        self.actionNEW_ROUTINE.triggered.connect(self.add_new_routine)

        self.actionEDIT_ROUTINE = QAction(MainWindow)
        self.actionEDIT_ROUTINE.setObjectName(u"actionEDIT_ROUTINE")
        self.actionEDIT_ROUTINE.triggered.connect(self.edit_routine)

        self.actionEDIT_DATABASE = QAction(MainWindow)
        self.actionEDIT_DATABASE.setObjectName(u"actionEDIT_DATABASE")
        self.actionEDIT_DATABASE.triggered.connect(self.add_edit_database)

        self.actionHOME = QAction(MainWindow)
        self.actionHOME.setObjectName(u"actionHOME")
        self.actionHOME.triggered.connect(self.add_calender)

        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.main_widget)

        self.widget_content = Ui_Calender()
        self.widget_content.setupUi(self.main_widget)
        self.widget_content.Enter_Attendance_pushButton.clicked.connect(
            self.save_daily_attendance)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        self.menubar.setCursor(QCursor(Qt.PointingHandCursor))
        self.menubar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.menuHome = QMenu(self.menubar)
        self.menuHome.setObjectName(u"menuHome")
        self.menuGET_DATA = QMenu(self.menubar)
        self.menuGET_DATA.setObjectName(u"menuGET_DATA")
        self.menuSETTINGS = QMenu(self.menubar)
        self.menuSETTINGS.setObjectName(u"menuSETTINGS")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Add actions to menus
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuGET_DATA.menuAction())
        self.menubar.addAction(self.menuSETTINGS.menuAction())
        self.menuHome.addAction(self.actionHOME)
        self.menuGET_DATA.addAction(self.actionASV)
        self.menuGET_DATA.addAction(self.actionAV)
        self.menuGET_DATA.addSeparator()
        self.menuGET_DATA.addAction(self.actionDAILY_ATTENDANCE)
        self.menuSETTINGS.addAction(self.actionNEW_ROUTINE)
        self.menuSETTINGS.addAction(self.actionEDIT_ROUTINE)
        self.menuSETTINGS.addSeparator()
        self.menuSETTINGS.addAction(self.actionEDIT_DATABASE)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Attendance System", None))
        self.actionASV.setText(
            QCoreApplication.translate("MainWindow", u"ATTENDANCE STATISTICAL VISUALIZATION", None))
        self.actionAV.setText(
            QCoreApplication.translate("MainWindow", u"ATTENDANCE STATISTICS", None))
        self.actionDAILY_ATTENDANCE.setText(
            QCoreApplication.translate("MainWindow", u"DAILY ATTENDANCE", None))
        self.actionNEW_ROUTINE.setText(
            QCoreApplication.translate("MainWindow", u"NEW ROUTINE", None))
        self.actionEDIT_ROUTINE.setText(
            QCoreApplication.translate("MainWindow", u"EDIT ROUTINE", None))
        self.actionEDIT_DATABASE.setText(
            QCoreApplication.translate("MainWindow", u"EDIT DATABASE", None))
        self.actionHOME.setText(
            QCoreApplication.translate("MainWindow", u"HOME", None))
        self.menuHome.setTitle(
            QCoreApplication.translate("MainWindow", u"HOME", None))
        self.menuGET_DATA.setTitle(
            QCoreApplication.translate("MainWindow", u"GET DATA", None))
        self.menuSETTINGS.setTitle(
            QCoreApplication.translate("MainWindow", u"SETTINGS", None))
    # retranslateUi

    # Methods to handle menu actions
    def add_calender(self):
        self.deleteLayout(self.main_widget.layout())
        self.widget_content = Ui_Calender()
        self.widget_content.setupUi(self.main_widget)
        self.widget_content.Enter_Attendance_pushButton.clicked.connect(
            self.save_daily_attendance)

    def daily_attendance_table(self):
        self.deleteLayout(self.main_widget.layout())
        self.widget_content = Ui_Daily_Attendance_Table()
        self.widget_content.setupUi(self.main_widget)

    def add_new_routine(self):
        self.deleteLayout(self.main_widget.layout())
        self.widget_content = Ui_New_Routine()
        self.widget_content.setupUi(self.main_widget)

    def edit_routine(self):
        self.deleteLayout(self.main_widget.layout())
        self.widget_content = Ui_Edit_Routine()
        self.widget_content.setupUi(self.main_widget)

    def add_edit_database(self):
        pass

    def get_monthly_attendance_statistic(self):
        self.deleteLayout(self.main_widget.layout())
        self.widget_content = Ui_Attendance_stats_visualization()
        self.widget_content.setupUi(self.main_widget)

    def get_monthly_attendance_table(self):
        self.deleteLayout(self.main_widget.layout())
        self.widget_content = Ui_Attendance_stats()
        self.widget_content.setupUi(self.main_widget)

    def save_daily_attendance(self):
        date = self.widget_content.date
        self.deleteLayout(self.main_widget.layout())
        self.widget_content = Ui_Daily_Attendance_update()
        self.widget_content.setupUi(self.main_widget,date)
        self.widget_content.back_pushButton.clicked.connect(self.add_calender)

    def deleteLayout(self, cur_lay):
        if cur_lay is not None:
            while cur_lay.count():
                item = cur_lay.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            parent_widget = cur_lay.parentWidget()
            if parent_widget is not None:
                parent_widget.layout().removeItem(cur_lay)