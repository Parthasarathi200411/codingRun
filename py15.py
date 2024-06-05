def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def non_prime_numbers(start, end):
    non_primes = []
    for num in range(start, end + 1):
        if not is_prime(num):
            non_primes.append(num)
    return non_primes

def main():
    while True:
        try:
            num1 = int(input("Enter the first positive integer: "))
            num2 = int(input("Enter the second positive integer: "))
            if num1 <= 0 or num2 <= 0:
                print("Please enter positive integers only.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    start = min(num1, num2)
    end = max(num1, num2)

    non_primes = non_prime_numbers(start, end)

    print("Non-prime numbers between {} and {}:".format(start, end))
    count = 0
    for num in non_primes:
        print(num, end=" ")
        count += 1
        if count % 10 == 0:
            print()

if __name__ == "__main__":
    main()
