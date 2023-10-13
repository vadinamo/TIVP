import unittest
from pathlib import Path

from main import task4, PageCreator


class TestTask4(unittest.TestCase):
    def test_file_exists(self):
        task4(False)

        file_path = 'index.html'
        path = Path(file_path)
        self.assertEqual(path.exists(), True)

    def test_invalid_file_name(self):
        page_creator = PageCreator()
        page_creator.create_fade_table()

        with self.assertRaises(ValueError) as context:
            page_creator.save_page('index.png')
        self.assertEqual(str(context.exception), 'HTML file extension expected')
