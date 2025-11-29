N=int(input("enter the ticket rate"))
M=int(input("enter the number of tickets"))
P=int(input("enter the student(1) or others(0)"))

total_amount=N*M
discount=0
if N>15:
    if P==1:
        discount=25 
        print("Discounts Applied-maxium Ticket and Student")
    else:
        discount=20
        print("discount Applied-maxium tickets")
else:
    print("no discount Applied")
final_amount=total_amount-(total_amount*discount/100)

print("Total Amount=",int(final_amount))