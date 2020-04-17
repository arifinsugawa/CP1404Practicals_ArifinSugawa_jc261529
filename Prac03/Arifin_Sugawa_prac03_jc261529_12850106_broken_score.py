"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this! (Done)

def main():
    score = float(input("Input score: "))
    print(determine_status(score))


def determine_status(score):
    if score < 0 or score > 100:
        return "Score Error"
    elif score >= 90:
        return "Distinction"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"


main()