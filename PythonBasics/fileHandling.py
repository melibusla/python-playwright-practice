# Example 1: Create/ Writing a file

#approach 1
# file = open("C:\\Users\\melib\\Documents\\automation-projects\\myfile.txt", "w")
# file.write("Hello World")
# file.close()

#approach 2 using with
# with open("C:\\Users\\melib\\Documents\\automation-projects\\myfile.txt", "w") as file:
#     file.write("Hello World with WITH")
#     file.close()

# Append Data
# with open("C:\\Users\\melib\\Documents\\automation-projects\\myfile.txt", "a") as file:
#     file.write("\n appending line\n")
#     file.close()

# Reading data
# read() - reads entire data
# readline() - read single line
# readlines() - read all the lines into list format ['Hello Worldappending line\n', '\n', ' appending line\n']
# with open("C:\\Users\\melib\\Documents\\automation-projects\\myfile.txt", "r") as file:
#     content = file.readlines()
#     print(content)
#     file.close()

# Renaming the file
# import os
# os.rename("C:\\Users\\melib\\Documents\\automation-projects\\myfile.txt", "C:\\Users\\melib\\Documents\\automation-projects\\myfile2.txt")
# print("File is renamed")

# Deleting the file
# import os
# file = "C:\\Users\\melib\\Documents\\automation-projects\\myfile2.txt"
#
# if os.path.exists(file):
#     os.remove(file)

# Creating a directory/folder
# import os
# os.mkdir("C:\\Users\\melib\\Documents\\automation-projects\\mydir")
# print("Directory Created")

# Check if the directory exists
# import os
# mydir = "C:\\Users\\melib\\Documents\\automation-projects\\mydir"
# if os.path.exists(mydir):
#     print("Directory Exists")
# else:
#     print("Directory do Not exists")
#
# # Rename the directory
# import os
# os.rename("C:\\Users\\melib\\Documents\\automation-projects\\mydir", "C:\\Users\\melib\\Documents\\automation-projects\\mydir2")
# print("directory renamed")

# Remove the directory
# import os
# import shutil
#if the folder is empty
# os.rmdir("C:\\Users\\melib\\Documents\\automation-projects\\mydir2")
#if there are files
# shutil.rmtree("C:\\Users\\melib\\Documents\\automation-projects\\mydir2")

# Get the current working directory
import os
print(os.getcwd())
