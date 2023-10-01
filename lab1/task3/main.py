import argparse


class SquareCalculator:
    @staticmethod
    def calculate(height, width):
        width_arg = float_try_parse(width)
        height_arg = float_try_parse(height)

        if not width_arg[1] or width_arg[0] < 0:
            raise ValueError('Invalid width argument')

        if not height_arg[1] or height_arg[0] < 0:
            raise ValueError('Invalid height argument')

        return width_arg[0] * height_arg[0]


def float_try_parse(value):
    try:
        return float(value), True
    except Exception:
        return value, False


def task3():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width')
    parser.add_argument('--height')

    args = parser.parse_args()

    print(f'Square: {SquareCalculator.calculate(args.height, args.width)}')


if __name__ == '__main__':
    task3()
