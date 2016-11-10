# Our quiz!

from time import sleep

def quiz():
    correct = 0
    wrong = 0
    print("Welcome!")
    
    sleep(1)
    #1
    Q = input("What is the code used for pausing a code for a certain time? ")
    sleep(.5)
    if Q == "time.sleep()":
        print(Q, "is correct!")
        correct = correct + 1
    else:
        print(Q, "is incorrect!")
        wrong = wrong + 1
    sleep(1)
    #2
    Q = input("What version of python are we using right now? ")
    sleep(.5)
    if Q == "3.3.2":
        print(Q, "is correct!")
        correct = correct + 1
    else:
        print(Q, "is incorrect!")
        wrong = wrong + 1
    sleep(1)
    #3
    Q = input("Is this computer 32 or 64 bit? ")
    sleep(.5)
    if Q == "32":
        print(Q, "is correct!")
        correct = correct + 1
    else:
        print(Q, "is incorrect!")
        wrong = wrong + 1
    sleep(1)
    #4
    Q = input("How old is the person that made this quiz? ")
    sleep(.5)
    if Q == "14":
        print(Q, "is correct!")
        correct = correct + 1
    else:
        print(Q, "is incorrect!")
        wrong = wrong + 1
    sleep(1)
    #5
    Q = input("When was the launch date of Windows 10 (use small date)? ")
    sleep(.5)
    if Q == "29.7.16":
        print(Q, "is correct!")
        correct = correct + 1
    else:
        print(Q, "is incorrect!")
        wrong = wrong + 1
    sleep(1)

    print("You got ",correct, "correct and ",wrong, "wrong")
    if correct == 5:
        print("Well done!")
    elif correct > wrong:
        print("Not bad")
    elif wrong > correct:
        print("Could be better")
    elif wrong == 5:
        print("You did terrible")
    
        
    





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
