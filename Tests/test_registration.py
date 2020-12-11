import unittest
from unittest.main import main
from unittest.mock import patch
from io import StringIO
import sys
import os
import json
USER_PATHS = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../'))
sys.path.insert(0, USER_PATHS)
from commands import registration
# [register] [username] [password]
class Test(unittest.TestCase):

    def test_write_json(self):
        student_data = {'student_info': [{'password': 'password', 'username': 'cprinsloo'}, {'password': 'password', 'username': 'student'}, {'password': '12345678', 'username': 'sgerber'}, {'password': 'password', 'username': 'jroy'}, {'username': 'bnkala', 'password': 'Ad3laide'}]}
        registration.write_json(student_data, filename='student-info/.student_test.json')

    def test_if_student_registered(self):
        filename='student-info/.student.json'
        with open(filename) as json_file:
            data = json.load(json_file)
        #     for student in data:
        #         print(student, data['student_info'][0])
        # result = {
        #     "password": "password",
        #     "username": "cprinsloo"
        # }
        # result_1 = data['student_info']
        # self.assertEqual(result, data['student_info'][0])
        self.assertTrue(registration.is_student_registered(data['student_info'], 'jroy'))

    def if_student_registered2(self):
        student_data = {'student_info': [{'password': 'password', 'username': 'cprinsloo'}, {'password': 'password', 'username': 'student'}, {'password': '12345678', 'username': 'sgerber'}, {'password': 'password', 'username': 'jroy'}, {'username': 'bnkala', 'password': 'Ad3laide'}]}

        result = registration.is_student_registered(student_data, 'cprinsloo')
        self.assertEqual(result, True)  
    
    def test_student_not_registered(self):
        filename = 'student-info/.student.json'
        with open(filename) as json_file:
            data = json.load(json_file)
        self.assertFalse(registration.is_student_registered(data['student_info'], 'smkiva'))

if __name__ == "__main__":
    unittest.main()