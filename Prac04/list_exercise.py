numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("Input first number:", numbers[0])
print("Input last number:", numbers[-1])
print("Input smallest number:", min(numbers))
print("Input largest number:", max(numbers))
print("Input average of the numbers:", sum(numbers) / len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']
username = input("Type username:")
if username in usernames:
    print("Successfully Accepted")
else:
    print("Fail to Accept; Rejected")