def even_numbers(numbers_str):
    numbers_list = [int(i) for i in numbers_str.split()]
    return [num for num in numbers_list if num%2==0]

numbers= input("Enter a list of numbers, each separated by space:")
even_nums = even_numbers(numbers)
print(f"List of even numbers: {even_nums}")
