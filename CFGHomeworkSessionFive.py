# Question one.
#
# What is PIP?
# PIP is a package manager for Python packages, or modules if you like.
#
# Note: If you have Python version 3.4 or later, PIP is included by default.
#
# What is a Package?
# A package contains all the files you need for a module.
#
# Modules are Python code libraries you can include in your project. You can use
# for example complex maths library that someone else has written.
# Then use that in your own code.


# Question two.

# poem = "I like Python and I am not very good at poems"
#
# with open("poem.txt,", "r") as poem_file:
#     poem_file.write(poem)

# The open() contains "r" which is read.  If we want to write to a file
# We need to use "w"


# Question three

import requests
import json

pokemonIds = [1, 2, 3, 4, 5, 6,]

with open("pokemon.txt", "w") as text_file:
    for x in pokemonIds:
        url = "https://pokeapi.co/api/v2/pokemon/{}/".format(x)
        response = requests.get(url)
        pokemon = response.json()

        pokemon_name = (pokemon['name'])
        pokemon_move = (pokemon['moves'][0]["move"]["name"])

        text_file.writelines([pokemon_name + '\n', json.dumps(pokemon_move) + '\n'])

# import requests
#
# pokemon_number = [5, 26, 14, 7, 74, 13]
#
# for i in pokemon_number:
#     url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(i)
#     url2 = 'https://pokeapi.co/api/v2/move/{}/'.format(i)
#     response = requests.get(url)
#     response2 = requests.get(url2)
#     pokemon = response.json()
#     pokemon_moves = response2.json()
#     all_moves = all_moves + " " + pokemon_moves["name"]
#     end = str((pokemon['name'], all_moves)) + '\n'
#     with open("pokemon.txt","a") as pokemon_file:
#         pokemon_file.write(end)