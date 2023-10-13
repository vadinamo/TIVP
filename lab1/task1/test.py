import unittest
from unittest.mock import patch
from io import StringIO

from main import task1


class TestTask1(unittest.TestCase):
    def test_output(self):
        for _ in range(10000):
            captured_output = StringIO()
            with patch('sys.stdout', new=captured_output):
                task1()
            output = captured_output.getvalue()
            self.assertRegex(output, r'^Hello, world!\nAndhiagain!\n!{5,50}$')
