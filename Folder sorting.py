import os
import glob

# All files in the current path

files_list = glob.glob('*')

# Avoid creating duplicate folders

extensions_set = set()

# Separation of files by extension

for each_file in files_list:
    try:
        extension = each_file.split('.')[1]
        extensions_set.add(extension)
    except:
        continue

# Creating folders based on file extension names except for files with ".py" extension

def creat_folder():

    for ext in extensions_set:
        if ext == 'py':
            continue
        try:
            os.makedirs(ext + '_files')
        except:
            continue

# Transferring files to their own extension folders

def move_files():
    for each_file in files_list:
        
        extension = each_file.split('.')[1]
        try:
            os.rename(each_file,extension+'_files/'+each_file)
        except:
            continue 

# Function call

creat_folder()
move_files()


