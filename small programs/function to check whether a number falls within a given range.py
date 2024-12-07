def check_num_in_range(x,y,num):
    if num in list(range(x,y)):
        return True
    else:
        return False

lower_range=int(input("Enter the lower range:"))
upper_range=int(input("Enter the upper range:"))
number=int(input(f"Enter the number to check whether it falls within the range({lower_range},{upper_range}):"))
result = check_num_in_range(lower_range,upper_range,number)
if result:
    print(f"The given number falls within the range({lower_range},{upper_range})")
else:
    print(f"The given number does not falls within the range({lower_range},{upper_range})")