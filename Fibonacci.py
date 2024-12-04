"""
Author: Dawn K Vinod
Date: 04-12-2024
"""
def fibonacci_series(n):
    num1,num2=0,1
    fibonacci_sequence = []
    for _ in range(n):
        num1,num2 = num2,num1+num2
        fibonacci_sequence.append(num1)
    return fibonacci_sequence
nth=int(input("Enter a number 'n' for displaying fibonacci series upto 'n':"))
result=fibonacci_series(nth)
print(f"The first {nth} terms of the Fibonacci sequence are:: {result}")
