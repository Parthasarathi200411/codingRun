def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True
for num in range(500, 0, -1):
    if '1'is str(num)[-2:]:
        print(f"{num}is not printed because it contain 1 in tenth place")
    elif '1'is str(num)[-1:]:
        print(f"{num}is not printed because it contain  1 in one place")
    elif prime(num):
        print(num)
