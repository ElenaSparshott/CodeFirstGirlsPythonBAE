import datetime

# age = input('What is your age?')
# print('Hello, I am {} yo'.format(age))
#
# friends = input("How many friends? ")
# pizzas = int(friends) * 0.5
# print('you need {} pizza for {} friends'.format(pizzas, friends))

# Module a library of code that can be reused.
# import <>
# from <>  import


x = datetime.datetime.now()
print(x)

for number in range(20, 26, 2):
    print(number)

for character in 'Banana':
    print(character)


staff = ['Mary', 'Ranjit', 'Fatima', "Ellie"]
for name in staff:
    print(name)

# def name(arguments):
#     statements
#     return value


def hello(name):
    print('Hello,', name)
hello('Ellie')


def some_function(name, job):
    print(name, "is a", job)



def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area

circle_1 = circle_area(3)
print(circle_1)


