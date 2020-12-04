import random as ran
min_value = 1
max_value = 45

def generate_line():
    line = []
    for x in range(6):
        num = ran.randrange(min_value,max_value)
        while num in line:
            num = ran.randrange(min_value,max_value)
        line.append(num)
    return line

def display_lines(lottery_ticket):
    for line in lottery_ticket:
        for num in line:
            print('{:2} '.format(num),end= ' ') 
        print('')
    
def main():
    lottery_ticket = []
    num_lines = int(input("How many quick picks? "))
    for x in range(num_lines):
        line = generate_line()
        line.sort()
        lottery_ticket.append(line)

    display_lines(lottery_ticket)

main()
