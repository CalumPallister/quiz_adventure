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
item = 0


#combat
ehp = 0
enemy = ''

#rooms
roomx = 1
roomy = 1

#other
count = 0
check_paul = 0

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
        combat()
        x1y2()

    elif do == "east":
        roomx = roomx + 1
        combat()
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

    do = input("""Within this room are 2 doorways, one west, the other east.
west or east? """)
    print('')
    
    if do == "west":
        roomx = roomx - 1
        x1y1()
    elif do == "east":
        roomx = roomx + 1
        combat()
        x3y1()
    else:
        what()
        print('')
        x2y1()

def x3y1():
    #blocked room
    global roomx
    global roomy

    do = input("""The way ahead is blocked by fallen rubble, broken bones litter the floor, you should probably go back.
west? """)
    print('')
    
    if do == "west":
        roomx = roomx - 1
        combat()
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
in blood is written the words: 'Eldritch Horror'. You think that escaping this place is probably a good idea...
east, north or south? """)
    print('')

    if do == "south":
        roomy = roomy - 1
        x1y1()
    elif do == "north":
        roomy = roomy + 1
        combat()
        x1y3()
    elif do == "east":
        roomx = roomx + 1
        combat()
        x2y2()
    else:
        what()
        print('')
        x1y2()

def x2y2():
    global roomx
    global roomy

    do = input("""Within this room are 2 doorways, one west, the other east as well as a skeleton hanging from the ceiling.
west or east? """)
    print('')
    if do == "west":
        roomx = roomx - 1
        combat()
        x1y2()
    elif do == "east":
        roomx = roomx + 1
        combat()
        x3y2()
    else:
        what()
        print('')
        x2y2()

def x3y2():
    global roomx
    global roomy

    do = input("""Within this room are 2 doorways, one west, and east.
west or east? """)
    print('')
    if do == "west":
        roomx = roomx - 1
        combat()
        x2y2()
    elif do == "east":
        roomx = roomx + 1
        combat()
        x4y2()
    else:
        what()
        print('')
        x3y2()

def x1y3():
    #note room
    global roomx
    global roomy

    do = input("""There is a doorway to the south, as well as unintelligable writing on the walls.
south? """)
    print('')
    if do == "south":
        roomy = roomy - 1
        combat()
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

    do = input("""There are 2 doorways, one west, the other south; blood stains the south doorway.
west or south? """)
    print('')
    if do == "west":
        roomx = roomx - 1
        combat()
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

    do = input("""There are 2 blocked doorways, and an accessable one is to the east, where a faint blue glow is emitted from within.
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
    #well
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
        combat()
        x5y2()

    elif do == "west":
        roomx = roomx - 1
        combat()
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
    global roomx
    global roomy
    global hp

    do = input("""There are 2 doorways, one is to the north and another to the south, a bloody skull is embedded in the west wall.
north or south? """)
    print('')
    if do == "north":
        roomy = roomy + 1
        combat()
        x5y3()
    elif do == "south":
        roomy = roomy - 1
        x5y1()
    else:
        what()
        print('')
        x5y2()

def x5y3():
    global roomx
    global roomy
    global hp
    
    do = input("""There is a doorway to the west and another to the south, a faint grey mist emerges through a crack in the north wall.
west or south? """)
    print('')
    if do == "west":
        roomx = roomx - 1
        combat()
        x4y3()
    elif do == "south":
        roomy = roomy - 1
        combat()
        x5y2()
    else:
        what()
        print('')
        x5y3()

def x4y3():
    global roomx
    global roomy
    global hp

    do = input("""There are two doorways to the west and east, a note depicts a large hooded creature, in blood is writen: Eldritch Guardian.
west or east? """)
    print('')
    if do == "west":
        roomx = roomx - 1
        combat()
        x3y3()
    elif do == "east":
        roomx = roomx + 1
        combat()
        x5y3()
    else:
        what()
        print('')
        x4y3()

