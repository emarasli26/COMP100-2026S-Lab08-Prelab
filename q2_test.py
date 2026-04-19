import unittest
from q2 import generate_gpa_ranking

class TestStudentGPARanking(unittest.TestCase):

    def test_gpa_ranking_output_file(self):
        # First run your code
        generate_gpa_ranking()

        # Open the generated file
        with open("gpa_ranking.txt", "r") as f_generated:
            generated_lines = f_generated.readlines()

        # Open the solution file
        with open("solution.txt", "r") as f_solution:
            solution_lines = f_solution.readlines()

        # Compare exactly (no stripping)
        self.assertEqual(generated_lines, solution_lines)

    def test_messages(self):
        messages = generate_gpa_ranking()
        expected = [
            "Grade B! not found.",
            "Course PHYS105 not found."
        ]
        self.assertEqual(messages, expected)  # sort to ignore order

if __name__ == "__main__":
    unittest.main()
