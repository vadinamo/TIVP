import argparse
import os
import re
import tkinter as tk
from tkinter import filedialog


class FileSearcher:
    def __init__(self):
        self._extension = ''

    def search_files(self, extension, folder_path):
        if not extension:
            raise Exception('Extension expected')
        if not re.match(r'^\.[A-Za-z0-9]+$', extension):
            raise ValueError('Invalid extension')

        if not folder_path:
            raise Exception('Invalid folder path')

        self._extension = extension
        self._folder_search(folder_path)

    def _folder_search(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith(self._extension):
                    print(f'{path}/{file}')
            for folder in dirs:
                folder_path = f'{path}/{folder}' if path[-1] != '/' else f'{path}{folder}'
                self._folder_search(folder_path)


def task5():
    parser = argparse.ArgumentParser()
    parser.add_argument('--extension')

    args = parser.parse_args()

    searcher = FileSearcher()
    try:
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory()
        searcher.search_files(args.extension, folder_path)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    task5()

# python3 main.py --extension .png
