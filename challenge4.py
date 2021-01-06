#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# Part 1: Write a for loop that returns all the animals from the NE Farm!
print("The NE Farm raises: ")
for animal in farms[0].get("agriculture"):
    print(animal)
print()

# Part 2: Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on
# that farm.
choice = -1

while choice != 1 and choice != 2 and choice != 3:
    choice = input(f"Please enter the corresponding # for which farm you would like to see details about:\n\t[1] NE "
                   f"Farm\n\t[2] W Farm\n\t[3] SE Farm\n")

    if choice == "1" or choice == "2" or choice == "3":
        choice = int(choice) - 1
        print("The {} raises: ".format(farms[choice].get("name")))
        for animal in farms[choice].get("agriculture"):
            print(animal)
    else:
        print("Invalid choice, please try again.")
        choice = -1

# Part 3: Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular 
# farm. 
choice = -1

while choice != 1 and choice != 2 and choice != 3:
    choice = input(f"Please enter the corresponding # for which farm you would like to see details about:\n\t[1] NE "
                   f"Farm\n\t[2] W Farm\n\t[3] SE Farm\n")

    if choice == "1" or choice == "2":
        choice = int(choice) - 1
        print("The {} raises: ".format(farms[choice].get("name")))
        for animal in farms[choice].get("agriculture"):
            print(animal)
    elif choice == "3":
        choice = int(choice) - 1
        print("The {} raises: ".format(farms[choice].get("name")))
        print(farms[choice].get("agriculture")[0])
    else:
        print("Invalid choice, please try again.")
        choice = -1
