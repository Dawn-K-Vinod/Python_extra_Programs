def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

number=int(input("Enter a number:"))
factorial_of_num =factorial(number)
print(f"Factorial of the given number: {factorial_of_num}")