
out_file = open("name.txt", "w")
name = input("Write Your Name Here! ")
print (out_file.write(name))
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Based on Your Written Name, Your Name Is", name)

out_file = open("numbers.txt", "w")
num1 = input("Write Your 1st Number Here! ")
num2 = input("Write Your 2nd Number Here! ")
num3 = input("Write Your 3rd Number Here! ")
print (out_file.write(num1))
print (out_file.write(num2))
print (out_file.write(num3))

out_file.close()

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)



