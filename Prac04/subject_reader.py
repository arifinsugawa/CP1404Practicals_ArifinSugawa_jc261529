"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def display_subject_details(data):
    for subject in data:
        title = subject[0]
        if subject[0] == 'CP1401':
            title = 'Programming'
        elif subject[0] == 'CP1404':
            title = 'Science' 
        elif subject[0] == 'CP4321':
            title = 'Math'
        elif subject[0] == 'CP1234':
            title = 'Economics' 
        print('{} is taught by {} and has {} students'.format(title,subject[1],subject[2]))

def main():
    data = get_data()
    #print(data)
    display_subject_details(data)


def get_data():
    data = []
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        #print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        #print(parts)  # See if that worked
        data.append(parts)
        #print("----------")
    input_file.close()
    return data


main()
