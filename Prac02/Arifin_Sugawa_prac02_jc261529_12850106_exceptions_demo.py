try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    fraction = 0
print("Finished.")

"""
When will a ValueError occur? When either the numerator or denominator is not a numerical value such as a letter.
                              This will cause a ValueError 
When will a ZeroDivisionError occur? ZeroDivisionError will occur if the input of denominator is 0 as any numbers 
                                     can't be divided by 0 (denominator).
Could you change the code to avoid the possibility of a ZeroDivisionError? Yes but it would just skip the error
                                                                           statement.
"""