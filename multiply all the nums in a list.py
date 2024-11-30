def multiply(numbers):
    nums_list=[int(i) for i in numbers.split()]
    product_nums=1
    for num in nums_list:
        product_nums*=num
    return product_nums

nums=input("Enter a list of numbers,each separated by space:")
product=multiply(nums)
print(f"Product of All the numbers: {product}")