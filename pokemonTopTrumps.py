import random
import requests


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        # want photo here - could have
        # must have 3 characteristics, could have 5 ideally (rarity?)
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'stats': pokemon['stats'],
    }

    # 'name_length' : len("name"),


# a = "Hello, World!"
# print(len(a))

# {'base_stat': 45,
#  'effort': 0,
#  'stat': {'name': 'speed',
#  'url': 'https://pokeapi.co/api/v2/stat/6/'}}],

def run():
    # could have two cards flashing up
    # could assign number values to moves so can compare
    # could print results to text file to record
    my_pokemon = random_pokemon()
    print('You were given     {}'.format(my_pokemon['name']))
    stat_choice = input('Which stat do you want to use? (id, height, weight, stats) ')
    opponent_pokemon = random_pokemon()
    print('The opponent chose   {}'.format(opponent_pokemon['name']))
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')

    elif my_stat < opponent_stat:
        print('You Lose!')

    else:
        print('Draw!')


run()
