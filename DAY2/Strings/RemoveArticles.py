article=['an','a','the']
sentences=input("enter the sentences to remove articles:")
result=sentences
for i in article:
    result=result.replace(i,'')
    result=result.replace(i.capitalize(),'')

result=''.join(result.split())
print(result) 