from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QDateEdit, QFrame, QHBoxLayout, QLabel,
                               QPushButton, QScrollArea, QSizePolicy, QVBoxLayout, QWidget, QLineEdit, QComboBox, QCheckBox, QMessageBox)
from edit_subjects import Ui_edit_subject_Frame
import database_functions as db


class Ui_Edit_Routine(object):
        # Encode subject type from full name to code
    encode = {
        'Practical':'P',
        'Theory':'T'
    }
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.subject_data_frame = [] # List to keep track of subject frames
        Form.resize(880, 372)
        # Vertical layout to arrange widgets in a column
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, -1, -1)
        # Top frame for the date and save button
        self.top_frame = QFrame(Form)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setStyleSheet(u"""QFrame {
                                    background-color: rgb(1, 107, 13);
                                    border-top-left-radius: 10px;
                                    border-top-right-radius: 10px;
                                }""")
        self.top_frame_horizontalLayout = QHBoxLayout(self.top_frame)
        self.top_frame_horizontalLayout.setObjectName(u"top_frame_horizontalLayout")
        # Label for start date
        self.start_date_label = QLabel(self.top_frame)
        self.start_date_label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Cascadia Code SemiBold"])
        font.setPointSize(12)
        font.setBold(True)
        self.start_date_label.setFont(font)
        self.start_date_label.setStyleSheet(u"""QLabel {
                                    padding: 5px 20px;
                                }""")

        self.top_frame_horizontalLayout.addWidget(self.start_date_label, 0, Qt.AlignmentFlag.AlignRight)

        # DateEdit widget for selecting start date
        self.start_dateEdit = QDateEdit(self.top_frame)
        self.start_dateEdit.setObjectName(u"start_dateEdit")
        self.start_dateEdit.setFont(font)
        self.start_dateEdit.setCalendarPopup(True)
        self.start_dateEdit.setDate(db.get_date())

        self.top_frame_horizontalLayout.addWidget(self.start_dateEdit, 0, Qt.AlignmentFlag.AlignLeft)

        # Save Date button
        self.Save_Date_pushButton = QPushButton(self.top_frame)
        self.Save_Date_pushButton.setObjectName(u"Save_Date_pushButton")
        self.Save_Date_pushButton.clicked.connect(self.save_date)
        pushButton_font = QFont()
        pushButton_font.setFamilies([u"Arial"])
        pushButton_font.setPointSize(10)
        pushButton_font.setBold(True)
        self.Save_Date_pushButton.setFont(pushButton_font)
        self.Save_Date_pushButton.setStyleSheet(u"""QPushButton {
                                            background-color: blue;
                                            color: white;
                                            border: 2px solid darkblue;
                                            border-radius: 5px;
                                            padding: 5px 15px;
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
                                        }""")

        self.top_frame_horizontalLayout.addWidget(self.Save_Date_pushButton, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalLayout.addWidget(self.top_frame)

        # Line separator
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setAutoFillBackground(False)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        # Edit Routine button
        self.Edit_Routine_pushButton = QPushButton(Form)
        self.Edit_Routine_pushButton.setObjectName(u"Edit_Routine_pushButton")
        self.Edit_Routine_pushButton.setFont(pushButton_font)
        self.Edit_Routine_pushButton.clicked.connect(self.save_edited_routine)
        self.Edit_Routine_pushButton.setStyleSheet(u"""QPushButton {
                                            background-color: rgb(221, 255, 0);
                                            color: black;
                                            border: 2px solid rgb(76, 70, 0);
                                            border-radius: 5px;
                                            padding: 5px 15px;
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
                                        }""")

        self.verticalLayout.addWidget(self.Edit_Routine_pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        # ScrollArea for subject list
        self.subject_list_scrollArea = QScrollArea(Form)
        self.subject_list_scrollArea.setObjectName(u"subject_list_scrollArea")
        self.subject_list_scrollArea.setWidgetResizable(True)
        self.subject_list_scrollAreaWidgetContents = QWidget()
        self.subject_list_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 859, 243))
        self.subject_list_scrollArea.setWidget(self.subject_list_scrollAreaWidgetContents)

        self.scrollAreaLayout = QVBoxLayout(self.subject_list_scrollAreaWidgetContents)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")

        self.verticalLayout.addWidget(self.subject_list_scrollArea)

        self.retranslateUi(Form)

        self.add_subjects() # Populate the subject list
        
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        # Set window title and text for labels and buttons
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.start_date_label.setText(QCoreApplication.translate(
            "Form", u"Change Start Date :", None))
        self.Save_Date_pushButton.setText(
            QCoreApplication.translate("Form", u"Save Date", None))
        self.Edit_Routine_pushButton.setText(
            QCoreApplication.translate("Form", u"Edit Routine", None))
    # retranslateUi

    def add_subjects(self):
        # Add subject frames to the scroll area
        for subject in db.get_subjects():
            subject_frame = QFrame(self.subject_list_scrollAreaWidgetContents)
            ui_subject_frame = Ui_edit_subject_Frame()
            ui_subject_frame.setupUi(subject_frame,subject)
            self.scrollAreaLayout.addWidget(subject_frame)
            self.subject_data_frame.append({
                'id':subject[0],
                'checkbox':subject_frame.findChild(QCheckBox),
                'subj_name':subject_frame.findChildren(QLineEdit)[0],
                'teacher_name':subject_frame.findChildren(QLineEdit)[1],
                'subj_type':subject_frame.findChild(QComboBox)
            })

    def save_edited_routine(self):
        # Collect data from subject frames and save
        subjects = []
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
            QMessageBox.information(None, 'No Changes', "No subjects were selected or edited.")
            return

        # Confirmation dialog before saving
        reply = QMessageBox.question(
            None, 
            'Confirmation',
            "Are you sure you want to save the edited routine?\n"
            "(id, subject name, teacher's name, subject type)\n" +
            '\n'.join(map(str, subjects)),
            QMessageBox.Yes,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                db.edit_subjects(subjects)  # Save the edited subjects to the database
                QMessageBox.information(None, 'Success', "Routine data saved successfully.")
            except Exception as e:
                QMessageBox.critical(None, 'Error', f"An error occurred while saving the data: {str(e)}")

    def save_date(self):
        # Save the selected start date
        date = self.start_dateEdit.date().toPython()
        
        reply = QMessageBox.question(
            None, 
            'Confirmation',
            f"Are you sure you want to save the selected date?\n{date.strftime('%Y-%m-%d')}",
            QMessageBox.Yes,
            QMessageBox.No
        )
    
        if reply == QMessageBox.Yes:
            try:
                db.edit_date(date) # Save the date to the database
                QMessageBox.information(None, 'Success', "Date saved successfully.")
            except Exception as e:
                QMessageBox.critical(None, 'Error', f"An error occurred while saving the date: {str(e)}")

