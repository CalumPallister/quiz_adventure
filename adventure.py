from random import randint
from time import sleep

print("ARCHAIC DUNGEON")
print("===============")
print('')

#player
hp = 100
mp = 100
shield = 0
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

    do = input("""Try to escape?
yes or no? """)
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

    do = input("""There are 2 slightly ruined doorways before you, one to the north and to the east as well as an arcane well in the centre of the room.
heal, north or east? """)
    print('')

    if do == "north":
        roomy = roomy + 1
        x1y2()

    elif do == "east":
        roomx = roomx + 1
        x2y1()

    elif do == "heal":
        hp = maxhp
        mp = maxmp
        print("Health and mana restored")
        print('')
        x1y1()
        

    else:
        what()
        print('')
        x1y1()

def x2y1():
    #combat room
    global roomx
    global roomy
    
    combat()

    do = input("""Within this room are 2 doorways, one west, the other east.
west or east? """)
    print('')
    
    if do == "west":
        roomx = roomx - 1
        x1y1()
    elif do == "east":
        roomx = roomx + 1
        x3y1()
    else:
        what()
        print('')
        x2y1()

def x3y1():
    #blocked room
    global roomx
    global roomy

    combat()

    do = input("""The way ahead is blocked by fallen rubble, broken bones litter the floor, you should probably go back.
west? """)
    print('')
    
    if do == "west":
        roomx = roomx - 1
        x2y1()
    else:
        what()
        print('')
        x3y1()

def x1y2():
    #note room
    global roomx
    global roomy

    do = input("""There are doorways south, north and east, a note on the floor depicts a creature that is soul-peircingly grotesque;
in blood is written the words 'Eldritch Horror', you think that escaping this place is probably a good idea...
east, north or south? """)
    print('')

    if do == "south":
        roomy = roomy - 1
        x1y1()
    elif do == "north":
        roomy = roomy + 1
        x1y3()
    elif do == "east":
        roomx = roomx + 1
        x2y2()
    else:
        what()
        print('')
        x1y2()

def x2y2():
    #combat room
    global roomx
    global roomy

    combat()
    
    do = input("""Within this room are 2 doorways, one west, the other east as well as a skeleton hanging from the ceiling.
west or east? """)
    print('')
    if do == "west":
        roomx = roomx - 1
        x1y2()
    elif do == "east":
        roomx = roomx + 1
        x3y2()
    else:
        what()
        print('')
        x2y2()

def x3y2():
    #combat room
    global roomx
    global roomy

    combat()
    
    do = input("""Within this room are 3 doorways, one west, east, and north.
west, east or north? """)
    print('')
    if do == "west":
        roomx = roomx - 1
        x2y2()
    elif do == "east":
        roomx = roomx + 1
        x4y2()
    else:
        what()
        print('')
        x3y2()

def x1y3():
    #note room
    global roomx
    global roomy

    combat()
    
    do = input("""There is a doorway to the south, as well as unintelligable writing on the walls.
south? """)
    print('')
    if do == "south":
        roomy = roomy - 1
        x1y2()
    else:
        what()
        print('')
        x1y3()

def x4y2():
    #coridoor
    global roomx
    global roomy
    global hp
    
    combat()
    
    do = input("""There are 2 doorways, one west, the other south; blood stains the south doorway.
west or south? """)
    print('')
    if do == "west":
        roomx = roomx - 1
        x3y2()
    elif do == "south":
        roomy == roomy - 1
        hp = 100
        coridoor()
        x4y1()
    else:
        what()
        print('')
        x4y2()

def x4y1():
    #Blocked room
    global roomx
    global roomy
    global hp
    
    combat()
    
    do = input("""There are 2 blocked doorways, and an accessable one is to the east, where a faint blue glow is emmited from within.
east? """)
    print('')
    if do == "east":
        roomx = roomx + 1
        x5y1()
    else:
        what()
        print('')
        x4y1()

def x5y1():
    #start
    global roomx
    global roomy
    global hp
    global mp
    global maxhp
    global maxmp

    do = input("""There are 2 slightly ruined doorways before you, one to the north and to the west as well as an arcane well in the centre of the room.
heal, north or west? """)
    print('')

    if do == "north":
        roomy = roomy + 1
        x5y2()

    elif do == "west":
        roomx = roomx - 1
        x4y1()

    elif do == "heal":
        hp = maxhp
        mp = maxmp
        print("Health and mana restored")
        print('')
        x5y1()

    else:
        what()
        print('')
        x5y1()

def x5y2():
    #Combat room
    global roomx
    global roomy
    global hp
    
    combat()
    
    do = input("""There are 2 doorways, one is to the north and another to the south, a skull is embedded in the west wall.
north or south? """)
    print('')
    if do == "north":
        roomy = roomy + 1
        x5y3()
    elif do == "south":
        roomy = roomy - 1
        x5y3()
    else:
        what()
        print('')
        x5y2()

