#(1,2,3),(4,5,6),(7,8,9)
List_of_Tuple=input("Enter the list of tuples: ")
List_of_Tuple=eval(List_of_Tuple)
product=1
k=int(input("Enter the column index: "))
for i in List_of_Tuple:
    if k<len(i):
        product=product*i[k]
    else:
        print(f"Invalid{k}")
        break
print(product)