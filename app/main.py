from fastapi import FastAPI, Depends, HTTPException
from utils import json_to_dict_list
# import os
from typing import Optional, List
from studentModel import *
from database import *


# script_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(script_dir)
# path_to_json = os.path.join(parent_dir, 'students.json')

class RBStudent:
    def __init__(self, course: Optional[int] = None, major: Optional[str] = None,
                 enrollment_year: Optional[int] = 2018):
        self.course = course
        self.major = major
        self.enrollment_year = enrollment_year


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Hello!"}


@app.get("/students")
def get_all_students(course: Optional[int] = None):
    # students = json_to_dict_list(path_to_json)
    students = json_to_dict_list()
    if course:
        result_list = [student for student in students if student["course"] == course]
        return result_list
    return students


@app.get("/students/{course}")
def get_all_students_course(request_body: RBStudent = Depends()) -> List[SStudent]:
    # students = json_to_dict_list(path_to_json)
    students = json_to_dict_list()
    filtered_students = [student for student in students if student["course"] == request_body.course]

    if request_body.major:
        filtered_students = [student for student in filtered_students if
                             student["major"].lower() == request_body.major.lower()]

    if request_body.enrollment_year:
        filtered_students = [student for student in filtered_students if
                             student["enrollment_year"] == request_body.enrollment_year]

    return filtered_students


@app.get("/student/{student_id}")
def get_student_by_id(student_id: int) -> SStudent:
    # students = json_to_dict_list(path_to_json)
    students = json_to_dict_list()
    for student in students:
        if student["student_id"] == student_id:
            return student


@app.get("/student")
def get_student_by_param_id(student_id: int) -> SStudent:
    # students = json_to_dict_list(path_to_json)
    students = json_to_dict_list()
    for student in students:
        if student["student_id"] == student_id:
            return student


@app.post("/add_student")
def add_student_handler(student: SStudent):
    student_dict = student.dict()
    check = add_student(student_dict)
    if check:
        return {"message": "Студент успешно добавлен!"}
    else:
        return {"message": "Ошибка при добавлении студента"}


@app.put("/update_student")
def update_student_handler(filter_student: SUpdateFilter, new_data: SStudentUpdate):
    check = upd_student(filter_student.dict(), new_data.dict())
    if check:
        return {"message": "Информация о студенте успешно обновлена!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при обновлении информации о студенте")


@app.delete("/delete_student")
def delete_student_handler(filter_student: SDeleteFilter):
    check = dell_student(filter_student.key, filter_student.value)
    if check:
        return {"message": "Студент успешно удален!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при удалении студента")
