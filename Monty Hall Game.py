import random
print("Welcome to Monty Hall Game.")
print("The Description and Rules about the game and how to play? are given below:")
print("You are given the choice of three doors: Behind one door is a car; behind the others, goats.")
print("You pick a door, say No. 1, and I, who knows what is behind the doors, opens "
      "another door, say No. 3, which has a goat. Then I will ask, \"Do you want to pick door No. 2?\" "
      "Now you have a chance to choose from other two doors or continue with the current door you chose.")
lst=["Goat","Car","Goat"]

door1=random.choice(lst)
lst.remove(door1)
door2=random.choice(lst)
lst.remove(door2)
door3=lst[0]

print("\nDoor1,Door2,Door3")
choice=int(input("Enter your choice (1, 2 or 3): "))

if choice==1:
      if door1=="car":
            print("Yes, your choice is correct. Behind the Door1 is Car.")
      else:
            switch_or_not=
