import argparse
import os
import subprocess

import requests


class FileWorker:
    @staticmethod
    def save_file(filename, save_path, content):
        print('Saving file')

        with open(os.path.join(save_path, filename), 'wb') as file:
            file.write(content)

        print('File saved successfully')

    @staticmethod
    def open_file(file_path):
        subprocess.run(['open', file_path], check=True)


class FileDownloader:  # https://libeldoc.bsuir.by/bitstream/123456789/48834/1/Navrockii_Osnovi.pdf
    def __init__(self, url, folder, file_worker):
        if not url:
            raise ValueError('Invalid url')

        if not folder or not (os.path.exists(folder) and os.path.isdir(folder)):
            raise ValueError('Invalid folder path')

        self._url = url
        self._folder = folder
        self._file_worker = file_worker

    def download_file(self, autoopen=False):
        print('Start downloading...')
        response = requests.get(self._url)
        if response.status_code != 200:
            raise Exception('Bad request')
        else:
            print('Connected')

        filename = os.path.basename(self._url)
        save_path = self._folder

        self._file_worker.save_file(filename=filename, save_path=save_path, content=response.content)

        if autoopen:
            self._file_worker.open_file(os.path.join(save_path, filename)) if input('Open downloaded file?\nY/n\n') == 'Y' else ''


def task6():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    parser.add_argument('--folder')

    args = parser.parse_args()

    url = args.url
    folder = args.folder

    try:
        downloader = FileDownloader(url, folder, FileWorker())
        downloader.download_file(True)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    task6()
