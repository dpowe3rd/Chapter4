# Darrell Powe
# This is a practice exercise from the book "Python Crash Course"
# Exercise 4-2

animals = ['spiders', 'snakes', 'dolphins']

for i in range(len(animals)):
    print(animals[i].title())
    print(str(animals[i].title()) + ' are very intelligent creatures.\n')

print(animals[0].title() + ', ' + animals[1].title() + ', and ' + animals[2].title() + ' are some of the worlds smartest creatures.')