file_name=input("enter the file name:")

try:
    with open(file_name,'r')as file:
        Nlines=file.readlines()
        Print(f"the number of lines in the file is:{}")