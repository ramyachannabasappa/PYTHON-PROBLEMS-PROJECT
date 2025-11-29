import os

source_file_path=input("Enter the source file path:")
destination_file_path=input("enter the destinationfile path:")

if os.path.exists(source_file_path):
    with open(source_file_path,'r',encoding='utf-8',errors='replace') as src:
       content=src.read()
    with open(destination_file_path,'w',encoding='utf-8') as dest:
     dest.write(content)
     print("content copied successfully.")

else:
   print(f"source file{source_file_path} does not exist.")