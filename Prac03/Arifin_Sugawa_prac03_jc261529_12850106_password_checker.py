MINIMUM_LENGTH = 4


def version_1():
    password = input("Input password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Input password of at least {} characters: ".format(MINIMUM_LENGTH))

    print('*' * len(password))




def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Input password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password that you input is too short")
        password = input("Input password of at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


main()