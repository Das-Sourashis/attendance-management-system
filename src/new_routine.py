from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt,QDate)
from PySide6.QtGui import (QFont,)
from PySide6.QtWidgets import (QDateEdit, QFrame, QHBoxLayout,
                               QLabel, QPushButton, QScrollArea, QSpinBox, QVBoxLayout, QWidget,QComboBox,QCheckBox,QLineEdit,QMessageBox)

from edit_subjects import Ui_edit_subject_Frame
import database_functions as db


class Ui_New_Routine(object):
    encode = {
        'Practical':'P',
        'Theory':'T'
    }
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.subject_data_frame = []
        Form.resize(858, 375)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(Form)
        self.top_frame.setObjectName(u"frame")
        self.top_frame.setStyleSheet(u"""#frame {
                                    background-color: rgb(1, 107, 13);
                                    border-top-left-radius: 10px;
                                    border-top-right-radius: 10px;
                                }""")
        self.top_frame_horizontalLayout = QHBoxLayout(self.top_frame)
        self.top_frame_horizontalLayout.setObjectName(u"top_frame_horizontalLayout")
        self.subject_count_label = QLabel(self.top_frame)
        self.subject_count_label.setObjectName(u"subject_count_label")
        font = QFont()
        font.setFamilies([u"Cascadia Code SemiBold"])
        font.setPointSize(12)
        font.setBold(True)
        self.subject_count_label.setFont(font)

        self.top_frame_horizontalLayout.addWidget(self.subject_count_label, 0, Qt.AlignmentFlag.AlignRight)

        self.subject_count_spinBox = QSpinBox(self.top_frame)
        self.subject_count_spinBox.setObjectName(u"subject_count_spinBox")
        self.subject_count_spinBox.setFont(font)
        self.subject_count_spinBox.setWrapping(False)
        self.subject_count_spinBox.setProperty("showGroupSeparator", False)

        self.top_frame_horizontalLayout.addWidget(self.subject_count_spinBox, 0, Qt.AlignmentFlag.AlignLeft)

        self.get_fields_pushButton = QPushButton(self.top_frame)
        self.get_fields_pushButton.setObjectName(u"get_fields_pushButton")
        pushButton_font = QFont()
        pushButton_font.setFamilies([u"Arial"])
        pushButton_font.setPointSize(10)
        pushButton_font.setBold(True)
        self.get_fields_pushButton.setFont(pushButton_font)
        self.get_fields_pushButton.clicked.connect(self.add_subjects)
        self.get_fields_pushButton.setStyleSheet(u"""#frame QPushButton {
                                        background-color: blue;
                                        color: white;
                                        border: 2px solid darkblue;
                                        border-radius: 5px;
                                        padding: 5px 15px;
                                        margin: 2px 20px;
                                    }
                                    
                                    #frame QPushButton:hover {
                                        background-color: lightblue;
                                        color: black;
                                        border-color: blue;
                                    }
                                    
                                    #frame QPushButton:pressed {
                                        background-color: darkblue;
                                        border-color: darkblue;
                                    }""")

        self.top_frame_horizontalLayout.addWidget(self.get_fields_pushButton, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalLayout.addWidget(self.top_frame)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.middle_frame = QFrame(Form)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setStyleSheet(u"""QFrame {
                                        background-color: rgb(90, 255, 131);
                                        margin: 0px;
                                    }""")
        self.middle_frame_horizontalLayout = QHBoxLayout(self.middle_frame)
        self.middle_frame_horizontalLayout.setObjectName(u"middle_frame_horizontalLayout")
        self.start_date_label = QLabel(self.middle_frame)
        self.start_date_label.setObjectName(u"start_date_label")
        self.start_date_label.setFont(font)
        self.start_date_label.setMargin(2)
        self.start_date_label.setIndent(10)

        self.middle_frame_horizontalLayout.addWidget(
            self.start_date_label, 0, Qt.AlignmentFlag.AlignRight)

        self.start_date_dateEdit = QDateEdit(self.middle_frame)
        self.start_date_dateEdit.setObjectName(u"start_date_dateEdit")
        self.start_date_dateEdit.setFont(font)
        self.start_date_dateEdit.setCalendarPopup(True)
        self.start_date_dateEdit.setDate(QDate.currentDate())

        self.middle_frame_horizontalLayout.addWidget(self.start_date_dateEdit, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout.addWidget(self.middle_frame)

        self.subject_list_scrollArea = QScrollArea(Form)
        self.subject_list_scrollArea.setObjectName(u"subject_list_scrollArea")
        self.subject_list_scrollArea.setToolTipDuration(-1)
        self.subject_list_scrollArea.setStyleSheet(u"""QScrollArea {
                                            background-color: rgb(174, 255, 120);
                                            margin: 0px;
                                        }""")
        self.subject_list_scrollArea.setFrameShape(QFrame.Shape.Box)
        self.subject_list_scrollArea.setWidgetResizable(True)
        self.subject_list_scrollAreaWidgetContents = QWidget()
        self.subject_list_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 838, 227))
        self.subject_list_scrollArea.setWidget(self.subject_list_scrollAreaWidgetContents)

        self.scrollAreaLayout = QVBoxLayout(self.subject_list_scrollAreaWidgetContents)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")

        self.verticalLayout.addWidget(self.subject_list_scrollArea)

        self.new_routine_pushButton = QPushButton(Form)
        self.new_routine_pushButton.setObjectName(u"new_routine_pushButton")
        self.new_routine_pushButton.clicked.connect(self.save_new_routine)
        self.new_routine_pushButton.setFont(pushButton_font)
        self.new_routine_pushButton.setStyleSheet(u"""QPushButton {
                                            background-color: green;
                                            border: 1px solid darkgreen;
                                            color: white;
                                            padding: 5px 10px;
                                            border-radius: 5px;
                                            margin: 5px;
                                        }
                                        
                                        QPushButton:hover {
                                            background-color: lightyellow;
                                            color: green;
                                            border: 1px solid darkgreen;
                                        }
                                        
                                        QPushButton:pressed {
                                            background-color: lightgreen;
                                            border: 1px solid darkgreen;
                                        }""")

        self.verticalLayout.addWidget(
            self.new_routine_pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.subject_count_label.setText(QCoreApplication.translate(
            "Form", u"Number Of Subjects : ", None))
        self.get_fields_pushButton.setText(QCoreApplication.translate(
            "Form", u"Get Routine Fields", None))
        self.start_date_label.setText(QCoreApplication.translate(
            "Form", u"Start Date :", None))
        self.new_routine_pushButton.setText(QCoreApplication.translate(
            "Form", u"Generate New Routine", None))
    # retranslateUi

    def add_subjects(self):
        self.delete_Layout(self.scrollAreaLayout)
        self.subject_data_frame.clear()
        for i in range(self.subject_count_spinBox.value()):
            subject_frame = QFrame(self.subject_list_scrollAreaWidgetContents)
            ui_subject_frame = Ui_edit_subject_Frame()
            ui_subject_frame.setupUi(subject_frame,(i+1,"",""," "))
            self.scrollAreaLayout.addWidget(subject_frame)
            self.subject_data_frame.append({
                'id':i+1,
                'checkbox': subject_frame.findChild(QCheckBox),
                'subj_name':subject_frame.findChildren(QLineEdit)[0],
                'teacher_name':subject_frame.findChildren(QLineEdit)[1],
                'subj_type':subject_frame.findChild(QComboBox)
            })
            subject_frame.findChild(QCheckBox).setChecked(True)
            subject_frame.findChild(QCheckBox).setEnabled(False)

    def save_new_routine(self):
        subjects = []
        date = self.start_date_dateEdit.date().toPython()
        for subject_frame in self.subject_data_frame:
            if subject_frame['checkbox'].isChecked() == True:
                subj_name = subject_frame['subj_name'].text().strip()
                teacher_name = subject_frame['teacher_name'].text().strip()
                subj_type = subject_frame['subj_type'].currentText()

                if subj_name and teacher_name:
                    subjects.append((
                        subject_frame['id'],
                        subj_name,
                        teacher_name,
                        self.encode[subj_type]
                    ))
                else:
                    QMessageBox.critical(None, 'Error', "Teacher and Subject cannot be empty.")
                    return

        if not subjects:
            QMessageBox.information(None, 'Empty', "No New Routine Created.")
            return

        reply = QMessageBox.question(
            None, 
            'Confirmation',
            "Are you sure you want to save the New routine and completely delete all previous routine data?\n"+
            f"With Start Date : {date}\n"+
            "(id, subject name, teacher's name, subject type)\n" +
            '\n'.join(map(str, subjects)),
            QMessageBox.Yes,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                db.clear_existing_routine_and_create_new(subjects,date)
                QMessageBox.information(None, 'Success', "Routine data saved successfully.")
            except Exception as e:
                QMessageBox.critical(None, 'Error', f"An error occurred while saving the data: {str(e)}")

    def delete_Layout(self, cur_lay):
        if cur_lay is not None:
            while cur_lay.count():
                item = cur_lay.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.delete_Layout(item.layout())
            parent_widget = cur_lay.parentWidget()
            if parent_widget is not None:
                parent_widget.layout().removeItem(cur_lay)