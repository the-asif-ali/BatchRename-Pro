import os #Imports all files and folders

folder = input("Enter Folder Path : ") #selecting folder
files = os.listdir(folder) #Opening folder

ext = input("Enter File Extension : ")

file_name = input("Enter the new name : ")

images = [f for f in files if f.endswith(ext)] #Selecting files with your extension

count = 1 #counter for renaming

for file in files:
    old_path = os.path.join(folder, file) #Old path , old name
    new_name = f"{file_name}_{count}{ext}" #New name
    new_path = os.path.join(folder, new_name) #Old path, new name

    os.rename(old_path, new_path) #renamed

    print(f"file ---> {new_name}") #name changing status on output
    count+=1
print("Renaming Done!")
