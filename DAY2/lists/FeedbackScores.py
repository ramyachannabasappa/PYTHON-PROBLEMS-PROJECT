Feedback=input("Enter the scores")

scores=[]

even_count=0
odd_count=0

for i in scores:
    if i%2==0:
        even_count+=1
        print("Even numbers:",even_count)

    else:
        odd_count+=1
        print("Odd numbers:",odd_count)

