#!/usr/bin/env python3
# Author: Bradley Pratt
# Created: 01/08/2021
# Last Edit: 01/08/2021

# imports always go at the top of your code
import requests


# ########MAIN FUNCTION##########
def main():
    pokemon = input("Please enter the name of the Pokemon you'd like to research: ").lower()
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    invalidPokemon = True

    # verify that pokemon is in database
    while invalidPokemon:
        try:
            pokeapi = requests.get(url).json()
            invalidPokemon = False
        except:
            print("We're sorry, that Pokemon cannot be found in our database.")
            pokemon = input("Please enter the name of the Pokemon you'd like to research: ").lower()
            url = "https://pokeapi.co/api/v2/pokemon/" + pokemon

    pokemon = pokemon.capitalize()

    # View the link to the artwork
    print("View artwork: ", pokeapi["sprites"]["other"]["official-artwork"]["front_default"])

    # Print the number of games the Pokemon has been in
    print("%s has been in %s different Pokemon games!" % (pokemon, len(pokeapi["game_indices"])))

    # Print out the move list in formatted columns for readability
    colCount = 0
    print("A complete list of %s's moves: " % pokemon)
    for item in pokeapi["moves"]:
        if colCount == 0:
            print("\t", end="")
        print("{:<20}".format(item["move"]["name"]), end="")
        colCount += 1

        if colCount == 5:
            print()
            colCount = 0


# Call the main function
if __name__ == "__main__":
    goAgain = "y"
    while goAgain == "y":
        main()
        print()
        goAgain = input("Would you like to research another Pokemon? (y/n) ")
    print("Gotta catch 'em all!")

