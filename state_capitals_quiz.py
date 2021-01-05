#!/usr/bin/env python3
# Author: Bradley Pratt
# Created: 01/05/2021
# Last Edit: 01/05/2021

# ########GLOBAL VARIABLES##########
welcomeMessage = "Welcome to the state capitals quiz! I will give you a state and you reply with the correct capital! " \
                 "Enter 's' to skip a state. Let's see if you can get all 50! "
states = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}
score = 0


# ########MAIN FUNCTION##########
def main():
    global score
    score = 0   # reset the score for each new game

    print(welcomeMessage)
    for key in states:  # cycle through each state
        quiz(key)

    print(f"Game complete! Your final score is: {score}")
    if score < 10:
        print("Maybe look at a map sometime!")
    elif score < 20:
        print("You really should've paid attention in school more!")
    elif score < 30:
        print("You know there is a whole other half to the country...right?")
    elif score < 40:
        print("Meh. It could be worse.")
    elif score < 50:
        print("That'll do pig, that'll do.")
    else:
        print("Get a life nerd!")


# ########ACCESSORY FUNCTION##########
def quiz(key):
    answer = ''
    global score

    while answer != 's':    # while the player doesn't want to skip
        answer = input("What is the capital of {}? ".format(key)).lower()

        if answer == 's':   # if they choose to skip, give them the correct answer
            print("You have chosen to skip this state. The correct answer is {}.".format(states.get(key)))
        elif key == "Minnesota" and (answer == "saint paul" or answer == "st paul"):
            # in case they spell out "saint" or skip the ".", they still get it right
            score += 1
            print(f"Correct! Current score: {score}")
            answer = 's'
        elif answer == states.get(key).lower():
            score += 1
            print(f"Correct! Current score: {score}")
            answer = 's'
        else:
            print("Incorrect- please try again or enter 's' to skip.")


# Call the main function
main()

