from PySide6.QtCore import (QCoreApplication, QDate, QMetaObject, Qt, QRect)
from PySide6.QtGui import (QCursor, QFont)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
                                QWidget, QCheckBox, QSlider, QMessageBox)
import database_functions as db
from datetime import datetime
from daily_subject_update import Ui_Daily_Subject_Update

class Ui_Daily_Attendance_update(object):
    def setupUi(self, Form, date):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.subject_data_frame = []
        self.date = date
        Form.resize(734, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_frame = QFrame(Form)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.main_frame_horizontalLayout = QHBoxLayout(self.main_frame) #layout of main_frame
        self.main_frame_horizontalLayout.setObjectName(u"main_frame_horizontalLayout")
        self.left_frame = QFrame(self.main_frame)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.left_frame_verticalLayout = QVBoxLayout(self.left_frame)
        self.left_frame_verticalLayout.setObjectName(u"left_frame_verticalLayout")
        self.pushButton_Frame = QFrame(self.left_frame)
        self.pushButton_Frame.setObjectName(u"pushButton_Frame")
        self.pushButton_Frame.setStyleSheet(u"background-color: rgb(115, 255, 99);")
        self.pushButton_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pushButton_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_Frame_horizontalLayout = QHBoxLayout(self.pushButton_Frame)
        self.pushButton_Frame_horizontalLayout.setSpacing(25)
        self.pushButton_Frame_horizontalLayout.setObjectName(u"pushButton_Frame_horizontalLayout")
        self.pushButton_Frame_horizontalLayout.setContentsMargins(25, -1, 25, -1)
        self.back_pushButton = QPushButton(self.pushButton_Frame)
        self.back_pushButton.setObjectName(u"back_pushButton")
        back_button_font = QFont()
        back_button_font.setPointSize(10)
        back_button_font.setBold(False)
        back_button_font.setItalic(True)
        self.back_pushButton.setFont(back_button_font)
        self.back_pushButton.setStyleSheet(u'''
                    QPushButton {
                        background-color: green;
                        color: white;
                        border: 2px solid darkgreen;
                        border-radius: 5px;
                        padding: 5px 15px;
                        margin: 7px 20px;
                    }

                    QPushButton:hover {
                        background-color: lightgreen;
                        color: black;
                        border-color: green;
                    }

                    QPushButton:pressed {
                        background-color: darkgreen;
                        border-color: darkgreen;
                    }
                    ''')

        self.pushButton_Frame_horizontalLayout.addWidget(
            self.back_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.save_pushButton = QPushButton(self.pushButton_Frame)
        self.save_pushButton.setObjectName(u"save_pushButton")
        save_edit_button_font = QFont()
        save_edit_button_font.setFamilies([u"Arial"])
        save_edit_button_font.setPointSize(10)
        save_edit_button_font.setBold(True)
        self.save_pushButton.setFont(save_edit_button_font)
        self.save_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_pushButton.clicked.connect(self.save_routine_data)
        self.save_pushButton.setStyleSheet(u'''
                    QPushButton {
                        background-color: blue;
                        color: white;
                        border: 2px solid darkblue;
                        border-radius: 5px;
                        padding: 8px 15px;
                        margin: 7px 20px;
                    }

                    QPushButton:hover {
                        background-color: lightblue;
                        color: black;
                        border-color: blue;
                    }

                    QPushButton:pressed {
                        background-color: darkblue;
                        border-color: darkblue;
                    }
                    ''')

        self.pushButton_Frame_horizontalLayout.addWidget(
            self.save_pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.edit_pushButton = QPushButton(self.pushButton_Frame)
        self.edit_pushButton.setObjectName(u"edit_pushButton")
        self.edit_pushButton.setFont(save_edit_button_font)
        self.edit_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_pushButton.clicked.connect(self.enable_edit)
        self.edit_pushButton.setStyleSheet(u'''
                    QPushButton {
                        background-color: rgb(221, 255, 0);
                        color: black;
                        border: 2px solid rgb(76, 70, 0);
                        border-radius: 5px;
                        padding: 8px 15px;
                        margin: 7px 20px;
                    }

                    QPushButton:hover {
                        background-color: rgb(255, 255, 124);
                        color: black;
                        border-color: rgb(251, 255, 0);
                    }

                    QPushButton:pressed {
                        background-color: rgb(149, 139, 0);
                        border-color: rgb(117, 118, 35);
                    }
                    ''')

        self.pushButton_Frame_horizontalLayout.addWidget(self.edit_pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.left_frame_verticalLayout.addWidget(self.pushButton_Frame)

        self.attendance_input_scrollArea = QScrollArea(self.left_frame)
        self.attendance_input_scrollArea.setObjectName(u"attendance_input_scrollArea")
        self.attendance_input_scrollArea.setStyleSheet(u"background-color: rgb(234, 255, 129);")
        self.attendance_input_scrollArea.setFrameShape(QFrame.Shape.Box)
        self.attendance_input_scrollArea.setWidgetResizable(True)
        self.attendance_input_scrollAreaWidgetContents = QWidget()
        self.attendance_input_scrollAreaWidgetContents.setObjectName(u"attendance_input_scrollAreaWidgetContents")
        self.attendance_input_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 416, 163))
        self.attendance_input_verticalLayout = QVBoxLayout(self.attendance_input_scrollAreaWidgetContents)
        self.attendance_input_verticalLayout.setSpacing(15)
        self.attendance_input_verticalLayout.setObjectName(u"attendance_input_verticalLayout")
        self.attendance_input_verticalLayout.setContentsMargins(10, -1, -1, -1)
        self.attendance_input_scrollArea.setWidget(self.attendance_input_scrollAreaWidgetContents)

        self.left_frame_verticalLayout.addWidget(self.attendance_input_scrollArea)

        self.main_frame_horizontalLayout.addWidget(self.left_frame)

        self.line = QFrame(self.main_frame)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.main_frame_horizontalLayout.addWidget(self.line)

        self.class_list_scrollArea = QScrollArea(self.main_frame)
        self.class_list_scrollArea.setObjectName(u"class_list_scrollArea")
        self.class_list_scrollArea.setStyleSheet(u"background-color: rgb(234, 255, 129);")
        self.class_list_scrollArea.setFrameShape(QFrame.Shape.Box)
        self.class_list_scrollArea.setWidgetResizable(True)
        self.class_list_scrollAreaWidgetContents = QWidget()
        self.class_list_scrollAreaWidgetContents.setObjectName(u"class_list_scrollAreaWidgetContents")
        self.class_list_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 237, 258))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.class_list_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.class_list_scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.class_list_verticalLayout = QVBoxLayout(self.class_list_scrollAreaWidgetContents)
        self.class_list_verticalLayout.setSpacing(15)
        self.class_list_verticalLayout.setObjectName(u"class_list_verticalLayout")
        self.class_list_verticalLayout.setContentsMargins(10, -1, -1, -1)

        self.add_subjects()

        self.class_list_label = QLabel(self.class_list_scrollAreaWidgetContents)
        self.class_list_label.setObjectName(u"class_list_label")
        class_list_font = QFont()
        class_list_font.setFamilies([u"Arial"])
        class_list_font.setPointSize(14)
        class_list_font.setBold(True)
        self.class_list_label.setFont(class_list_font)
        self.class_list_label.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.class_list_label.setLineWidth(5)
        self.class_list_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.class_list_label.setWordWrap(True)
        self.class_list_label.setMargin(5)
        self.class_list_label.setIndent(5)

        self.class_list_verticalLayout.addWidget(self.class_list_label)

        self.class_list_scrollArea.setWidget(self.class_list_scrollAreaWidgetContents)

        self.main_frame_horizontalLayout.addWidget(self.class_list_scrollArea)

        self.verticalLayout.addWidget(self.main_frame)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.subject_info(date)
        self.add_value_to_subjects(date)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.back_pushButton.setText(
            QCoreApplication.translate("Form", u"< Back", None))
        self.save_pushButton.setText(
            QCoreApplication.translate("Form", u"Save", None))
        self.edit_pushButton.setText(
            QCoreApplication.translate("Form", u"Edit", None))
        # self.label.setText("")
    # retranslateUi

    def add_subjects(self):
        for subject in db.get_subjects():
            subject_frame = QFrame()
            self.subjects = Ui_Daily_Subject_Update()
            self.subjects.setupUi(subject_frame, subject)
            self.attendance_input_verticalLayout.addWidget(subject_frame)
            self.subject_data_frame.append({
                'id': subject[0],
                'checkbox': subject_frame.findChild(QCheckBox),
                'class_duration_slider': subject_frame.findChildren(QSlider)[0],
                'student_time_slider': subject_frame.findChildren(QSlider)[1],
            })

    def subject_info(self, date):
        date_object = QDate.fromString(date, "yyyy-MM-dd")
        label_text = f"Date : {date_object.toString('dd-MMMM-yyyy (dddd)')} \n\n\n\n"
        i = 1
        for subject in db.any_day_attendance_list(date):
            label_text = label_text + \
                f"{i} )  {subject[1]} by {subject[2]},\n Class Duration: {subject[4]} hours,\n Student Attendance Time: {subject[3]} hours\n\n\n"
            i += 1
        self.class_list_label.setText(label_text)

        # if i == 1:
        #     self.edit_pushButton.setEnabled(False)
        # else:
        #     self.save_pushButton.setEnabled(False)
            

    def add_value_to_subjects(self, date):
        for subject in db.any_day_attendance_list(date):
            for subject_frame in self.subject_data_frame:
                if subject[0] == subject_frame['id']:
                    subject_frame['checkbox'].setChecked(True)
                    subject_frame['class_duration_slider'].setValue(subject[4])  # duration
                    subject_frame['student_time_slider'].setValue(subject[3])  # student time
        
        if date != QDate.currentDate().toPython().strftime("%Y-%m-%d"):
            self.enable_disable_frame_content(False)
            self.save_pushButton.setEnabled(False)
        else:
            self.edit_pushButton.setEnabled(False)
            

    def enable_edit(self):
        self.save_pushButton.setEnabled(True)
        self.edit_pushButton.setEnabled(False)
        self.enable_disable_frame_content(True)

    def save_routine_data(self):
        data = []
        for subject_frame in self.subject_data_frame:
            if subject_frame['checkbox'].isChecked() == True :
                if subject_frame['class_duration_slider'].value() >= subject_frame['student_time_slider'].value():
                    data.append((
                        datetime.strptime(self.date, "%Y-%m-%d"),
                        datetime.strptime(self.date, "%Y-%m-%d").isoweekday(),
                        subject_frame['id'],
                        subject_frame['class_duration_slider'].value(),
                        subject_frame['student_time_slider'].value()
                    ))
                else:
                    QMessageBox.information(None, "Wrong Data Entry", "Class Duration is less than Student Attendance. So check your inserted data.")
                    data.clear()
                    return

        reply = QMessageBox.question(None, 'Confirmation', f"Are you sure you want to save the routine data?\n" +
                                    "('date', 'weekday', 'subject_id','class duration', 'student time duration') \n" + '\n'.join(map(str, data)), QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            db.update_daily_data(data, self.date)
            self.subject_info(self.date)
            QMessageBox.information(
                None, 'Success', "Routine data saved successfully.")
        else:
            QMessageBox.information(
                None, 'Failure', "Save operation cancelled.")

        self.enable_disable_frame_content(False)
        self.save_pushButton.setEnabled(False)
        self.edit_pushButton.setEnabled(True)

    def enable_disable_frame_content(self, state):
        for subject_frame in self.subject_data_frame:
            subject_frame['checkbox'].setEnabled(state)
            subject_frame['class_duration_slider'].setEnabled(state)
            subject_frame['student_time_slider'].setEnabled(state)
