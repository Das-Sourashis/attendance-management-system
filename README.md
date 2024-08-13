
# Attendance Management System

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Database Schema](#database-schema)

## Introduction

The **Attendance Management System** is a Python application developed primarily using PySide6 for the user interface, SQLAlchemy as the ORM, and SQLite3 for the database. This system is designed for single-student use, allowing a student to manage their subjects for a session or semester, view and edit daily attendance, and generate monthly attendance summaries.

## Features

- **Subject Management**: Save and manage subjects for the current session or semester.
- **Daily Attendance**: Insert and edit attendance for specific days.
- **Routine Management**: Create and edit daily class routines.
- **Monthly Attendance Summary**: Generate and view monthly attendance statistics.

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Das-Sourashis/attendance-management-system.git
   cd attendance-management-system
   ```

2. **Create a Virtual Environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup the Database**:
   No additional setup is required. Running the main application will automatically create the necessary tables if they do not exist.

## Usage

1. **Start the Application**:
   ```bash
   python main.py
   ```

2. **Navigation**:
   - **Home**: View calendar for daily attendance and Insert or edit attendance for a specific day.
   - **Attendance Statistics**: View graphical and tabular attendance summaries.
   - **New Routine**: Add a new routine for the semester.
   - **Edit Routine**: Modify an existing routine.


3. **Menu Actions**:
   - **HOME**: Returns to the main calendar view.
   - **GET DATA**: Provides options for viewing attendance statistics.
   - **SETTINGS**: Allows creating, editing routines, and database management.

4. **Exiting the Application**:
    close the window to exit the application.

## Screenshots

Here are some screenshots of the application:

![Calendar](https://github.com/user-attachments/assets/70a0c756-b04e-4357-b5ae-ed6d0bb11222)
*Calendar view*

![Daily_Attendance](https://github.com/user-attachments/assets/19ee4841-c008-4a23-8f52-26a7e3b82ffb)
*Interface for recording daily attendance*

![Attendance_Statistics](https://github.com/user-attachments/assets/f98fedc1-ee38-4eb0-8d0e-3ccff5afd97d)
*representation of attendance statistics*

![editRoutine](https://github.com/user-attachments/assets/bcf0cae3-e2b8-4a55-8faa-bf812b11dd46)
*Editing and managing class routines*

[Video](https://drive.google.com/file/d/1qTP7AbPbologRRTQI02N9qRgHA1sdusA/view?usp=sharing)  
*Demo video of the Attendance Management System*

## Database Schema

The database schema includes the following tables:

- **subjects**: Stores subject information such as ID, name, teacher, and type.
  - **Columns**:
    - `sid` (Integer, Primary Key): Subject ID.
    - `subjectname` (String, 50, Unique, Not Null): Name of the subject.
    - `teacher` (String, 50, Not Null): Name of the teacher.
    - `type` (String, 1, Not Null): Type of subject (e.g., Lecture, Lab).

- **classes**: Records attendance and routine data for each subject on a particular date.
  - **Columns**:
    - `date` (Date, Primary Key): Date of the class.
    - `day` (Integer, Not Null): Day of the week (1-7).
    - `sid` (Integer, Foreign Key to `subjects.sid`, Primary Key): Subject ID.
    - `duration` (Integer, Not Null): Duration of the class.
    - `studenttime` (Integer, Not Null): Time student spent in the class.

- **startdate**: Holds the start date of the session or semester.
  - **Columns**:
    - `sdate` (Date, Primary Key): Start date of the session.

#




