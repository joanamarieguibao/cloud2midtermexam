from datetime import datetime


class Student:

    def __init__(
        self,
        student_id,
        name,
        email,
        course,
        year_level
    ):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.course = course
        self.year_level = year_level
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "course": self.course,
            "year_level": self.year_level,
            "created_at": self.created_at
        }