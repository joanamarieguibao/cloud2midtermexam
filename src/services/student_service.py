import json
import os
from datetime import datetime

from src.models.student import Student


class StudentService:

    def __init__(self, data_file="data/students.json"):
        self.data_file = data_file
        self.create_data_file()

    def create_data_file(self):
        folder = os.path.dirname(self.data_file)

        if folder:
            os.makedirs(folder, exist_ok=True)

        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as file:
                json.dump([], file, indent=4)

    def load_students(self):
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self, students):
        with open(self.data_file, "w") as file:
            json.dump(students, file, indent=4)

    def add_student(self, student_data):

        students = self.load_students()

        student_id = str(
            student_data.get("student_id", "")
        ).strip()

        if len(student_id) != 7 or not student_id.isdigit():
            raise ValueError(
                "Student ID must contain exactly 7 digits."
            )

        for student in students:
            if student["student_id"] == student_id:
                raise ValueError(
                    "Student ID already exists."
                )

        student = Student(
            student_id,
            student_data["name"],
            student_data["email"],
            student_data["course"],
            student_data["year_level"]
        )

        students.append(student.to_dict())
        self.save_students(students)

        return student.to_dict()

    def get_all_students(self):
        return self.load_students()

    def get_student(self, student_id):

        students = self.load_students()

        for student in students:
            if student["student_id"] == student_id:
                return student

        return None

    def update_student(self, student_id, data):

        students = self.load_students()

        for student in students:

            if student["student_id"] == student_id:

                for key, value in data.items():
                    if value:
                        student[key] = value

                student["updated_at"] = (
                    datetime.now().isoformat()
                )

                self.save_students(students)

                return student

        return None

    def delete_student(self, student_id):

        students = self.load_students()

        original_count = len(students)

        students = [
            student
            for student in students
            if student["student_id"] != student_id
        ]

        self.save_students(students)

        return len(students) < original_count

    def search_students(self, keyword):

        students = self.load_students()

        keyword = keyword.lower().strip()

        results = []

        for student in students:

            if (
                keyword in student["student_id"].lower()
                or keyword in student["name"].lower()
                or keyword in student["email"].lower()
                or keyword in student["course"].lower()
            ):
                results.append(student)

        return results