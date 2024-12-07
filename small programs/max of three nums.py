def max_of_three_num(num1,num2,num3):
    return max([num1,num2,num3])


number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
number3=int(input("Enter third number:"))
max=max_of_three_num(number1,number2,number3)
print(f"Maximum of given three numbers: {max}")