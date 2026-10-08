import os
import tempfile
import unittest

from src.services.student_service import StudentService


class TestStudentService(unittest.TestCase):

    def setUp(self):

        self.file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".json"
        )

        self.file.close()

        self.service = StudentService(
            self.file.name
        )

    def tearDown(self):

        if os.path.exists(self.file.name):
            os.remove(self.file.name)

    def sample_student(self):

        return {
            "student_id": "2401478",
            "name": "Joan Guibao",
            "email": "joan@example.com",
            "course": "BSIT",
            "year_level": "3"
        }

    def test_add_student(self):

        student = self.service.add_student(
            self.sample_student()
        )

        self.assertEqual(
            student["student_id"],
            "2401478"
        )

        self.assertEqual(
            student["name"],
            "Joan Guibao"
        )

    def test_get_student(self):

        self.service.add_student(
            self.sample_student()
        )

        student = self.service.get_student(
            "2401478"
        )

        self.assertIsNotNone(student)

        self.assertEqual(
            student["student_id"],
            "2401478"
        )

    def test_update_student(self):

        self.service.add_student(
            self.sample_student()
        )

        student = self.service.update_student(
            "2401478",
            {
                "name": "Joan Marie Guibao"
            }
        )

        self.assertIsNotNone(student)

        self.assertEqual(
            student["name"],
            "Joan Marie Guibao"
        )

    def test_delete_student(self):

        self.service.add_student(
            self.sample_student()
        )

        result = self.service.delete_student(
            "2401478"
        )

        self.assertTrue(result)

        self.assertIsNone(
            self.service.get_student(
                "2401478"
            )
        )

    def test_search_student(self):

        self.service.add_student(
            self.sample_student()
        )

        results = self.service.search_students(
            "Joan"
        )

        self.assertEqual(
            len(results),
            1
        )

        self.assertEqual(
            results[0]["student_id"],
            "2401478"
        )


if __name__ == "__main__":
    unittest.main()