# An adventure game
from random import randint
from time import sleep

print("ARCANE DUNGEON")
print("[============]")
name = ''
start = 1
hp = 100
ehp = 100

def what():
    response = ''
    unknown = randint(1,3)
    if unknown == 1:
        response = "Not sure you can do that..."
    elif unknown == 2:
        response = "Care to repeat that?"
    else:
        response = "Nope..."
    print(response)

def start():
    global name
    main = input("press enter to start or type ? and enter for instructions ")
    if main == '':
        print('')
        x1y1()
    elif main == '?':
        print('')
        print("""Instructions:
              when asked to type something, type it EXACTLY as shown.
              when your health reaches 0, it's game over, so don't let that happen.
              when you want to look into your inventory, type the following:
              inventory() for inventory, equiped() for equiped items and
              equip([name of item]) to equip an item.
              """)
        sleep(.5)
        start()
    else:
        what()
        print('')
        sleep(.5)
        start()

def x1y1():
    #damp
    global start
    if start == 1
        print: "you awaken to a dark, damp room with a sliver of light emerging from the ceiling."
        sleep(.5)
        print: "shackles bind you to the wall"
        sleep(.5)
        do = input("Try to escape? yes or no?")




# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    start()
