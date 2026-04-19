import unittest
from datetime import datetime
from q1 import *

class TestStudentMidtermSchedule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load data once before all tests
        cls.exam_dates = {}
        cls.student_courses = {}
        load_data(cls.exam_dates, cls.student_courses)

    def test_student_with_all_midterms_alice(self):
        student_name = "Alice"
        result = get_student_schedule(student_name, self.student_courses, self.exam_dates)
        expected = [
            "COMP100 2025-05-10",
            "PHYS101 2025-05-12",
            "No midterm exams scheduled for MATH101."
        ]
        self.assertEqual(result, expected)

    def test_student_not_found(self):
        student_name = "Jerry"
        result = get_student_schedule(student_name, self.student_courses, self.exam_dates)
        expected = ["Student not found."]
        self.assertEqual(result, expected)

    def test_student_with_some_missing_exams_bob(self):
        student_name = "Bob"
        result = get_student_schedule(student_name, self.student_courses, self.exam_dates)
        expected = [
            "COMP130 2025-05-15",
            "No midterm exams scheduled for MATH101.",
            "No midterm exams scheduled for PHYS106."
        ]
        self.assertEqual(result, expected)

    def test_student_with_multiple_courses_frank(self):
        student_name = "Frank"
        result = get_student_schedule(student_name, self.student_courses, self.exam_dates)
        expected = [
            "COMP100 2025-05-10",
            "PHYS101 2025-05-12",
            "No midterm exams scheduled for PHYS106."
        ]
        self.assertEqual(result, expected)

    def test_student_with_midterms_carol(self):
        student_name = "Carol"
        result = get_student_schedule(student_name, self.student_courses, self.exam_dates)
        expected = [
            "PHYS101 2025-05-12",
            "MATH102 2025-05-18",
            "COMP131 2025-05-20"
        ]
        self.assertEqual(result, expected)

    def test_student_with_midterms_david(self):
        student_name = "David"
        result = get_student_schedule(student_name, self.student_courses, self.exam_dates)
        expected = [
            "COMP100 2025-05-10",
            "MATH218 2025-05-22",
            "PHYS102 2025-05-24"
        ]
        self.assertEqual(result, expected)

    def test_student_with_midterms_emma(self):
        student_name = "Emma"
        result = get_student_schedule(student_name, self.student_courses, self.exam_dates)
        expected = [
            "COMP130 2025-05-15",
            "MATH102 2025-05-18",
            "COMP131 2025-05-20"
        ]
        self.assertEqual(result, expected)

    def test_student_with_missing_exam_grace(self):
        student_name = "Grace"
        result = get_student_schedule(student_name, self.student_courses, self.exam_dates)
        expected = [
            "COMP130 2025-05-15",
            "PHYS102 2025-05-24",
            "No midterm exams scheduled for MATH101."
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
