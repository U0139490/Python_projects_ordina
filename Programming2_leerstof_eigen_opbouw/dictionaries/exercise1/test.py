from student import * 
import unittest

class TestDictionaryFunctions(unittest.TestCase):
    def test_process_data(self):
        data = ['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry']
        expected_output = {
            'John Smith': {
                'age': 20,
                'courses': ['Math', 'Physics']
            },
            'Jane Doe': {
                'age': 21,
                'courses': ['Biology', 'Chemistry']
            }
        }
        self.assertEqual(process_data(data), expected_output)

    def test_avg_age(self):
        data = {
            'John Smith': {
                'age': 20,
                'courses': ['Math', 'Physics']
            },
            'Jane Doe': {
                'age': 21,
                'courses': ['Biology', 'Chemistry']
            }
        }
        expected_output = 20.5
        self.assertEqual(avg_age(data), expected_output)

    def test_courses(self):
        data = {
            'John Smith': {
                'age': 20,
                'courses': ['Math', 'Physics']
            },
            'Jane Doe': {
                'age': 21,
                'courses': ['Biology', 'Chemistry']
            }
        }
        expected_output = ['Math', 'Physics', 'Biology', 'Chemistry']
        self.assertEqual(courses(data), expected_output)

    def test_most_common_course(self):
        data = {
            'John Smith': {
                'age': 20,
                'courses': ['Math', 'Physics']
            },
            'Jane Doe': {
                'age': 21,
                'courses': ['Biology', 'Chemistry']
            },
            'Bob Smith': {
                'age': 22,
                'courses': ['Biology', 'Chemistry']
            }
        }
        expected_output = 'Biology'
        self.assertEqual(most_common_course(data), expected_output)

if __name__ == "__main__":
    unittest.main()
