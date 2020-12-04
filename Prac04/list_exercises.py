def basic_list_operations():
    number_list = []
    count = 1
    number = int(input("Number {}: ".format(count)))

    while number > 0:
        count += 1
        number_list.append(number) 
        number = int(input("Number {}: ".format(count)))
    
    if len(number_list) > 0:
        print('The first number is {}'.format(number_list[0]))
        print('The last number is {}'.format(number_list[-1]))
        print('The smallest number is {}'.format(min(number_list)))
        print('The largest number is {}'.format(max(number_list)))
        average = sum(number_list) / len(number_list)
        print('The average of the numbers is {}'.format(average))

def username_checker():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter username :")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

def main():
    basic_list_operations()
    #username_checker()

main()
