def main():
    email_to_name = {}
    email = input("Please Input Email Here: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your Email name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Please Input Name Here: ")
        email_to_name[email] = name
        email = input("Please Input Email Here: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()