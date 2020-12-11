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


    def test_if_student_registered(self):
        filename='student-info/.student.json'
        with open(filename) as json_file:
            data = json.load(json_file)
        self.assertTrue(registration.is_student_registered(data['student_info'], 'jroy'))
      
    
    def test_student_not_registered(self):
        filename = 'student-info/.student.json'
        with open(filename) as json_file:
            data = json.load(json_file)
        self.assertFalse(registration.is_student_registered(data['student_info'], 'bnkala'))

if __name__ == "__main__":
    unittest.main()