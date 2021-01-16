import os 
import shutil 

def main(): 
    extensions = [] 
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        split_filename = filename.split('.')
        extension = split_filename[1]
        if extension not in extensions:
            extensions.append(extension)
            try:
                os.mkdir(extension) 
            except FileExistsError: 
                print("directory exist") 
        path = os.path.join(extension,filename)
        while os.path.exists(path):
            if split_filename[0][-1].isdigit():
                split_filename[0] = str(split_filename[0][:-1]) + str(int(split_filename[0][-1]) + 1) 
            else:
                split_filename[0] += '1'
            print(split_filename[0])
            path = os.path.join(extension, '.'.join(split_filename))
        shutil.move(filename,path)
main() 
