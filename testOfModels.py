from studentModel import SStudent
from pydantic import ValidationError
from datetime import date


def test_valid_student(data: dict) -> None:
    try:
        student = SStudent(**data)
        print(student)
    except ValidationError as e:
        print(f"Error of validation: {e}")


student_data = {
    "student_id": 1,
    "phone_number": "+1234567890",
    "first_name": "Иван",
    "last_name": "Иванов",
    "date_of_birth": date(2000, 1, 1),
    "email": "ivan.ivanov@example.com",
    "address": "Москва, ул. Пушкина, д. Колотушкина",
    "enrollment_year": 2022,
    "major": "Информатика",
    "course": 3,
    "special_notes": "Увлекается программированием"
}

test_valid_student(student_data)
