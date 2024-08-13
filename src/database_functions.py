#  Contains database-related functions.

from sqlalchemy import select, func, update, delete, insert
from datetime import datetime
from PySide6.QtCore import QDate
from database_setup import session, Subject, Class, Date


def get_date():
    stmt = select(Date.sdate)
    result = session.execute(stmt).all()
    
    # If the result is empty, return today's date
    if not result or result[0][0] is None:
        today = datetime.today()
        return QDate(today.year, today.month, today.day)
    
    return QDate(result[0][0].year, result[0][0].month, result[0][0].day)

# print(get_date())


def get_subjects():
    query = select(Subject.sid, Subject.subjectname, Subject.teacher, Subject.type).order_by(Subject.sid)
    result = session.execute(query).fetchall()
    return result


def daily_data_insert(data):
    for row in data:
        session.add(Class(row))
    session.commit()


def update_daily_data(data: list[tuple[datetime, int, int, int, int]], date: str):
    stmt = delete(Class).where(Class.date == date)
    session.execute(stmt)
    session.commit()

    stmt = insert(Class).values(data)
    session.execute(stmt)
    session.commit()


def any_day_attendance_list(date):
    stmt = select(Subject.sid, Subject.subjectname, Subject.teacher, Class.studenttime, Class.duration)\
        .select_from(Class).join(Subject, Class.sid == Subject.sid)\
        .filter(Class.date == date)
    results = session.execute(stmt).fetchall()
    return results


def any_day_total_attendance(date):
    stmt = select(
        func.sum(Class.studenttime).label('total_studenttime'),
        func.sum(Class.duration).label('total_duration')
    ).select_from(Class).join(Subject, Class.sid == Subject.sid).filter(Class.date == date)

    results = session.execute(stmt).fetchall()
    return results


def month_wise_attendance():
    stmt = select(
        func.extract('month', Class.date).label('month'),
        func.extract('year', Class.date).label('year'),
        Subject.subjectname,
        func.sum(Class.studenttime).label('total_student_time'),
        func.sum(Class.duration).label('total_duration')
    ).select_from(
        Subject
    ).join(
        Class, Class.sid == Subject.sid
    ).group_by(
        func.extract('month', Class.date),
        func.extract('year', Class.date),
        Subject.subjectname
    ).order_by(
        func.extract('year', Class.date),
        func.extract('month', Class.date),
        Subject.subjectname
    )

    results = session.execute(stmt).fetchall()
    all_subjects = [subject[0] for subject in session.query(Subject.subjectname).order_by(Subject.subjectname).all()]

    attendance_dict = {}
    subject_totals = {subject: [0, 0] for subject in all_subjects}
    
    for result in results:
        month, year, subjectname, total_student_time, total_duration = result
        key = (month, year)

        if key not in attendance_dict:
            attendance_dict[key] = {subject: [0, 0] for subject in all_subjects}

        attendance_dict[key][subjectname] = [total_student_time, total_duration]
        subject_totals[subjectname][0] += total_student_time
        subject_totals[subjectname][1] += total_duration

    for key in attendance_dict:
        attendance_dict[key] = [[subject, *attendance_dict[key][subject]] for subject in all_subjects]
        total_month_attendance = sum(item[1] for item in attendance_dict[key])
        total_month_class_duration = sum(item[2] for item in attendance_dict[key])
        attendance_dict[key].append(["Total Month Attendance", total_month_attendance, total_month_class_duration])

    subject_totals_list = [[subject, *subject_totals[subject]] for subject in all_subjects]
    total_attendance = sum(item[1] for item in subject_totals_list)
    total_duration = sum(item[2] for item in subject_totals_list)
    subject_totals_list.append(["Total Attendance", total_attendance, total_duration])

    return subject_totals_list, attendance_dict

# print(month_wise_attendance())

def get_subject_name():
    stmt = select(Subject.subjectname, Subject.sid).order_by(Subject.sid)
    results = session.execute(stmt).fetchall()
    return results


def get_all_classes():
    stmt = select(Class.date, Class.day, Class.sid, Class.duration, Class.studenttime).order_by(Class.date)
    results = session.execute(stmt).fetchall()
    return results


def search_in_date_range(start, end):
    stmt = select(Class.date, Class.day, Class.sid, Class.duration, Class.studenttime).filter(
        Class.date.between(start, end)).order_by(Class.date)
    results = session.execute(stmt).fetchall()
    return results


def clear_existing_routine_and_create_new(value, date):
    set_date(date)

    stmt = delete(Class)
    session.execute(stmt)

    stmt = delete(Subject)
    session.execute(stmt)

    stmt = insert(Subject).values(value)
    session.execute(stmt)

    session.commit()


def set_date(date):
    stmt = delete(Date)
    session.execute(stmt)

    stmt = insert(Date).values(sdate=date)
    session.execute(stmt)

    session.commit()


def edit_subjects(data):
    for row in data:
        subject_id = row[0]
        updated_data = {
            'subjectname': row[1],
            'teacher': row[2],
            'type': row[3],
        }
        stmt = update(Subject).where(Subject.sid == subject_id).values(updated_data)
        session.execute(stmt)

    session.commit()


def edit_date(date):
    stmt = delete(Class).where(Class.date < date)
    session.execute(stmt)
    session.commit()

    stmt = update(Date).values(sdate=date)
    session.execute(stmt)
    session.commit()
