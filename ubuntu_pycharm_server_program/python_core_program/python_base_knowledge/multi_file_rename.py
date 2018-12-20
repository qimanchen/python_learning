import os

# read folder
file_list = os.listdir("./file_rename_folder")
os.chdir("./file_rename_folder")

# rename file name from folder
for file_name in file_list:
    os.rename(file_name,"man_"+file_name)

print(os.listdir("./"))

