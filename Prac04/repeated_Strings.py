def main():
    strings = []
    repeated_strings = []
    user_input = input("Enter a string : ")
    while user_input != '':
        if user_input in strings:
            repeated_strings.append(user_input)    
        else:
            strings.append(user_input)
        user_input = input("Enter a string : ")

    if len(repeated_strings) > 0:
        for string in repeated_strings:
            print("Strings repeated: {}".format(string))

    else:
        print("No repeated strings entered")

main()
