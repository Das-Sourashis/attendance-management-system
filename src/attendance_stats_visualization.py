# Visualizes monthly attendance statistics.

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import QGridLayout, QScrollArea, QVBoxLayout, QWidget, QFrame, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import textwrap
import numpy as np
import matplotlib.pyplot as plt
import database_functions as db


class Ui_Attendance_stats_visualization(object):
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
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 280))
        self.scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scroll_layout.setObjectName(u"scroll_layout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)

        subject_total,attendance_dict = db.month_wise_attendance()
        self.add_attendance_visualization("Total Attendance ", subject_total)
        for month_year, data in attendance_dict.items():
            month, year = month_year
            self.add_attendance_visualization(f"Attendance for Month {month}/{year}", data)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi


    def add_attendance_visualization(self, month_year_label, data):
        month_frame = self.create_month_frame()
        fig, ax = self.create_figure_and_axes(month_year_label)
        self.plot_data(ax, data)
        self.add_labels_and_legend(ax)
        self.adjust_plot_layout(ax, fig)
        canvas = self.create_canvas(fig)
        self.add_canvas_to_frame(canvas, month_frame)

    def create_month_frame(self):
        month_frame = QFrame()
        month_frame.setFrameShape(QFrame.StyledPanel)
        month_frame.setLineWidth(2)
        month_frame.setFixedHeight(450)
        self.scroll_layout.addWidget(month_frame)
        return month_frame

    def create_figure_and_axes(self, month_year_label):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_title(month_year_label)
        return fig, ax

    def plot_data(self, ax, data):
        subjects = [entry[0] for entry in data]
        student_time = [entry[1] for entry in data]
        total_duration = [entry[2] for entry in data]

        x = np.arange(len(subjects))
        width = 0.35
        self.bars1 = ax.bar(x - width/2, student_time, width, label='Student Attendance')
        self.bars2 = ax.bar(x + width/2, total_duration, width, label='Total Duration')
        
        self.add_value_labels(ax, self.bars1, student_time, 'blue')
        self.add_value_labels(ax, self.bars2, total_duration, 'orange')
        self.add_percentage_labels(ax, self.bars1, student_time, total_duration)

        self.add_subject_labels(ax, x, subjects)

    def add_percentage_labels(self, ax, bars, student_time, total_duration):
        max_height = max(max(student_time), max(total_duration))
        for bar, st, td in zip(bars, student_time, total_duration):
            if td > 0:
                percentage = (st / td) * 100
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, height + (max_height * 0.07), f'{percentage:.1f}%',
                        ha='center', va='bottom', fontsize=8, color='green')
            else:
                ax.text(bar.get_x() + bar.get_width() / 2, (max_height * 0.07), 'N/A',
                        ha='center', va='bottom', fontsize=8, color='red')
        
        # Ensure y-axis limit accommodates all labels
        ax.set_ylim(0, max_height * 1.15)  # Increase top limit by 15%


                
    def add_value_labels(self, ax, bars, values, color):
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height, f'{value}',
                    ha='center', va='bottom', fontsize=10, color=color)

    def add_subject_labels(self, ax, x, subjects):
        wrapped_subjects = [textwrap.fill(subject, width=15) for subject in subjects]
        ax.set_xticks(x)
        ax.set_xticklabels([])
        for i, subject in enumerate(wrapped_subjects):
            ax.text(i, ax.get_ylim()[0] - 0.1 * (ax.get_ylim()[1] - ax.get_ylim()[0]), 
                    subject, ha='center', va='top', rotation=0, fontsize=8)

    def add_labels_and_legend(self, ax):
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Time (hours)')
        ax.legend()

    def adjust_plot_layout(self, ax, fig):
        ax.set_xlim(-0.5, len(ax.get_xticks()) - 0.5)
        plt.subplots_adjust(bottom=0.2, top=0.9)

    def create_canvas(self, fig):
        canvas = FigureCanvas(fig)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry()
        return canvas

    def add_canvas_to_frame(self, canvas, frame):
        layout = QVBoxLayout(frame)
        layout.addWidget(canvas)
