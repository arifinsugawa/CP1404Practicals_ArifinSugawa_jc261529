
user_sales = float(input("Please input the current existing sales: "))
while user_sales > 0:
    if user_sales >= 1000:
        user_bonus = user_sales * 0.15
        print("Your total sales is over $1000 gaining you a 15% bonus totaling of ${}".format(user_bonus))
        user_sales = float(input("Please input the current existing sales: "))

    else:
        user_bonus = user_sales * 0.10
        print("Your total sales is less than $1000 gaining you a 10% bonus totaling of ${}".format(user_bonus))
        user_sales = float(input("Please input the current existing sales: "))

print("You have input an incorrect value, please try inputting it again.")