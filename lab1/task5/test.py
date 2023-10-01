import unittest
from unittest.mock import patch
from io import StringIO

from main import FileSearcher


class TestTask5(unittest.TestCase):
    def setUp(self):
        self.searcher = FileSearcher()

    def test_invalid_values(self):
        with self.assertRaises(ValueError) as context:
            self.searcher.search_files('a', '/')
        self.assertEqual(str(context.exception), 'Invalid extension')

        with self.assertRaises(Exception) as context:
            self.searcher.search_files(None, '/')
        print(str(context.exception), 'Extension expected')

        with self.assertRaises(Exception) as context:
            self.searcher.search_files('.png', None)
        print(str(context.exception), 'Invalid folder path')

    def test_file_search(self):
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            self.searcher.search_files('.png', '/Users/vadinamo/Downloads/cutted-images/')
        output = captured_output.getvalue()
        self.assertEqual(output,
                         '/Users/vadinamo/Downloads/cutted-images/homme/jacket.PNG\n' +
                         '/Users/vadinamo/Downloads/cutted-images/homme/truhi.PNG\n' +
                         '/Users/vadinamo/Downloads/cutted-images/femme/skirt.PNG\n' +
                         '/Users/vadinamo/Downloads/cutted-images//jacket.PNG\n' +
                         '/Users/vadinamo/Downloads/cutted-images//truhi.PNG\n' +
                         '/Users/vadinamo/Downloads/cutted-images//skirt.PNG\n')
