from src.services.student_service import StudentService
from src.utils.logger import create_logger


class StudentInformationSystem:

    def __init__(self):

        self.service = StudentService()
        self.logger = create_logger()

    def menu(self):

        print("\n==============================")
        print("   STUDENT INFORMATION SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Search Student")
        print("7. Exit")
        print("==============================")

    def add_student(self):

        print("\n--- Add Student ---")

        student_id = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")
        course = input("Course: ")
        year_level = input("Year Level: ")

        data = {
            "student_id": student_id,
            "name": name,
            "email": email,
            "course": course,
            "year_level": year_level
        }

        try:

            student = self.service.add_student(data)

            self.logger.info(
                f"Added student {student['student_id']}"
            )

            print("\nStudent added successfully.")

        except ValueError as error:

            print(f"\nError: {error}")

    def view_students(self):

        print("\n--- All Students ---")

        students = self.service.get_all_students()

        if not students:

            print("No students found.")
            return

        for student in students:

            print(
                f"\nID: {student['student_id']}"
            )

            print(
                f"Name: {student['name']}"
            )

            print(
                f"Email: {student['email']}"
            )

            print(
                f"Course: {student['course']}"
            )

            print(
                f"Year Level: {student['year_level']}"
            )

    def view_student(self):

        print("\n--- View Student ---")

        student_id = input("Student ID: ")

        student = self.service.get_student(student_id)

        if student:

            print("\nStudent Information")

            print(f"ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Email: {student['email']}")
            print(f"Course: {student['course']}")
            print(f"Year Level: {student['year_level']}")

        else:

            print("Student not found.")

    def update_student(self):

        print("\n--- Update Student ---")

        student_id = input("Student ID: ")

        student = self.service.get_student(student_id)

        if not student:

            print("Student not found.")
            return

        print("Press Enter to keep the current value.")

        name = input(
            f"Name [{student['name']}]: "
        )

        email = input(
            f"Email [{student['email']}]: "
        )

        course = input(
            f"Course [{student['course']}]: "
        )

        year_level = input(
            f"Year Level [{student['year_level']}]: "
        )

        updates = {
            "name": name,
            "email": email,
            "course": course,
            "year_level": year_level
        }

        updated = self.service.update_student(
            student_id,
            updates
        )

        if updated:

            self.logger.info(
                f"Updated student {student_id}"
            )

            print("Student updated successfully.")

    def delete_student(self):

        print("\n--- Delete Student ---")

        student_id = input("Student ID: ")

        student = self.service.get_student(student_id)

        if not student:

            print("Student not found.")
            return

        print(f"Student: {student['name']}")

        confirm = input(
            "Delete this student? (y/n): "
        )

        if confirm.lower() != "y":

            print("Delete cancelled.")
            return

        deleted = self.service.delete_student(
            student_id
        )

        if deleted:

            self.logger.info(
                f"Deleted student {student_id}"
            )

            print("Student deleted successfully.")

    def search_student(self):

        print("\n--- Search Student ---")

        keyword = input(
            "Enter ID, Name, Email, or Course: "
        )

        results = self.service.search_students(
            keyword
        )

        if not results:

            print("No students found.")
            return

        print("\n--- Search Results ---")

        for student in results:

            print(
                f"ID: {student['student_id']}, "
                f"Name: {student['name']}, "
                f"Course: {student['course']}"
            )

    def run(self):

        while True:

            self.menu()

            choice = input(
                "Enter your choice: "
            )

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.view_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.search_student()

            elif choice == "7":

                print("\nThank you for using the system.")
                break

            else:

                print(
                    "Invalid choice. Please try again."
                )


if __name__ == "__main__":

    app = StudentInformationSystem()

    app.run()