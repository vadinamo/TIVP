class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age


class PersonList:
    def __init__(self):
        self._persons = []

    def __add__(self, first_name, second_name, age):
        if first_name.replace(' ', '').replace('\t', '') == '':
            raise ValueError('Invalid first name')

        if second_name.replace(' ', '').replace('\t', '') == '':
            raise ValueError('Invalid second name')

        result_age = int_try_parse(age)
        if not result_age[1] or result_age[0] < 0 or result_age[0] > 100:
            raise ValueError('Error. 0 <= age <= 100 expected.')

        self._persons.append(Person(first_name, second_name, result_age[0]))

    def print_persons(self):
        for person in self._persons:
            print(f'{person.first_name} {person.second_name}, {person.age}')

    def min_age(self):
        return min(self._persons, key=lambda p: p.age).age

    def max_age(self):
        return max(self._persons, key=lambda p: p.age).age

    def avg_age(self):
        return round(sum(person.age for person in self._persons) / len(self._persons), 2)


def int_try_parse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def task2():
    persons = PersonList()
    while input('Enter /stop to finish inserting people or anything else to continue.\n') != '/stop':
        try:
            persons.__add__(input('First name: '), input('Second name: '), input('Age: '))
        except Exception as e:
            print(e)

    persons.print_persons()

    print(f'Min age: {persons.min_age()}')
    print(f'Max age: {persons.max_age()}')
    print(f'Average age: {persons.avg_age()}')


if __name__ == '__main__':
    task2()
