# This program excute copy file function

# dieced need read file
old_file_name = input("please input need copy file:")

# open file
fr = open(old_file_name,"r")

# read old file content
content = fr.read()

# write to new file
new_file_name = old_file_name+"a"

fw = open(new_file_name,"w")
fw.write(content)

# close all file
fr.close()
fw.close()
