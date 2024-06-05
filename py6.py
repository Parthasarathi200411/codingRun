sum=0
for i in range(5):
    sub=int(input(f"enter the mark for sub{i+1}:"))
    sum=sum+sub
    
percentage=(sum/500)*100 
print("percentage is:")
if percentage>=90:
    print("o")
elif 80<=percentage<90:
    print("e")
elif 70<=percentage<80:
    print("a")
elif 60<=percentage<70:
    print("b")
elif 50<=percentage<60:
    print("c")
else:
    print("d")
        
