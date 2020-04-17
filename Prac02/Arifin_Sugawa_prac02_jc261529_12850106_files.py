# Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

out_file = open("name.txt", "w")
name = input("Write Your Name Here! ")
print (out_file.write(name))
out_file.close()

# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Based on Your Written Name, Your Name Is", name)

# Create a text file called numbers.txt and save it in your prac_02 directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers
# and adds them together then prints the result, which should be... 59.

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

# Now write a fourth block of code that prints the total for all lines in numbers.txt
# or a file with any number of numbers.

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)



