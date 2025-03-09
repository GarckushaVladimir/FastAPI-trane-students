from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.database import async_session_maker
from app.students.models import Student, Major
from app.dao.base import BaseDAO


class StudentDAO(BaseDAO):
    model = Student

    @classmethod
    async def find_full_data(cls, student_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.major)).filter_by(id=student_id)
            result_student = await session.execute(query)
            student_info = result_student.scalar_one_or_none()

            if not student_info:
                return None

            student_data = student_info.to_dict()
            student_data["major"] = student_info.major.major_name

            return student_data
