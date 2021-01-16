import os 
import shutil 

def findDir(category, extension):
    for key,value in category.items():
        if extension in value:
            return key

def main(): 
    extensions = [] 
    category = {} 
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[1]
        if extension not in extensions:
            extensions.append(extension)
            dir_choice = input("What category would you like to sort {} files into? ".format(extension))
            if dir_choice in category:
                category[dir_choice].append(extension) 
            else:
                os.mkdir(dir_choice)
                category[dir_choice] = [extension] 
        else:
            dir_choice = findDir(category,extension) 

        path = os.path.join(dir_choice,filename)
        while os.path.exists(path):
            if split_filename[0][-1].isdigit():
                split_filename[0] = str(split_filename[0][:-1]) + str(int(split_filename[0][-1]) + 1) 
            else:
                split_filename[0] += '1'
            print(split_filename[0])
            path = os.path.join(extension, '.'.join(split_filename))

        shutil.move(filename,path)
main() 
