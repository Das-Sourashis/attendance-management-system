from PySide6.QtCore import Qt, QCoreApplication, QMetaObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QCheckBox, QWidget


# Add label to sliders
class LabeledSlider(QWidget):
    def __init__(self, min_value, max_value, subject_type,  parent=None):
        super().__init__(parent)
        self.min_value = min_value
        self.max_value = max_value
        self.subject_type = subject_type
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(self.min_value)
        slider.setMaximum(self.max_value)
        slider.setTickPosition(QSlider.TicksAbove)
        slider.setTickInterval(1)

        if self.subject_type == "T":
            slider.setValue(2)
        if self.subject_type == "P":
            slider.setValue(4)

        layout.addWidget(slider)

        labels_layout = QHBoxLayout()
        for value in range(self.min_value, self.max_value + 1):
            label = QLabel(str(value), self)
            label.setAlignment(Qt.AlignCenter)
            labels_layout.addWidget(label)

        layout.addLayout(labels_layout)
        self.slider = slider


class Ui_Daily_Subject_Update(object):
    def setupUi(self, Frame, subject):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        self.max_class_hour = 6
        Frame.resize(615, 120)  # Adjust height to accommodate the labels
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # Setup Checkbox
        self.checkBox = self.createCheckBox(Frame)
        self.verticalLayout.addWidget(self.checkBox)

        # Setup horizontal layouts
        self.layout_container_horizontalLayout = self.createHorizontalLayout(
            spacing=20, margins=(45, 5, 10, -1))
        self.class_duration_horizontalLayout = self.createHorizontalLayout(spacing=20)
        self.Attendance_Time_horizontalLayout = self.createHorizontalLayout(spacing=20)

        # Add Class Duration label and slider
        self.class_duration_label = self.createLabel(Frame, "class_duration_label", "Class Duration")
        self.class_duration_labeledSlider = LabeledSlider(
            0, self.max_class_hour, subject[3], Frame)
        self.class_duration_horizontalLayout.addWidget(self.class_duration_label)
        self.class_duration_horizontalLayout.addWidget(self.class_duration_labeledSlider)
        self.layout_container_horizontalLayout.addLayout(self.class_duration_horizontalLayout)

        # Add Student Attendance Time label and slider
        self.Attendance_Time_label = self.createLabel(
            Frame, "Attendance_Time_label", "Student Attendance Time")
        self.Attendance_Time_labeledSlider = LabeledSlider(
            0, self.max_class_hour, subject[3], Frame)
        self.Attendance_Time_horizontalLayout.addWidget(self.Attendance_Time_label)
        self.Attendance_Time_horizontalLayout.addWidget(self.Attendance_Time_labeledSlider)
        self.layout_container_horizontalLayout.addLayout(self.Attendance_Time_horizontalLayout)

        self.verticalLayout.addLayout(self.layout_container_horizontalLayout)

        self.retranslateUi(Frame, subject)
        QMetaObject.connectSlotsByName(Frame)

    def createCheckBox(self, parent):
        checkBox = QCheckBox(parent)
        checkBox.setObjectName(u"checkBox")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        checkBox.setFont(font)
        return checkBox

    def createHorizontalLayout(self, spacing=0, margins=None):
        layout = QHBoxLayout()
        layout.setSpacing(spacing)
        if margins:
            layout.setContentsMargins(*margins)
        return layout

    def createLabel(self, parent, object_name, text):
        label = QLabel(parent)
        label.setObjectName(object_name)
        label.setText(QCoreApplication.translate("Frame", text, None))
        return label

    def retranslateUi(self, Frame, subject):
        Frame.setWindowTitle(
            QCoreApplication.translate("Frame", u"Frame", None))
        self.checkBox.setText(QCoreApplication.translate(
            "Frame", f"{subject[0]}) {subject[1]}", None))
