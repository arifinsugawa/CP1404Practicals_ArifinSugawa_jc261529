"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this! (Done)

def main():
    score = float(input("Enter score: "))
    get_score(score)


def get_score(number1):
    if number1 < 0 or number1 > 100:
        return "Invalid score"
    elif number1 > 90:
        return "Excellent"
    elif number1 > 50:
        return "Passable"
    else:
        return "Bad"


main()
