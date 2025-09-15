#s= open("demofile.txt", "r")
# print(s.read())

# The open() function opens a file, and returns it as a file object.
# Syntax:
# open(file, mode)
'''
file -  The path and name of the file
mode -  A string, define which mode you want to open the file in:
        "r" - Read - Default value. Opens a file for reading, error if the file does not exist
        "a" - Append - Opens a file for appending, creates the file if it does not exist
        "w" - Write - Opens a file for writing, creates the file if it does not exist
        "x" - Create - Creates the specified file, returns an error if the file exist
        "t" - Text - Default value. Text mode
        "b" - Binary - Binary mode (e.g. images)
'''

shubham_file=open("C:\Users\SK1601\OneDrive - Modak Analytics LLP\Desktop\github-vscode-sync\repo-name\PYTHON-study\sample-file.txt","r")
print(shubham_file.read())