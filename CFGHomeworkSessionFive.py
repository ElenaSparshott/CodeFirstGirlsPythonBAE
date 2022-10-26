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

pokemonIds = [1, 2, 3, 4, 5, 6,]

for x in pokemonIds:
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(x)
    response = requests.get(url)
    pokemon = response.json()

    print(pokemon['name'])
    print(pokemon['moves'])


