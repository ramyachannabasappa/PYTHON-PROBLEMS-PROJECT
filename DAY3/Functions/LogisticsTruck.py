Fuel_efficiency=set(map(float,input("enter the fuel efficency: ").split()))

max=-float('inf')
min=float('inf')

for i in Fuel_efficiency:
    if i>max:
        max=i
    elif i<min:
        min=i

print("maximum fuel efficency is: ",max)
print("minimum fuel efficency is: ",min)