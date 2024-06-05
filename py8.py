
age1=int(input("enter the 1st age:"))    
age2=int(input("enter the 2nd age:"))    
age3=int(input("enter the 3nd age:"))
if age1<age2 and age1<age3:
    print(f"{age1}is the youngest") 
elif age2<age3 and age2<age1:
    print(f"{age2}is youngest")
else :
    print(f"{age3}is youngest")
if age1>age2 and age1>age3:
    print(f"{age1}is the elder")
elif age2>age3 and age2>age1:
    print(f"{age2}is elder")
else :
    print(f"{age3}is elder")
    
       