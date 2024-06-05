input=int(input("enter a number"))
def prime(number):
  if number<=1:
    return False
  for i in range(2,number+1):
    if number%i==0:
        return False
    return True
if prime(input):
    print(f"{input}is a prime number")
else:
    print(f"{input}is not a prime number")