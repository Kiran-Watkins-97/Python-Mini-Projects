def print_hi(name):
    print(f'Hi, {name}')


def square_value(input_value: int) -> int:
    return input_value * input_value


if __name__ == '__main__':
    print_hi('PyCharm')
    print("Here is your squared value: " +
          str(square_value(int(input("Insert number you wish to square: ")))))