def x3y3():
    global roomx
    global roomy
    global hp

    do = input("""There are doorways to the north and east, this room seems colder than the others.
north or east? """)
    print('')
    if do == "north":
        roomy = roomy + 1
        combat()
        x3y4()
    elif do == "east":
        roomx = roomx + 1
        combat()
        x4y3()
    else:
        what()
        print('')
        x3y3()

def x3y4():
    global roomx
    global roomy
    global hp

    do = input("""There are doorways to the south and west.
south or west? """)
    print('')
    if do == "south":
        roomy = roomy - 1
        combat()
        x3y3()
    elif do == "west":
        roomx = roomx - 1
        combat()
        x2y4()
    else:
        what()
        print('')
        x3y4()

def x2y4():
    global roomx
    global roomy
    global hp

    do = input("""There are doorways to the south and west, the eastern doorway has collapsed.
south or west? """)
    print('')
    if do == "south":
        roomy = roomy - 1
        combat()
        x2y3()
    elif do == "west":
        roomx = roomx - 1
        combat()
        x1y4()
    else:
        what()
        print('')
        x2y4()

def x1y4():
    global roomx
    global roomy
    global hp
    
    combat()
    
    do = input("""There is a doorway to the east and to the north, where a faint blue glow is emitted from within.
north or east? """)
    print('')
    if do == "north":
        roomy = roomy + 1
        x1y5()
    elif do == "east":
        roomx = roomx + 1
        combat()
        x1y4()
    else:
        what()
        print('')
        x2y4()

def x2y3():
    #blocked room
    global roomx
    global roomy

    do = input("""There is nothing in this room other than a pile of bones, you should probably go back.
north? """)
    print('')
    
    if do == "north":
        roomy = roomy + 1
        combat()
        x2y4()
    else:
        what()
        print('')
        x2y3()

def x1y5():
    #well
    global roomx
    global roomy
    global hp
    global mp
    global maxhp
    global maxmp

    do = input("""There is a slightly ruined doorway to the east, a collapsed doorway to the south, and an arcane well in the centre of the room.
heal, east? """)
    print('')

    if do == "east":
        roomx = roomx + 1
        combat()
        x2y5()

    elif do == "heal":
        hp = maxhp
        mp = maxmp
        print("Health and mana restored")
        print('')
        x1y5()

    else:
        what()
        print('')
        x1y5()

def x2y5():
    #mistroom 1
    global roomx
    global roomy

    do = input("""The western doorway collapses, a faint mist pours through the eastern doorway.
east? """)
    print('')
    
    if do == "east":
        roomx = roomx + 1
        combat()
        x3y5()
    else:
        print("You try to do something else, but you are pushed into the next room by an unseen force")
        print('')
        roomx = roomx + 1
        combat()
        x3y5()

def x3y5():
    #mistroom 2
    global roomx
    global roomy

    do = input("""The western doorway collapses, the mist is significantly thicker, you can only go east.
east? """)
    print('')
    
    if do == "east":
        roomx = roomx + 1
        combat()
        x4y5()
    else:
        print("You try to do something else, but you are pushed into the next room by an unseen force")
        print('')
        combat()
        x4y5()

def x4y5():
    #mistroom 3
    global roomx
    global roomy

    do = input("""The western doorway collapses, the mist almost blinds you, you can only go south.
south? """)
    print('')
    
    if do == "south":
        roomy = roomy - 1
        combat()
        x4y4()
    else:
        print("You try to do something else, but you are pushed into the next room by an unseen force")
        print('')
        roomy = roomy - 1
        combat()
        x4y4()

def x4y4():
    #mistroom 4
    global roomx
    global roomy

    do = input("""The northern doorway collapses, a chill surges through you, you can only go east.
east? """)
    print('')
    
    if do == "east":
        roomx = roomx + 1
        combat()
        x5y4()
    else:
        print("You try to do something else, but you are pushed into the next room by an unseen force")
        print('')
        roomx = roomx + 1
        combat()
        x5y4()

