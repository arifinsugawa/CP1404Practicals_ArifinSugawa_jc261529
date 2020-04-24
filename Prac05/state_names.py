STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}

state = input("Enter a state name: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid state name")
    state = input("Enter a state name: ").upper()