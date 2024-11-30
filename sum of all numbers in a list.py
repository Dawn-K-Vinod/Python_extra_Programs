def sum_of_numbers(numbers):
    return sum([int(i) for i in numbers.split()])


nums=input("Enter a list of numbers,each separated by space:")
sum_numbers = sum_of_numbers(nums)
print(f"The sum of all the numbers: {sum_numbers}")
