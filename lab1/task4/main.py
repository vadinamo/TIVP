import subprocess


class PageCreator:
    def __init__(self):
        self._page = ''
        self._file_name = ''

    def create_fade_table(self):
        doc = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <style>
                body {
                    margin: 0;
                }
                table {
                    width: 100vw;
                    height: 100vh;
                    border-collapse: collapse;
                }
            </style>
            <body>
            <table>
                '''

        for i in range(255, -1, -1):
            doc += f'''<tr>
                    <td style="background-color: rgb({", ".join([str(i)] * 3)})"></td>
                </tr>
                '''

        doc += '''
            </table>
            </body>
            </html>
            '''

        self._page = doc

    def save_page(self, file_name: str):
        if file_name.split('.')[-1].lower() != 'html':
            raise ValueError('HTML file extension expected')

        with open(file_name, 'w+') as f:
            f.write(self._page)

        self._file_name = file_name

    def open_page(self):
        subprocess.run(['open', self._file_name], check=True)


def task4():
    page_creator = PageCreator()
    page_creator.create_fade_table()
    page_creator.save_page('index.html')
    page_creator.open_page()


if __name__ == '__main__':
    task4()
