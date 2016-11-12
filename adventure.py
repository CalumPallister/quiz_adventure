from random import randint
from time import sleep

print("ARCHAIC DUNGEON")
print("===============")
print('')

#player
hp = 100
mp = 100
equip = ''
equipd = 0
maxhp = 100
maxmp = 100

#combat
ehp = 0
enemy = ''

#rooms
roomx = 1
roomy = 1

#other
count = 0

def what():
    response = ''
    unknown = randint(1,10)
    if unknown == 1:
        response = "Not sure you can do that..."
    elif unknown == 2:
        response = "Care to repeat that?"
    elif unknown == 3:
        response = "Nope..."
    elif unknown == 4:
        response = "Try again?"
    elif unknown == 5:
        response = "Flavour text..."
    elif unknown == 6:
        response = "You sure about that?"
    elif unknown == 7:
        response = "Nada..."
    elif unknown == 8:
        response = "I don't think that was an option..."
    elif unknown == 9:
        response = "You might want to type that right next time..."
    elif unknown == 10:
        response = "Nothing..."
    
    print(response)
    sleep(.5)

def start():
    global name
    main = input("press enter to start or type ? and enter for instructions ")
    print('')
    
    if main == '':
        print('')
        intro()

    elif main == '?':
        print('')
        print("""Instructions:
   When asked to type something, type it EXACTLY as shown.
   When your health reaches 0, it's game over, so don't let that happen.
   Monsters, their attacks and your attacks grow stronger depending your distance
   from the starting area.
         """)
        sleep(1)
        start()

    else:
        what()
        print('')
        start()

def intro():
        print("You awaken to a dark, damp room with a sliver of light emerging from the ceiling.")
        print('')
        sleep(1)
        print("Shackles bind you to the wall.")
        print('')
        sleep(1)
        trapped()
        
def trapped():
    global count

    do = input("Try to escape? yes or no? ")
    print('')      

    if do == 'yes':
        print('You notice that the shackles are rather rusty and you try to break them.')
        print('')
        sleep(1)
        print('The chains snap and you are free.')
        print('')
        x1y1()
        
    elif do == 'no':
        if count == 0:
            print("There's honestly nothing better to do.")
        elif count == 1:
            print("What are you trying?")
        elif count == 2:
            print("Just type yes and play the game already...")
        elif count == 3:
            print("...")
        elif count == 4:
            print("WHY ARE YOU STILL DOING THIS!?")
        else:
            print('You notice that the shackles are rather rusty and you try to break them.')
            sleep(1)
            print('')
            print('The chains snap and you are free.')
            print('')
            x1y1()

            
        print('')
        count = count + 1
        trapped()
                      
    else:
        what()
        print('')
        trapped()

def x1y1():
    #start
    global roomx
    global roomy
    global hp
    global mp
    global maxhp
    global maxmp

    do = input("There are 2 slightly ruined doorways before you, one to the north and to the east as well as an arcane well. heal, up or right? ")
    print('')

    if do == "up":
        roomy = roomy + 1
        x1y2()

    elif do == "right":
        roomx = roomx + 1
        x2y1()

    elif do == "heal":
        hp = maxhp
        mp = maxmp
        print("Health and mana restored")
        x1y1()

    else:
        what()
        print('')
        x1y1()

def x2y1():
    #combat room
    global roomx
    global roomy
    global hp
    global mp
    global maxhp
    global maxmp
    
    combat()

    do = input("Within this room are 2 doorways, one west, the other east. left or right? ")
    print('')
    
    if do == "left":
        roomx = roomx - 1
        x1y1()
    elif do == "right":
        roomx = roomx + 1

    else:
        what()
        print('')
        x2y1()
    
def combat():
    global roomx
    global roomy
    global hp
    global mp
    global maxhp
    global maxmp
    global enemy
    global ehp

    e = randint(1,5)
    if e > 3:
        o = True
    else:
        o = False
    
    damage = 0
    spell = ''
    shield = 0
    if ehp < 1 and o == True:

        if roomx+roomy <= 5:
            print("An unerving chill sweeps through your body.")
            enemy = "Goblin"
        elif roomx+roomy <= 10:
            print("Something lurks in the darkness.")
            enemy = "Orc"
        elif roomx+roomy <= 15:
            print("Something is watching you.")
            enemy = "Golem"
        elif roomx+roomy <= 20:
            print("You hear breathing behind you.")
            enemy = "Troll"
        elif roomx+roomy < 25:
            print("A cold stare peirces your soul.")
            enemy = "Eldritch Guardian"
        elif roomx+roomy == 25:
            print("You become overwhelmed with dread")
            enemy = "Eldrich Horror"
            
        ehp = (roomx*roomy*8)
        print ('')
        sleep(.5)
        combat()
        print(enemy, "attacks!")
        print('')
        
    elif ehp > 0:

        print("Player hp:", hp, " Enemy hp:", ehp)
        print('')
        
        do = input("use attack, spell or shield? ")
        print('')
        
        if do == "attack":
            damage = (randint(roomx+roomy, roomx+roomy+10))
            
            print('You attack the', enemy, 'and deal',damage, "damage.")
            ehp = ehp - damage
            
            print(ehp)
        elif do == "spell":

            x = randint(1, 4)
            if x == 1:
                spell = "fireball"
            elif x == 2:
                spell = "frost bolt"
            elif x == 3:
                spell = "lightning"
            elif x == 4:
                spell = "purify"

            damage = randint(roomx+room, (roomx*10 + roomy*10)//2)
            damagedone = damage
            print("You cast", spell, "on the", enemy, "and deal",damage,"damage.")
            ehp = ehp - damage
            mp = mp - (damage // 2)
                      
        elif do == "shield":
            shield = (roomx+roomy)*10
            mp = mp - shield//2
            print("You project an arcane barrier that will absorb",shield, "damage")

        if hp < 1:
            Print("""
                                       =========
                                       GAME OVER
                                       =========""")
            quit
        elif ehp > 0:
            combat()
        else:
            print(enemy, "defeated!")
        print('')
    

# Leave this at the bottom - it makes start run automatically when you
# run your code.
if __name__ == "__main__":
    start()
