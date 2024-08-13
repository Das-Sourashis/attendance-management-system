from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QFrame)

# input frame for subject used in edit_routine.py and new_routine.py

class Ui_edit_subject_Frame(object):
    # Decode subject type from code to full name
    decode = {
        'P': 'Practical',
        'T': 'Theory',
        " ": 'Theory'  # Default to 'Theory' for empty or unknown codes
    }

    def setupUi(self, Frame, subject):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(756, 52)  # Set the size of the frame

        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        # Checkbox for the subject, possibly for marking or selection
        self.checkBox = QCheckBox(Frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"""
            QCheckBox { 
                padding: 5px; 
                font-size: 12px;
                font-family: Cascadia Code SemiBold;    
            }""")

        self.horizontalLayout.addWidget(self.checkBox)

        # Label for Subject Name
        self.label_subject_name = QLabel(Frame)
        self.label_subject_name.setObjectName(u"label_subject_name")
        self.label_subject_name.setStyleSheet(u"""
            QLabel { 
                padding: 5px; 
                font-size: 12px;
                font-family: Cascadia Code SemiBold;    
            }""")

        self.horizontalLayout.addWidget(self.label_subject_name)

        # Text field for entering the subject name
        self.lineEdit_sub_name = QLineEdit(Frame)
        self.lineEdit_sub_name.setObjectName(u"lineEdit_sub_name")
        self.lineEdit_sub_name.setText(subject[1])  # Set default text from subject data
        self.lineEdit_sub_name.setStyleSheet(u"""
            QLineEdit {
                border: 2px solid #A3A3A3;
                border-radius: 5px;
                padding: 5px;
                background-color: #FFFFFF;
                selection-background-color: #007BFF;
                selection-color: #FFFFFF;
            }
            QLineEdit:focus {
                border-color: #007BFF;
            }
        """)

        self.horizontalLayout.addWidget(self.lineEdit_sub_name)

        # Label for Teacher
        self.label_teacher = QLabel(Frame)
        self.label_teacher.setObjectName(u"label_teacher")
        self.label_teacher.setStyleSheet(u"""
            QLabel { 
                padding: 5px; 
                font-size: 12px;
                font-family: Cascadia Code SemiBold;    
            }""")

        self.horizontalLayout.addWidget(self.label_teacher)

        # Text field for entering the teacher's name
        self.lineEdit_teacher = QLineEdit(Frame)
        self.lineEdit_teacher.setObjectName(u"lineEdit_teacher")
        self.lineEdit_teacher.setText(subject[2])  # Set default text from subject data
        self.lineEdit_teacher.setStyleSheet(u"""
            QLineEdit {
                border: 2px solid #A3A3A3;
                border-radius: 5px;
                padding: 5px;
                background-color: #FFFFFF;
                selection-background-color: #007BFF;
                selection-color: #FFFFFF;
            }
            QLineEdit:focus {
                border-color: #007BFF;
            }
        """)

        self.horizontalLayout.addWidget(self.lineEdit_teacher)

        # Label for Subject Type
        self.label_subject_type = QLabel(Frame)
        self.label_subject_type.setObjectName(u"label_subject_type")
        self.label_subject_type.setStyleSheet(u"""
            QLabel { 
                padding: 5px; 
                font-size: 12px;
                font-family: Cascadia Code SemiBold;    
            }""")

        self.horizontalLayout.addWidget(self.label_subject_type)

        # ComboBox for selecting subject type (Theory/Practical)
        self.comboBox_sub_type = QComboBox(Frame)
        self.comboBox_sub_type.setObjectName(u"comboBox_sub_type")
        self.comboBox_sub_type.addItems(['Theory', 'Practical'])  # Options for the ComboBox
        self.comboBox_sub_type.setCurrentText(self.decode[subject[3]])  # Set current text based on subject type
        self.comboBox_sub_type.setStyleSheet(u"""
            QComboBox {
                border: 2px solid #A3A3A3;
                border-radius: 5px;
                padding: 5px;
                background-color: #FFFFFF;
            }
            QComboBox:focus {
                border-color: #007BFF;
            }
        """)

        self.horizontalLayout.addWidget(self.comboBox_sub_type)

        self.retranslateUi(Frame, subject[0])

        QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame, i):
        # Set window title and text for labels and checkbox
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.checkBox.setText(QCoreApplication.translate("Frame", f" {i})", None))
        self.label_subject_name.setText(QCoreApplication.translate("Frame", u"Subject Name :", None))
        self.label_teacher.setText(QCoreApplication.translate("Frame", u"Teacher : ", None))
        self.label_subject_type.setText(QCoreApplication.translate("Frame", u"Subject Type :", None))
