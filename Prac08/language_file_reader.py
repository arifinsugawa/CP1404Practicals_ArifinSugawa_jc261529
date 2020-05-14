import csv
from collections import namedtuple

from Prac08.programming_language import ProgrammingLanguage


def main():
    languages = []
    in_file = open('languages.csv', 'r')
    in_file.readline()

    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection,
                                       int(parts[3]))

        languages.append(language)

    in_file.close()

    for language in languages:
        print(language)


main()


def using_csv():
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        print(row)

    in_file.close()




def using_namedtuple():
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    Language = namedtuple('Language', 'name, typing, reflection, year')
    reader = csv.reader(in_file)  # use default dialect, Excel

    for row in reader:
        language = Language._make(row)
        print(repr(language))
    in_file.close()




def using_csv_namedtuple():
    Language = namedtuple('Language', 'name, typing, reflection, year')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))