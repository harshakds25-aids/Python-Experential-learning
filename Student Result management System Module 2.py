# ==============================
# STUDENT CLASS
# ==============================
import os
import json
class Student:

    def __init__(self, roll_no, name, course, semester, marks):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.semester = semester
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_percentage(self):
        total = self.calculate_total()
        maximum = len(self.marks) * 100

        if maximum == 0:
            return 0

        return (total / maximum) * 100

    def calculate_grade(self):

        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        elif percentage >= 40:
            return "E"
        else:
            return "F"

    def get_status(self):

        for mark in self.marks.values():

            if mark < 40:
                return "FAIL"

        return "PASS"

    def to_dict(self):

        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "course": self.course,
            "semester": self.semester,
            "marks": self.marks
        }


# ==============================
# RESULT MANAGEMENT SYSTEM CLASS
# ==============================

class ResultManagementSystem:

    FILE_NAME = "Student.json"

    def __init__(self):
        self.students = {}
        self.load_data()

    # --------------------------
    # LOAD DATA FROM JSON FILE
    # --------------------------

    def load_data(self):

        if os.path.exists(self.FILE_NAME):

            try:

                with open(self.FILE_NAME, "r") as file:
                    data = json.load(file)

                for roll_no, student_data in data.items():

                    self.students[roll_no] = Student(
                        student_data["roll_no"],
                        student_data["name"],
                        student_data["course"],
                        student_data["semester"],
                        student_data["marks"]
                    )

            except (json.JSONDecodeError, KeyError):

                print("Invalid student data file.")

    # --------------------------
    # SAVE DATA TO JSON FILE
    # --------------------------

    def save_data(self):

        data = {}

        for roll_no, student in self.students.items():

            data[roll_no] = student.to_dict()

        with open(self.FILE_NAME, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # --------------------------
    # ADD STUDENT
    # --------------------------

    def add_student(self):

        print("\n========== ADD STUDENT ==========")

        roll_no = input("Enter Roll Number: ").strip()

        if roll_no in self.students:

            print("Student already exists.")
            return

        name = input("Enter Student Name: ").strip()

        course = input("Enter Course/Branch: ").strip()

        semester = input("Enter Semester: ").strip()

        marks = {}

        try:

            number_of_subjects = int(
                input("Enter Number of Subjects: ")
            )

            if number_of_subjects <= 0:

                print("Number of subjects must be greater than 0.")
                return

            for i in range(number_of_subjects):

                subject = input(
                    f"Enter Subject {i + 1} Name: "
                ).strip()

                if subject == "":
                    print("Subject name cannot be empty.")
                    return

                mark = float(
                    input(f"Enter Marks for {subject}: ")
                )

                if mark < 0 or mark > 100:

                    print("Marks must be between 0 and 100.")
                    return

                marks[subject] = mark

        except ValueError:

            print("Invalid input. Please enter a valid number.")
            return

        student = Student(
            roll_no,
            name,
            course,
            semester,
            marks
        )

        self.students[roll_no] = student

        self.save_data()

        print("Student added successfully.")

    # --------------------------
    # VIEW ALL STUDENTS
    # --------------------------

    def view_students(self):

        if not self.students:

            print("\nNo student records found.")
            return

        print("\n========== ALL STUDENTS ==========")

        for student in self.students.values():

            print("--------------------------------")

            print("Roll Number:", student.roll_no)
            print("Name:", student.name)
            print("Course:", student.course)
            print("Semester:", student.semester)

            print(
                "Percentage:",
                f"{student.calculate_percentage():.2f}%"
            )

            print(
                "Grade:",
                student.calculate_grade()
            )

            print(
                "Status:",
                student.get_status()
            )

    # --------------------------
    # SEARCH STUDENT
    # --------------------------

    def search_student(self):

        print("\n========== SEARCH STUDENT ==========")

        roll_no = input("Enter Roll Number: ").strip()

        student = self.students.get(roll_no)

        if student is None:

            print("Student not found.")
            return

        self.display_result(student)

    # --------------------------
    # DISPLAY RESULT
    # --------------------------

    def display_result(self, student):

        print("\n========================================")
        print("           STUDENT RESULT")
        print("========================================")

        print("Roll Number:", student.roll_no)
        print("Name:", student.name)
        print("Course:", student.course)
        print("Semester:", student.semester)

        print("\nSubject-wise Marks")

        for subject, mark in student.marks.items():

            print(f"{subject:<25} {mark:.2f}")

        print("----------------------------------------")

        print(
            "Total Marks:",
            f"{student.calculate_total():.2f}"
        )

        print(
            "Percentage:",
            f"{student.calculate_percentage():.2f}%"
        )

        print(
            "Grade:",
            student.calculate_grade()
        )

        print(
            "Result:",
            student.get_status()
        )

        print("========================================")

    # --------------------------
    # UPDATE STUDENT
    # --------------------------

    def update_student(self):

        print("\n========== UPDATE STUDENT ==========")

        roll_no = input("Enter Roll Number: ").strip()

        student = self.students.get(roll_no)

        if student is None:

            print("Student not found.")
            return

        print("\n1. Update Name")
        print("2. Update Course")
        print("3. Update Semester")
        print("4. Update Marks")

        choice = input("Enter choice: ")

        if choice == "1":

            new_name = input("Enter new name: ").strip()

            if new_name == "":
                print("Name cannot be empty.")
                return

            student.name = new_name

        elif choice == "2":

            new_course = input("Enter new course: ").strip()

            if new_course == "":
                print("Course cannot be empty.")
                return

            student.course = new_course

        elif choice == "3":

            new_semester = input("Enter new semester: ").strip()

            if new_semester == "":
                print("Semester cannot be empty.")
                return

            student.semester = new_semester

        elif choice == "4":

            subject = input("Enter subject: ").strip()

            if subject not in student.marks:

                print("Subject not found.")
                return

            try:

                mark = float(
                    input("Enter new marks: ")
                )

                if mark < 0 or mark > 100:

                    print("Marks must be between 0 and 100.")
                    return

                student.marks[subject] = mark

            except ValueError:

                print("Invalid marks.")
                return

        else:

            print("Invalid choice.")
            return

        self.save_data()

        print("Record updated successfully.")

    # --------------------------
    # DELETE STUDENT
    # --------------------------

    def delete_student(self):

        print("\n========== DELETE STUDENT ==========")

        roll_no = input("Enter Roll Number: ").strip()

        if roll_no not in self.students:

            print("Student not found.")
            return

        confirm = input(
            "Are you sure? (yes/no): "
        ).lower()

        if confirm == "yes":

            del self.students[roll_no]

            self.save_data()

            print("Student deleted successfully.")

        else:

            print("Operation cancelled.")

    # --------------------------
    # GENERATE RESULT REPORT
    # --------------------------

    def generate_report(self):

        print("\n========== GENERATE RESULT REPORT ==========")

        roll_no = input("Enter Roll Number: ").strip()

        student = self.students.get(roll_no)

        if student is None:

            print("Student not found.")
            return

        report_file = f"result_{roll_no}.txt"

        # Create result text file
        with open(report_file, "w") as file:

            file.write("========================================\n")
            file.write("       STUDENT RESULT REPORT\n")
            file.write("========================================\n\n")

            file.write(
                f"Roll Number : {student.roll_no}\n"
            )

            file.write(
                f"Name        : {student.name}\n"
            )

            file.write(
                f"Course      : {student.course}\n"
            )

            file.write(
                f"Semester    : {student.semester}\n\n"
            )

            file.write("Subject-wise Marks\n")
            file.write("------------------\n")

            for subject, mark in student.marks.items():

                file.write(
                    f"{subject:<25} {mark:.2f}\n"
                )

            file.write("\n")

            file.write(
                f"Total Marks : "
                f"{student.calculate_total():.2f}\n"
            )

            file.write(
                f"Percentage  : "
                f"{student.calculate_percentage():.2f}%\n"
            )

            file.write(
                f"Grade       : "
                f"{student.calculate_grade()}\n"
            )

            file.write(
                f"Result      : "
                f"{student.get_status()}\n"
            )

            file.write("\n")
            file.write("========================================\n")

        # Confirm file generation
        print("\nReport generated:", report_file)

        # Read the generated file
        with open(report_file, "r") as file:

            report_content = file.read()

        # Display report on OnlineGDB screen
        print("\n========== GENERATED RESULT REPORT ==========\n")

        print(report_content)

        print("============================================")


# ==============================
# MAIN FUNCTION
# ==============================

def main():

    system = ResultManagementSystem()

    while True:

        print("\n======================================")
        print(" STUDENT RESULT MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Generate Result Report")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            system.add_student()

        elif choice == "2":

            system.view_students()

        elif choice == "3":

            system.search_student()

        elif choice == "4":

            system.update_student()

        elif choice == "5":

            system.delete_student()

        elif choice == "6":

            system.generate_report()

        elif choice == "7":

            print("\nThank you for using Student Result Management System!")
            break

        else:

            print("Invalid choice. Please try again.")


# ==============================
# PROGRAM START
# ==============================

if __name__ == "__main__":

    main()
