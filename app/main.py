from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Hello!"}


@app.get("/students")
def get_all_students(course: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if course:
        result_list = [student for student in students if student["course"] == course]
        return result_list
    return students


@app.get("/students/{course}")
def get_all_students_course(course: Optional[int] = None, major: Optional[str] = None,
                            enrollment_year: Optional[int] = 2018):
    students = json_to_dict_list(path_to_json)
    filtered_students = [student for student in students if student["course"] == course]

    if major:
        filtered_students = [student for student in filtered_students if student["major"].lower() == major.lower()]

    if enrollment_year:
        filtered_students = [student for student in filtered_students if student["enrollment_year"] == enrollment_year]

    return filtered_students


@app.get("/student/{student_id}")
def get_student_by_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student


@app.get("/student")
def get_student_by_param_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student