def x5y3():
    #Combat room
    global roomx
    global roomy
    global hp
    
    combat()
    
    do = input("""There is a doorway to the west and another to the south, .
west or south? """)
    print('')
    if do == "west":
        roomy = roomy + 1
        x5y3()
    elif do == south
    else:
        what()
        print('')
        x5y2()
    
def combat():
    global roomx
    global roomy
    global hp
    global mp
    global shield
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
    if ehp < 1 and o == True:
        shield = 0
        if roomx+roomy < 4:
            print("An unerving chill sweeps through your body.")
            enemy = "Goblin"
        elif roomx+roomy < 6:
            print("Something lurks in the darkness.")
            enemy = "Orc"
        elif roomx+roomy < 8:
            print("You hear breathing behind you.")
            enemy = "Troll"
        elif roomx+roomy < 10:
            print("A cold stare peirces your soul.")
            enemy = "Eldritch Guardian"
        elif roomx+roomy == 10:
            print("You become overwhelmed with dread.")
            enemy = "Eldritch Horror"
            
        ehp = (roomx*roomy*8)
        print ('')
        sleep(.5)
        print(enemy, "attacks!")
        combat()
        print('')
        
    elif ehp > 0:

        print("Player hp:", hp,"Player mp:", mp,"Barrier hp:", shield, "Enemy hp:", ehp)
        print('')
        
        do = input("use attack, spell or shield? ")
        print('')
        
        if do == "attack":
            damage = (randint(roomx+roomy, roomx+roomy+10))
            
            print('You attack the', enemy, 'and deal',damage, "damage.")
            ehp = ehp - damage
            
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

            damage = randint(roomx+roomy, (roomx*10 + roomy*10)//2)
            if mp - (roomx+roomy) > 0:
                print("You cast", spell, "on the", enemy, "and deal",damage,"damage.")
                ehp = ehp - damage
                mp = mp - (damage // 2)
            else:
                print("Not enough mp!")
                print('')
                combat()
                      
        elif do == "shield":
            if mp - (((roomx+roomy)*10)//4) > 0:
                shield = (roomx+roomy)*10
                mp = mp - shield//4
                print("You project an arcane barrier that will absorb",shield, "damage.")
            else:
                print("Not enough mp!")
                print('')
                combat()
        else:
            what()
            print('')
            combat()

        y = randint(1,5)
        if y < 5:
            if ehp > 0:
                edamage = randint(roomx*2+roomy*2,roomx*5+roomy*5)
                if shield > 0:
                    shield = shield - edamage
                    if shield > 0:
                        print("Your arcane barrier received", edamage,"damage!")
                    else:
                        shield = 0
                        print("Your arcane barrier was destroyed!")
                else:
                    hp = hp - edamage
                    print("You received",edamage,"damage!")
        else:
            if ehp > 0:
                regain = roomx+roomy+ehp//10
                ehp = ehp + regain
                print(enemy,"gained", regain,"hp!")
            

        if hp < 1:
            print('')
            print("""
                                       =========
                                       GAME OVER
                                       =========""")
            sleep(2)
            quit
        if ehp > 0 and hp > 0:
            sleep(0.5)
            combat()
        elif ehp < 1:
            print(enemy, "was slain!")

def coridoor():
    global hp
    
    if hp == 100:

        do = input("You enter a long dark hallway. Do you proceed? yes or no? ")

    elif hp == 75:

        do = input("The walls now have small splatters of blood upon them... Do you proceed? ")

    elif hp == 50:

        do = input("Blood grows upon the walls... Do you proceed? ")

    elif hp == 25:

        do = input("Distant wailing draws nearer... Do you proceed? ")

            
    print('')
    if do == "yes":
        hp = hp - 25
        if hp < 1:
            print("""





















































""")
            print("Feelings lost and taken away,")
            sleep(1.5)
            print("Reaching out this fateful day,")
            sleep(1.5)
            print("Sudden pain within your veins,")
            sleep(1.5)
            print("Bursting, causing large red stains,")
            sleep(1.5)
            print("He speaks of words with unknown meaning,")
            sleep(1.5)
            print("All this you knew,")
            sleep(1.5)
            print("From knowledge gained while dreaming.")
            sleep(3)
            print("""





















































""")
            print("""
                                    =========
                                    GAME OVER
                                    =========""")
            sleep(2)
            quit
        else:
            coridoor()
    else:
        hp = 100
        x4y1()

# Leave this at the bottom - it makes start run automatically when you
# run your code.
if __name__ == "__main__":
    start()
