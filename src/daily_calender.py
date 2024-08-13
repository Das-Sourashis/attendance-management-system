from PySide6.QtCore import (QCoreApplication, QLocale, QMetaObject,  Qt, QDate)
from PySide6.QtGui import (QFont, QPalette)
from PySide6.QtWidgets import (
    QCalendarWidget, QLabel, QPushButton, QVBoxLayout)
import resource_rc
import database_functions as db

class Ui_Calender():
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(726, 298)
        Form.setStyleSheet(u"")
        self.date = QDate.currentDate().toString("yyyy-MM-dd")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.calendarWidget = QCalendarWidget(Form)
        self.calendarWidget.setObjectName(u"calendarWidget")
        palette = QPalette()
        self.calendarWidget.setPalette(palette)
        self.calendarWidget.setToolTipDuration(-1)
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setStyleSheet(u"""
            QCalendarWidget QWidget {
                alternate-background-color: rgb(3, 84, 17);
            }
            
            /* style for top navigation area ###############################################*/ 
            
            #qt_calendar_navigationbar {
                background-color: rgb(0, 170, 0);
                height: 30px;
                border: 2px solid  #B8E2FF;
                border-bottom: 0px;
                border-top-left-radius: 15px;
                border-top-right-radius: 15px;
            }
            
            /* style for month change buttons ############################################ */
            
            #qt_calendar_prevmonth, 
            #qt_calendar_nextmonth {
                border: none;  
                min-width: 13px;
                max-width: 23px;
                min-height: 13px;
                max-height: 23px;
                border-radius: 15px; 
                background-color: transparent; 
                padding: 15px;
            }
            
            /* style for pre month button ############################################ */
            
            #qt_calendar_prevmonth {
                margin-left: 15px;
            }
            
            /* style for next month button ########################################### */
            #qt_calendar_nextmonth {
                margin-right: 15px;
            }
            #qt_calendar_prevmonth:hover, 
            #qt_calendar_nextmonth:hover {
                background-color: #55aaff;
            }
            
            #qt_calendar_prevmonth:pressed, 
            #qt_calendar_nextmonth:pressed {
                background-color: rgb(120, 244, 92);
            }
            
            /* Style for month and year buttons #################################### */
            
            #qt_calendar_yearbutton {
                color: #000;
                margin: 15px;
                border-radius: 5px;
                font-size: 15px;
                padding: 0px 10px;
            }
            
            #qt_calendar_monthbutton {
                width: 110px;
                color: #000;
                font-size: 15px;
                margin: 15px 0px;
                border-radius: 5px;
                padding: 0px 10px;
            }
            
            #qt_calendar_yearbutton:hover, 
            #qt_calendar_monthbutton:hover {
                background-color: #55aaff;
            }
            
            #qt_calendar_yearbutton:pressed, 
            #qt_calendar_monthbutton:pressed {
                background-color: rgba(235, 235, 235, 100);
            }
            
            /* Style for year input lineEdit ##########################################*/
            
            #qt_calendar_yearedit {
                min-width: 100px;
                color: #000;
                background: transparent;
                font-size: 15px;
            }
            
            /* Style for year change buttons ######################################*/
            
            #qt_calendar_yearedit::up-button { 
                image: url(:/icon/arrow-151-48.ico);
                subcontrol-position: right;
            }
            
            #qt_calendar_yearedit::down-button { 
                image: url(:/icon/arrow-213-48.ico);
                subcontrol-position: left; 
            }
            
            #qt_calendar_yearedit::down-button, 
            #qt_calendar_yearedit::up-button {
                width: 10px;
                padding: 0px 5px;
                border-radius: 3px;
            }
            
            #qt_calendar_yearedit::down-button:hover, 
            #qt_calendar_yearedit::up-button:hover {
                background-color: #55aaff;
            }
            
            /* Style for month select menu ##################################### */
            
            #calendarWidget QToolButton QMenu {
                background-color: rgb(114, 255, 130);
            }
            
            #calendarWidget QToolButton QMenu::item {
                /*padding: 10px;*/
            }
            #calendarWidget QToolButton QMenu::item:selected:enabled {
                background-color: #55aaff;
            }
            
            #calendarWidget QToolButton::menu-indicator {
                subcontrol-position: right center;
                margin-top: 10px;
                width: 20px;
            }
            
            /* Style for calendar table ########################################## */
            #qt_calendar_calendarview {
                outline: 0px;
                font: 700 12pt "Bahnschrift Condensed";
                border: 2px solid  #B8E2FF;
                border-top: 0px;
                border-bottom-left-radius: 5px;
                border-bottom-right-radius: 5px;
            }
            
            #qt_calendar_calendarview::item:hover {
                border-radius: 5px;
                background-color: rgb(160, 255, 187);
            }
            
            #qt_calendar_calendarview::item:selected {
                background-color: rgb(0, 135, 0); 
                border-radius: 5px;
            }
        """)  # Style the calendar widget

        # Set calendar widget properties
        self.calendarWidget.setLocale(QLocale(QLocale.English, QLocale.India))
        self.calendarWidget.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.calendarWidget.setFirstDayOfWeek(Qt.DayOfWeek.Monday)
        self.calendarWidget.setGridVisible(True)

        self.calendarWidget.setMinimumDate(db.get_date())
        self.calendarWidget.setMaximumDate(QDate.currentDate())

        self.calendarWidget.setSelectionMode(QCalendarWidget.SelectionMode.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.LongDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.ISOWeekNumbers)
        self.calendarWidget.setNavigationBarVisible(True)

        self.calendarWidget.clicked.connect(self.show_attendance_info)
        self.calendarWidget.currentPageChanged.connect(self.show_attendance_info)

        self.verticalLayout.addWidget(self.calendarWidget)

        # Attendance label setup
        self.Attendance_label = QLabel(Form)
        self.Attendance_label.setObjectName(u"Attendance_label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Attendance_label.setFont(font)
        self.Attendance_label.setLineWidth(15)
        self.Attendance_label.setMargin(5)
        self.Attendance_label.setIndent(1)

        self.verticalLayout.addWidget(self.Attendance_label, 0, Qt.AlignmentFlag.AlignHCenter)

        # Button setup
        self.Enter_Attendance_pushButton = QPushButton(Form)
        self.Enter_Attendance_pushButton.setObjectName(u"Enter_Attendance_pushButton")
        self.Enter_Attendance_pushButton.setStyleSheet(u"""
            QPushButton {
                background-color: green;
                height: 15%;
                color: white;
                font: 900 12pt "Segoe UI";
                border: 2px solid darkgreen;
                border-radius: 10px;
                padding: 5px 20px;
                margin: 5px;
            }

            QPushButton:hover {
                background-color: lightgreen;
                color: green;
                border-color: green;
            }

            QPushButton:pressed {
                background-color: darkgreen;
                border-color: darkgreen;
            }
        """)

        self.verticalLayout.addWidget(
            self.Enter_Attendance_pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.container_widget = Form
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        response = db.any_day_total_attendance(QDate.currentDate().toString("yyyy-MM-dd"))
        self.Attendance_label.setText(QCoreApplication.translate(
            "Form", f'Attendance : {response[0][0]} h / {response[0][1]} h' if response[0][1] is not None else 'No Classes', None))
        self.Enter_Attendance_pushButton.setText(QCoreApplication.translate(
            "Form", u"Enter Attendance", None))
    # retranslateUi

    def show_attendance_info(self):
        self.date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        response = db.any_day_total_attendance(self.date)
        self.Attendance_label.setText(f'Attendance : {response[0][0]} h / {response[0][1]} h' if response[0][1] is not None else 'No Classes')
