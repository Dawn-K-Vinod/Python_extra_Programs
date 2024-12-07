import random
print("--Welcome to Monty Hall Game--")
print("The `Description` and `Rules` and `how to play?` are given below:")
print("You are given the choice of three doors: Behind one door is a car and behind the other two are goat.")
print("You pick a door, say No. 1, and I, who knows what is behind the doors, opens "
      "another door, say No. 3, which has a goat. Then I will ask, \"Do you want to pick door No. 2?\" "
      "Now you have a chance to choose from other two doors or continue with the current door you chose.")
lst = ["Goat", "Car", "Goat"]
random.shuffle(lst)
three_doors = [lst[0], lst[1], lst[2]]
all_opened=f"Door-1:{three_doors[0]},\nDoor-2:{three_doors[1]},\nDoor-3:{three_doors[2]}"

print("\nDoor1|Door2|Door3")

# Prompt the user to enter the choice
while True:
    choice = int(input("Enter your choice (1, 2 or 3): "))
    if choice in [1,2,3]:
        break
    else:
        print("Invalid Entry. Try Again.")
        continue

# Opening the door that has a Goat behind it, other than the chosen door (if a Goat is behind the chosen door)
for index,door in enumerate(three_doors):
    if door=="Goat" and index+1 != choice:
        index_of_opened_door = index
        break
print(f"\nBehind the Door {index_of_opened_door + 1} is Goat.")

# Door other than the opened door and chosen door
not_chosen_door = list({1,2,3}-{choice, index_of_opened_door + 1})

# Asking the user whether he/she want to continue with the chosen door or switch to the door that not chosen
while True:
    continue_or_not = input(
        f"Do you want to continue with Door-{choice} OR switch to Door-{not_chosen_door[0]}? (continue/switch): ")

    # checking whether the car is behind the chosen door, if the user want to continue
    if continue_or_not.lower() == 'continue':
        if three_doors[choice - 1] == "Car":
            print(f"\nYes, your choice is correct. Car is behind the Door-{choice}.\n--YOU WON--")
        else:
            print(f"\nCar is behind the Door-{three_doors.index("Car") + 1}.\n--YOU LOSE--")
        break

    # checking whether the car is behind the door that the user switched to, if the user want to switch
    elif continue_or_not.lower() == 'switch':
        if three_doors[not_chosen_door[0] - 1] == "Car":
            print(f"\nYes, your choice is correct. Car is behind the Door-{not_chosen_door[0]}.\n--YOU WON--")
        else:
            print(f"\nCar is behind the Door-{three_doors.index("Car") + 1}.\n--YOU LOSE--")
        break
    else:
        print("Invalid Entry.Try Again.")
        continue
        
# Opening all three doors to see what is behind each door
print(f"\n{all_opened}")
