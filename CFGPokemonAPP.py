# https://www.futurelearn.com/info/courses/block-to-text-based-programming/0/steps/39498

import random
import requests
import pandas as pd


# import matplotlib.pyplot as plt

# for x in range(0,3):
def retrieve_pokemon(pokemon_number):  # random_pokemon():
    # pokemon_number = random.randint(1, 151)

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],
        'order': pokemon['order']
        # webbrowser.open(poke.sprites.front_default)
    }


def run():
    my_pokemon = retrieve_pokemon(random.randint(1, 151))
    print('You were given {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight, base_experience, order) ')
    opponent_pokemon = retrieve_pokemon(random.randint(1, 151))
    print('The opponent chose {}'.format(opponent_pokemon['name']))
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    results = ""
    if my_stat > opponent_stat:
        print('You Win!')
        results = 3  # "You win!"
    elif my_stat < opponent_stat:
        print('You Lose!')
        results = 0  # "You lose!"
    else:
        print('Draw!')
        results = 1  # "Draw"
    return results


def write_to_file(text):
    with open("pokemon.txt", "a") as pokemon_file:
        pokemon_file.write(text)


score = 0
for x in range(0, 6):
    # pokemon_number = random.randint(1, 151)
    # retrieve_pokemon(random.randint(1, 151))
    winnings = run()
    score = score + winnings

    write_to_file(str(winnings) + "\n")

print(score)

# need to create a list/arrray for bar chart - done - dataframe should generate from below if next to do done
# need to import pandas and matplotlib
# need to connect score with the score being generated

list_of_dicts = [
    {"player 1": 25},
    {"player 2": 42}
]
# dict_of_lists ={
# "name": ["player_1", "player_2"],
# "score": [25, 42]
# }

player_results = pd.DataFrame(list_of_dicts)

print(player_results)

# def graph of player_results

# plt.bar(df.player_results)

# x_axis = plt.xlabel('player name') - not needed
# y_axis = plt.ylabel('number of points')
# plt.show()


# import random
# import requests

# def random_pokemon():
#   pokemon_number =     random.randint(1, 151)
#   url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
#   response = requests.get(url)
#   pokemon = response.json()
#   return {
#   'name': pokemon['name'],
#   #want photo here - could have
#   #must have 3 characteristics, could have 5 ideally (rarity?)
#   'id': pokemon['id'],
#   'height': pokemon['height'],
#   'weight': pokemon['weight'],
#   'stats' : pokemon['stats'],
#   'base_experience': pokemon['base_experience'],
#   'order': pokemon['order']
# }

#   # 'name_length' : len("name"),

# # a = "Hello, World!"
# # print(len(a))

# def run():
# #could have two cards flashing up
# # could assign number values to moves so can compare
# #could print results to text file to record
#   my_pokemon = random_pokemon()
#   print('You were given     {}'.format(my_pokemon['name']))
#   stat_choice = input('Which stat do you want to use? (id, height, weight, base_experience, order) ')
#   opponent_pokemon = random_pokemon()
#   print('The opponent chose   {}'.format(opponent_pokemon['name']))
#   my_stat = my_pokemon[stat_choice]
#   opponent_stat = opponent_pokemon[stat_choice]

#   if my_stat > opponent_stat:
#     print('You Win!')

#   elif my_stat < opponent_stat:
#     print('You Lose!')

#   else:
#     print('Draw!')

# run()