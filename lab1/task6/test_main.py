from pathlib import Path
from unittest import TestCase, mock

from main import FileDownloader, FileWorker


class TestFileDownloader(TestCase):
    def test_download_file(self):
        folder_path = '/Users/vadinamo/Downloads/'
        downloader = FileDownloader('https://libeldoc.bsuir.by/bitstream/123456789/48834/1/Navrockii_Osnovi.pdf',
                                    folder_path, FileWorker())

        downloader.download_file()
        path = Path(f'{folder_path}Navrockii_Osnovi.pdf')

        self.assertEqual(path.exists(), True)

    @mock.patch('builtins.input', side_effect=['Y'])
    def test__file_worker(self, mock_input):
        mock_file_worker = mock.Mock(spec=FileWorker)
        downloader = FileDownloader('https://libeldoc.bsuir.by/bitstream/123456789/48834/1/Navrockii_Osnovi.pdf',
                                    '/Users/vadinamo/Downloads/', mock_file_worker)
        downloader.download_file(autoopen=True)
        mock_file_worker.open_file.assert_called_with('/Users/vadinamo/Downloads/Navrockii_Osnovi.pdf')
