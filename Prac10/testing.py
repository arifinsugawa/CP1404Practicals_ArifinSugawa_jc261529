import doctest
from prac_06.car import Car


def repeat_string(s, n):
    return " ".join([s] * n)


def is_long_word(word, length=5):

    >>> is_long_word("not")
    >>> is_long_word("supercalifrag")
    >>> is_long_word("Python", 6)

    return len(word) >= length


def run_tests():
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    test_car = Car()
    assert test_car.fuel == 0



def phrase_to_sentence(phrase):

    >>> phrase_to_sentence('hello')
    >>> phrase_to_sentence('It is an ex parrot.')
    >>> phrase_to_sentence('This subject rocks')

    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()

doctest.testmod()