def x5y4():
    #mistroom 5
    global roomx
    global roomy

    do = input("""The western doorway collapses. you dont want to, but you can only go north.
north? """)
    print('')
    
    if do == "north":
        roomy = roomy + 1
        combat()
        x5y5()
    else:
        print("You try to do something else, but you are pushed into the next room by an unseen force")
        print('')
        roomx = roomy + 1
        combat()
    
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
    global item
    game = ''
    o = False
    e = randint(1,10)
    if e > 5 or roomx+roomy == 9 or roomx + roomy == 10 or (roomx == 4 and roomy == 4):
        o = True
    elif e < 7 or roomy == 5:
        o = False
    damage = 0
    spell = ''
    if o == True or check_paul == 1:
        checkenemy()
                
        print ('')
        sleep(.5)
        print(enemy, "attacks!")
        print('')
            
        while ehp > 0 and hp > 0:
                    
            attack()                
                    
        if hp < 1:
            print("\n"*100)
            print("""
                                        =========
                                        GAME OVER
                                        =========""")
            sleep(2)
            quit()

        elif ehp < 1:
            endcombat()

def attack():
    global item
    global ehp
    global mp
    global shield

    if item < 1:
        print("Player hp:", hp,"Player mp:", mp,"Barrier hp:", shield, "Enemy hp:", ehp)
        print('')
    elif item > 0:
        print("Player hp:", hp,"Player mp:", mp,"Damage boost: +", item,"Barrier hp:", shield, "Enemy hp:", ehp)
        print('')
    
    do = input("use attack, spell or shield? ")
    print('')
            
    if do == "attack":
        damage = (randint(roomx+roomy, roomx+roomy+10)+item)
        
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
            attack()
                  
    elif do == "shield":
        if mp - (roomx+roomy)//4 > 0:
            shield = (roomx*roomy)*10
            mp = mp - shield//6
            print("You project an arcane barrier that will absorb",shield, "damage.")
        else:
            print("Not enough mp!")
            print('')
            attack()
            
    else:
        what()
        print('')

    if do == "shield" or do == "spell" or do == "attack":
        if "Eldritch" in enemy:
            eldritchattack()
        else:
            enemyattack()

def eldritchattack():
    global hp
    global shield
    global ehp
    global enemy
    if ehp > 0:
        y = randint(1,20)
        if y < 19:
            edamage = randint(roomx*2+roomy*2,roomx*5+roomy*5)
            if roomx + roomy == 10:
                edamage = randint(25, 75)
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
        elif y == 19 and shield > 0:
            edamage = shield//2
            if shield > 0:
                shield = shield - edamage
                if shield > 0:
                    print("Your arcane barrier was torn in half!")
                else:
                    shield = 0
                    print("Your arcane barrier was reduced to shreds!")
              
        else:
            regain = roomx+roomy+ehp//20
            ehp = ehp + regain
            print(enemy,"gained", regain,"hp!")
                
def enemyattack():
    global hp
    global shield
    global ehp
    global enemy
    global check_paul
    if check_pail == 1:
        ehp = 999999999
        edamage = 999999999
        if shield > 0:
            shield = shield - edamage
            if shield > 0:
                print("Your arcane barrier received", edamage,"damage!")
            elif shield < 1:
                shield = 0
                print("Your arcane barrier was destroyed!")
                sleep(5)
        else:
            hp = hp - edamage
            print("You received",edamage,"damage!")
            sleep(2)
            print("Your body is engulfed in fire")
            sleep(2)
            print("\n"*100)
            print("""
                                        =========
                                        GAME OVER
                                        =========""")
            sleep(2)
            quit()
                
    elif enemy != "Paul" and ehp > 0:
        y = randint(1,10)
        if y < 9:
            edamage = randint(roomx*2+roomy*2,roomx*5+roomy*5)
            if roomx + roomy == 10:
                edamage = randint(25, 75)
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
            regain = roomx+roomy+ehp//10
            ehp = ehp + regain
            print(enemy,"gained", regain,"hp!")

