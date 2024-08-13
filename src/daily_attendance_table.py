from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, QDate)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QAbstractItemView, QDateEdit, QFrame, QHBoxLayout,
                               QLabel, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView)

import database_functions as db
import calendar


class Ui_Daily_Attendance_Table(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(777, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headFrame = QFrame(Form)
        self.headFrame.setObjectName(u"headFrame")
        self.headFrame.setStyleSheet(u"""#headFrame {
                                        background-color: rgb(1, 107, 13);
                                        border-radius: 10px;
                                    }""")
        self.headFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.headFrame_horizontalLayout = QHBoxLayout(self.headFrame)
        self.headFrame_horizontalLayout.setObjectName(u"headFrame_horizontalLayout")
        self.start_date_label = QLabel(self.headFrame)
        self.start_date_label.setObjectName(u"start_date_label")
        font = QFont()
        font.setFamilies([u"Cascadia Code SemiBold"])
        font.setPointSize(12)
        font.setBold(True)
        self.start_date_label.setFont(font)

        self.headFrame_horizontalLayout.addWidget(self.start_date_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.start_date_dateEdit = QDateEdit(self.headFrame)
        self.start_date_dateEdit.setObjectName(u"start_date_dateEdit")
        self.start_date_dateEdit.setFont(font)
        self.start_date_dateEdit.setAcceptDrops(False)
        self.start_date_dateEdit.setCalendarPopup(True)
        self.start_date_dateEdit.setMinimumDate(db.get_date())
        self.start_date_dateEdit.setMaximumDate(QDate.currentDate())
        self.start_date_dateEdit.setDate(db.get_date())

        self.headFrame_horizontalLayout.addWidget(self.start_date_dateEdit)

        self.end_date_label = QLabel(self.headFrame)
        self.end_date_label.setObjectName(u"end_date_label")
        self.end_date_label.setFont(font)
        self.end_date_label.setMargin(10)
        self.end_date_label.setIndent(1)

        self.headFrame_horizontalLayout.addWidget(self.end_date_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.end_date_dateEdit = QDateEdit(self.headFrame)
        self.end_date_dateEdit.setObjectName(u"end_date_dateEdit")
        self.end_date_dateEdit.setFont(font)
        self.end_date_dateEdit.setCalendarPopup(True)
        self.end_date_dateEdit.setMinimumDate(db.get_date())
        self.end_date_dateEdit.setMaximumDate(QDate.currentDate())
        self.end_date_dateEdit.setDate(QDate.currentDate())

        self.headFrame_horizontalLayout.addWidget(self.end_date_dateEdit)

        self.range_search_pushButton = QPushButton(self.headFrame)
        self.range_search_pushButton.setObjectName(u"range_search_pushButton")

        button_font = QFont()
        button_font.setFamilies([u"Cascadia Mono SemiBold"])
        button_font.setPointSize(10)
        button_font.setBold(True)

        self.range_search_pushButton.setFont(button_font)
        self.range_search_pushButton.clicked.connect(self.insert_data)
        self.range_search_pushButton.setStyleSheet(u"""#headFrame QPushButton {
                                            background-color: blue;
                                            color: white;
                                            border: 2px solid darkblue;
                                            border-radius: 5px;
                                            padding: 5px 10px;
                                            margin-left: 30px;
                                        }

                                        #headFrame QPushButton:hover {
                                            background-color: lightblue;
                                            color: black;
                                            border-color: blue;
                                        }

                                        #headFrame QPushButton:pressed {
                                            background-color: darkblue;
                                            border-color: darkblue;
                                        }""")

        self.headFrame_horizontalLayout.addWidget(self.range_search_pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.all_search_pushButton = QPushButton(self.headFrame)
        self.all_search_pushButton.setObjectName(u"all_search_pushButton")
        self.all_search_pushButton.setFont(button_font)
        self.all_search_pushButton.clicked.connect(self.get_all)
        self.all_search_pushButton.setStyleSheet(u"""#headFrame QPushButton {
                                            background-color: blue;
                                            color: white;
                                            border: 2px solid darkblue;
                                            border-radius: 5px;
                                            padding: 5px 10px;
                                        }

                                        #headFrame QPushButton:hover {
                                            background-color: lightblue;
                                            color: black;
                                            border-color: blue;
                                        }

                                        #headFrame QPushButton:pressed {
                                            background-color: darkblue;
                                            border-color: darkblue;
                                        }""")

        self.headFrame_horizontalLayout.addWidget(self.all_search_pushButton, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalLayout_2.addWidget(self.headFrame)

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setStyleSheet(u"""QTableWidget {
                                            background-color: #f0f0f0;
                                            border: 1px solid #dddddd;
                                        }
                                        
                                        QHeaderView::section {
                                            background-color: #4CAF50;
                                            color: white;
                                            padding: 4px;
                                            font-size: 12px;
                                            text-align: center;
                                            font: 700 12pt "Arial";
                                        }
                                        
                                        QTableView QScrollBar:vertical {
                                            background: #f0f0f0;
                                            width: 10px;
                                            margin: 0px 0px 0px 0px;
                                        }
                                        
                                        QTableWidget::item {
                                            background-color: #ffffff;
                                            color: black;
                                            font-size: 14px;
                                            padding: 4px;
                                            border-bottom: 1px solid #dddddd;
                                            margin: 0;
                                            height: auto; /* Allow automatic height adjustment for wrapped text */
                                            text-align: center; /* Center align the text */
                                        }
                                        
                                        QTableWidget::item:selected {
                                            background-color: #ccffcc;
                                        }""")
        self.tableWidget.setFrameShape(QFrame.Shape.WinPanel)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.tableWidget.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setHorizontalHeaderLabels([])  # Remove the default horizontal header
        # self.tableWidget.horizontalHeader().hide()  # Hide the horizontal header
        # self.tableWidget.horizontalHeader().setMaximumSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # Enable interactive resizing

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.set_header()
        self.insert_data()

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.start_date_label.setText(QCoreApplication.translate(
            "Form", u"Start Date : ", None))
        self.end_date_label.setText(QCoreApplication.translate(
            "Form", u"End Date :", None))
        self.range_search_pushButton.setText(QCoreApplication.translate(
            "Form", u"Search In Range", None))
        self.all_search_pushButton.setText(
            QCoreApplication.translate("Form", u"Search All", None))

    # retranslateUi

    def set_header(self):
        subjects = db.get_subject_name()
        table_header = ["Date", "Day"]

        for subject_tuple in subjects:
            table_header.append(subject_tuple[0])

        self.tableWidget.setColumnCount(len(table_header))
        self.tableWidget.insertRow(0)  # Insert the first row for headers
        for col, header in enumerate(table_header):
            item = QTableWidgetItem(header)
            item.setBackground(Qt.GlobalColor.green)  # Set background color
            item.setForeground(Qt.GlobalColor.white)  # Set text color
            item.setFont(QFont("Arial", 12, QFont.Weight.Bold))  # Set font style
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Align text to center
            self.tableWidget.setItem(0, col, item)

    def get_all(self):
        self.start_date_dateEdit.setDate(db.get_date())
        self.end_date_dateEdit.setDate(QDate.currentDate())
        self.insert_data()

    def insert_data(self):
        self.tableWidget.setRowCount(1)  # Keep the header row
        start_date = self.start_date_dateEdit.date().toPython()
        end_date = self.end_date_dateEdit.date().toPython()
        response = db.search_in_date_range(start_date, end_date)
        row = 1  # Start row counter from 1

        for record in response:
            date_str = record[0].strftime("%Y-%m-%d")
            if self.tableWidget.rowCount() == 1 or self.tableWidget.item(row - 1, 0).text() != date_str:
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(date_str))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(calendar.day_name[record[1] - 1]))
                row += 1

            cell_item = QTableWidgetItem(f'{record[4]}/{record[3]}')
            cell_item.setFlags(cell_item.flags() | Qt.ItemFlag.ItemIsEditable)
            cell_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget.setItem(row - 1, record[2] + 1, cell_item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
