def distinct_element_list(list1):
    return list(set(int(i) for i in list1.split()))

first_list = input("Enter a list of numbers, each separated by space:")
distinct_list= distinct_element_list(first_list)
print(f"The list of distinct numbers: {distinct_list}")