def checkenemy():
    global ehp, enemy, hp, mp
    ehp = (roomx*roomy*8)
    if roomx + roomy == 9 or (roomx == 4 and roomy == 4):
        ehp = 200
    if roomx + roomy == 10:
        ehp = 1000 
    
    shield = 0
    paul = randint(1,1000)
    if paul == 1 or check_paul == 1:
        print("A creature emerges from the darkness, It's head blazes with fire")
        enemy = "Paul"
        return
    if check_paul != 1:
        if roomx+roomy < 4:
            print("An unerving chill sweeps through your body.")
            enemy = "Goblin"
        elif roomx+roomy < 6:
            print("Something lurks in the darkness.")
            enemy = "Orc"
        elif roomx+roomy == 9 or (roomx == 4 and roomy == 4) :
            print("A cold stare peirces your soul.")
            enemy = "Eldritch Guardian"
        elif roomx+roomy == 10:
            print("You become overwhelmed with dread.")
            enemy = "Eldritch Horror"
            mp = 250
            hp = 100
        else:
            print("You hear breathing behind you.")
            enemy = "Troll"
        
def item_check():
    global item

    checkitem = randint(1,100)
    if checkitem < 6 and item < 5:
        item = 5
        print("Aquired a steel shortsword! Damage boost:",item)
    if checkitem > 5 and checkitem < 10 and item < 25:
        item = 25
        print("Aquired an enchanted sabre! Damage boost:",item)
    if checkitem > 9 and checkitem < 13 and item < 50:
        item = 50
        print("Aquired a mythril greatsword! Damage boost:",item)
    if checkitem > 12 and checkitem < 14 and item < 75:
        item = 75
        print("Aquired the vampiric dagger! Damage boost:",item)
    
    if checkitem == 14 and item < 100:
        item = 100
        print("Aquired the Slayer of The Eldritch! Damage boost:",item)
    print('')
    
def endcombat():
    global hp
    global mp
    global maxmp
    print(enemy, "was slain!")
    print('')

    item_check()

    if enemy == "Eldritch Guardian":
        print("Max Mp increased to:", maxmp+50)
        maxmp = maxmp + 50
        print("Health and mana restored.")
        hp = 100
        mp = maxmp
    elif enemy == "Eldritch Horror":
        print('')
        sleep(1)
        print("As the last sliver of life ebbs out of the Eldritch Horror, the northern wall is destroyed by a beam of light.")
        print('')
        sleep(1)
        print("You walk out, the blue sky is above you, the sun's heat warming the chill that was hung over your soul.")
        print('')
        sleep(2)
        print("You are free.")
        print('')
        sleep(2)
        print("""
                                   =========
                                    YOU WIN
                                   =========""")
        print('')
        sleep(3)
        print("Credits:")
        print("everything - Calum Pallister")
        print('')
        sleep(2)
        print("Special thanks to:")
        print("Luke Briggs, Harry Reed & Issac Douglas")
        print('')
        sleep(2)
        print("Thank you for playing!")
        sleep(3)
        quit()    
                
def coridoor():
    global hp
    global check_paul
    game = ''
    if hp == 100:
        do = input("You enter a long dark hallway. Do you proceed? yes or no? ")
    elif hp == 75:
        do = input("Voices whisper within the depths... Do you proceed? ")
    elif hp == 50:
        do = input("Blood grows upon the walls... Do you proceed? ")
    elif hp == 25:
        do = input("Distant wailing draws nearer... Do you proceed? ")

    if do == "paul":
        check_paul = 1
        combat()
    print('')
    if do == "yes":
        hp = hp - 25
        if hp < 1:
            hp = 100
            print("\n"*50)
            sleep(5)
            print("Your soul freezes.")
            sleep(2)
            print("You begin to bleed")
            sleep(2)
            print("your life is ripped from you.")
            while hp > 0:
                print("Hp:",hp)
                hp = hp // 8
                print("\n"*50)
                sleep(.05)
            if hp < 1:
                sleep(5)
                print("\n"*50)
                print("""
                                        =========
                                        GAME OVER
                                        =========""")
                sleep(2)
                game = "over"
                quit()
        elif hp > 0:
            coridoor()
    elif do == 'no':
        hp = 100
        x4y1()


if __name__ == "__main__":
    start()
    
