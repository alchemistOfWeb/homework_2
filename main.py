def hr():
    print('='*100)


def fizz_buzz():
    for i in range(1, 101):
        out = ''
        if i % 3 == 0:
            out = 'Fizz'

        if i % 5 == 0:
            out += 'Buzz'

        out = i if not out else out

        print(out)


def key_value(sample_dict):
    result = {val: key for key, val in sample_dict.items()}
    print(result)


def duplicates(old_list):
    new_list = list(set(old_list))
    print(new_list)


if __name__ == '__main__':
    fizz_buzz()
    hr()
    key_value({'first': 1, 'second': 23, 'third': 44})
    hr()
    duplicates([1, 2, 3, 4, 4, 4, 5, 2, 3, 8, 7])
