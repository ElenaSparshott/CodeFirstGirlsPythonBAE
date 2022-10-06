import random

# for i in range(9):
#     print('~'* i)

#
# price = float(input("What is the price of the burger?"))
# within = float(price) <= 10.00
# veggie = input("Is there a veggie option? y/n ")
# meets = within and veggie == 'y'
# is_a_good_option = within and veggie
#
# if is_a_good_option:
#     print(f"burger meal {meets}")
# if not is_a_good_option:
#     print("no")
#
# meal_price = float(input("How much did the meal cost? "))
# discount_choice = input("Do you have a discount? y/n ")
# discount_applicable = discount_choice == 'y'
#
# if discount_applicable:
#     newPrice = meal_price * 0.9
#     print(f"yes discount {newPrice}")
# if not discount_applicable:
#     print(f"no discount {meal_price}")


# password = input("password: ")
# if password.strip() == 'bobby':
#     print("success")
# else:
#     print("no")

# temp = int(input('What is the temperature: '))
# if temp > 200:
#     print("The oven is too hot")
# elif temp < 150:
#     print("The oven is too cold")
# elif temp == 180:
#     print("The oven is at the perfect temperature")
# else:
#     print("The temperature is close enough")

def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = "rock"
    elif choice_number == 2:
        choice = "scissors"
    else:
        choice = 'paper'

    return choice


my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))

if my_choice == opponent_choice:
    print('You Draw!')
elif my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')
elif my_choice == 'rock' and opponent_choice == 'paper':
    print('You lose!')
elif my_choice == 'paper' and opponent_choice == 'scissors':
    print('You lose!')
elif my_choice == 'paper' and opponent_choice == 'rock':
    print('You win!')
elif my_choice == 'scissors' and opponent_choice == 'rock':
    print('You lose!')
else:
    my_choice == 'scissor' and opponent_choice == 'paper'
    print('You win!')
