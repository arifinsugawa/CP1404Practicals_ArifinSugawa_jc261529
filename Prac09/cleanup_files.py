import os

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    UNDERSCORE = '_'
    EMPTY_STRING = ''
    new_name = EMPTY_STRING
    prev_letter =  EMPTY_STRING
    for letter in filename: 
        if letter == ' ':
            letter = UNDERSCORE
        elif prev_letter.islower() and letter.isupper():
            new_name += UNDERSCORE
        
        prev_letter = letter
        new_name += letter

    new_name = new_name.replace(".TXT", ".txt")
    return new_name

def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        path = os.path.join(os.getcwd(),directory_name)

        for filename in filenames:
            file_path = os.path.join(path,filename)
            new_name = get_fixed_filename(filename)
            os.rename(file_path, os.path.join(path,new_name))

main()
