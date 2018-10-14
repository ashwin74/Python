import os
import re

def rename_files():
    
    #(1) get file names from a folder.
    file_list = os.listdir(r"E:\sData\P")
    os.chdir(r"E:\sData\P")
    saved_path = os.getcwd()
    print ("Current Directory "+saved_path)

    #(2) for each file, rename filename.
    for file_name in file_list:
        print ("Old name - " +file_name)
        os.rename(file_name, file_name.strip("0123456789"))

    os.chdir(saved_path)
    
    # (3) print new names.
    file_list = os.listdir(r"E:\sData\P")
    for file in file_list:
        print ("New name - ",file)


rename_files()
