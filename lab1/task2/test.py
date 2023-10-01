import unittest
from unittest.mock import patch
from io import StringIO

from main import PersonList


class TestTask2(unittest.TestCase):
    def test_add(self):
        persons = PersonList()

        persons.__add__('a', 'g', 42)
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            persons.print_persons()
        output = captured_output.getvalue()
        self.assertEqual(output, 'a g, 42\n')

        persons.__add__('s', 'h', 100)
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            persons.print_persons()
        output = captured_output.getvalue()
        self.assertEqual(output, 'a g, 42\n'
                                 's h, 100\n')

    def test_add_invalid_first_name(self):
        persons = PersonList()

        with self.assertRaises(ValueError) as context:
            persons.__add__('', 'a', 12)

        self.assertEqual(str(context.exception), 'Invalid first name')

    def test_add_invalid_second_name(self):
        persons = PersonList()

        with self.assertRaises(ValueError) as context:
            persons.__add__('a', '', 12)

        self.assertEqual(str(context.exception), 'Invalid second name')

    def test_add_invalid_age(self):
        persons = PersonList()

        with self.assertRaises(ValueError) as context:
            persons.__add__('a', 'a', -1)
        self.assertEqual(str(context.exception), 'Error. 0 <= age <= 100 expected.')

        with self.assertRaises(ValueError) as context:
            persons.__add__('a', 'a', 'a')
        self.assertEqual(str(context.exception), 'Error. 0 <= age <= 100 expected.')

    @staticmethod
    def _insert_persons_list_values(persons: PersonList):
        persons.__add__('a', 'b', 2)
        persons.__add__('c', 'd', 5)
        persons.__add__('e', 'f', 6)

    def test_persons_values(self):
        persons = PersonList()
        self._insert_persons_list_values(persons)

        self.assertEqual(persons.min_age(), 2)
        self.assertEqual(persons.max_age(), 6)
        self.assertEqual(persons.avg_age(), 4.33)
