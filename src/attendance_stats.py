# Handles monthly attendance statistics calculations.

from PySide6.QtCore import QCoreApplication, Qt, QRect, QMetaObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QGridLayout, QScrollArea, QSizePolicy,
                               QVBoxLayout, QWidget, QLabel, QTableWidget, QTableWidgetItem,
                               QAbstractItemView, QHeaderView)

import database_functions as db

class Ui_Attendance_stats():
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 280))
        self.scrollAreaLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)

        subject_total,attendance_dict = db.month_wise_attendance()
        self.add_month_table("Total Attendance ", subject_total)
        for month_year, data in attendance_dict.items():
            month, year = month_year
            self.add_month_table(f"Attendance for Month {month}/{year}", data)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi


    def add_month_table(self, month, data):
        self.add_month_label(month)
        tableWidget = self.create_table_widget(data)
        self.populate_table_with_data(tableWidget, data)
        self.add_percentage_row(tableWidget, data)
        self.scrollAreaLayout.addWidget(tableWidget)

    def add_month_label(self, month_text):
        month_label = QLabel(self.scrollAreaWidgetContents)
        month_label.setObjectName(u"month_label")
        month_label.setText(month_text)
        month_label_font = QFont()
        month_label_font.setFamilies([u"Arial"])
        month_label_font.setPointSize(12)
        month_label_font.setBold(True)
        month_label.setFont(month_label_font)
        self.scrollAreaLayout.addWidget(month_label)

    def create_table_widget(self, data):
        tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        tableWidget.setObjectName(u"tableWidget")
        tableWidget.setEnabled(True)
        tableWidget.setRowCount(4)  # Include an additional row for headers and one for percentage
        tableWidget.setColumnCount(len(data) + 1)  # Include an additional column for labels
        table_font = QFont()
        table_font.setFamilies([u"Arial"])
        table_font.setPointSize(10)
        table_font.setBold(True)
        tableWidget.setFont(table_font)
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tableWidget.setWordWrap(True)

        # Apply yellow-green theme
        tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #f0f8e4; /* Light yellow-green background */
                color: #000000; /* Black text color for contrast */
            }
            QTableWidget::item {
                padding: 5px;
                border: 1px solid #d0e1a7; /* Soft green border */
            }
            QHeaderView::section {
                background-color: #d0e1a7; /* Light green header */
                color: #000000; /* Black header text color */
                border: 1px solid #b0b0b0; /* Grey border for header */
            }
        """)
        tableWidget.horizontalHeader().setVisible(False)
        tableWidget.verticalHeader().setVisible(False)

        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Set column widths and enable text wrapping
        max_width = 300  # Maximum column width in pixels
        for col in range(len(data) + 1):
            tableWidget.setColumnWidth(col, max_width)
            tableWidget.horizontalHeader().setMaximumSectionSize(max_width)
            tableWidget.horizontalHeader().setMinimumSectionSize(100)

        # Add labels to the first column
        labels = ["Subject", "Student's Attendance", "Class Duration"]
        for row, label in enumerate(labels):
            label_item = QTableWidgetItem(label)
            label_item.setFont(table_font)
            label_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            label_item.setToolTip(label)  # Optional: set tooltip for full label view
            tableWidget.setItem(row, 0, label_item)

        return tableWidget

    def populate_table_with_data(self, tableWidget, data):
        for col, entry in enumerate(data, start=1):
            subject_item = QTableWidgetItem(entry[0])
            attendance_item = QTableWidgetItem(str(entry[1]))
            duration_item = QTableWidgetItem(str(entry[2]))

            # Set text alignment and enable word wrapping
            for item in [subject_item, attendance_item, duration_item]:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item.setToolTip(item.text())  # Optional: set tooltip for full text view

            tableWidget.setItem(0, col, subject_item)
            tableWidget.setItem(1, col, attendance_item)
            tableWidget.setItem(2, col, duration_item)

    def add_percentage_row(self, tableWidget, data):
        total_attendance = sum(item[1] for item in data)
        total_duration = sum(item[2] for item in data)
        attendance_percentage = (total_attendance / total_duration) * 100 if total_duration != 0 else 0

        percentage_item = QTableWidgetItem(f"Attendance Percentage = {round(attendance_percentage, 5)}%")
        percentage_item.setFont(tableWidget.font())
        # percentage_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        tableWidget.setItem(3, 0, percentage_item)
        tableWidget.setSpan(3, 0, 1, len(data) + 1)  # Span across all columns

        # Adjust row heights to fit content
        tableWidget.resizeRowsToContents()

        # Set fixed height for the table
        tableWidget.setFixedHeight(220)