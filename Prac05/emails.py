def input_emails():
    email_dict = {} 
    email = input("Email: ")
    while email != "":
        #split email by @ , [0] to get before @
        name = email.split("@")[0]
        #split everything before @ by . 
        name = name.split(".")
        #join back with space 
        name = " ".join(name).title() 
        user_input = input("Is your name {}? (Y/n) ".format(name))
        if (user_input.lower() != "y" and user_input != ""):
            name = input("Name : ")

        email_dict[email] = name
        email = input("Email: ")

    return email_dict

def main():
    email_dict = input_emails()
    for email,name in email_dict.items():
        print("{} ({})".format(name,email))

main()
