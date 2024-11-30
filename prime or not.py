def prime_or_not(num):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        return True
    return False

number = int(input("Enter a number:"))
result = prime_or_not(number)
if result:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

