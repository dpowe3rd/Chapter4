# Darrell Powe
# This is a practice exercise from the book "Python Crash Course"
# Exercises 4-11 & 4-12

pizza = ['pepperoni', 'cheese', 'bacon', 'extra cheese']
friend_pizza = pizza[:]

pizza.append('sausage')

for i in range(len(pizza)):
    # print(pizza[i].title())
    print('I like ' + str(pizza[i].title()) + ' pizza, it taste very good.')

print('\nI love pizza.\n')

friend_pizza.append('supreme')

for i in range(len(friend_pizza)):
    # print(friend_pizza[i].title())
    print('My friend likes ' + str(friend_pizza[i].title()) + ' pizza, they say it  tastes very good.')

print('\nThey love pizza too.')

