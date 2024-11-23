"""
Author: Dawn K Vinod
Date: 23-11-2024
Description: Python program to display the total stock value of
each item in the inventory. Also display all the items with the highest stock value.
"""
inventory=[]
n=int(input("Enter how many items you want to add to the inventory:"))
for i in range(1,n+1):
    print(f"Item {i}:")
    name=input(f"Enter the name of item {i}: ")
    stock=int(input(f"Enter the stock of item {i}: "))
    price=float(input(f"Enter the price of item {i}: "))
    inventory.append((name,stock,price))

print(f"Inventory:{inventory}")

list_of_total_value=[]
for item in inventory:
    name,stock,price=item
    total_value = stock*price
    print(f"Total value of {name} is: {total_value}")
    list_of_total_value.append(total_value)

highest_value_items=[]
highest_value = max(list_of_total_value)
for index,value in enumerate(list_of_total_value):
    if value==highest_value:
        highest_value_items.append(inventory[index][0])
print(f"The item(s) having highest value: {highest_value_items}")
