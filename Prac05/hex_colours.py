#https://www.color-hex.com/color-names.html
NAME_TO_CODE = {"ALICEBLUE": "#f0f8ff", "AZURE1": "#f0fff", "BEIGE": "#f5f5dc", "ANTIQUEWHITE": "#faebd7", "AQUAMARINE1": "#7fffd4", "BROWN": "#a52a2a", "CADETBLUE": "#98f5ff", "CORAL": "ff7f50", "CORNFLOWERBLUE": "6495ed", "DARKGREEN": "#005400"}

color = input("Enter Color Name :").upper()

while color != "":
    if color in NAME_TO_CODE:
        print(NAME_TO_CODE[color])
    else:
        print("Invalid Color name")
    color = input("Enter Color Name :").upper()

