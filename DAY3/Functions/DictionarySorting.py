# SAMPLE INPUT
#{'Laptop':800,'Mobile':400,'TV':600,'Headphones':100}
#SAMPLE INPUT END
products=eval(input("Enter the product:"))
sort_mehtod=input("Enter the sorting type key or price:")

if sort_mehtod=='key':
    sorted_values=sorted(set(products.values()))

    sorted_dict={}
    for i in sorted_values:
        for key in products:
         if key in products:
          if products[key]==i:
             sorted_dict[key]=i
else:
    sorted_dict=products
    print("Invalid option.")
print("sorted dictionary:",sorted_dict)