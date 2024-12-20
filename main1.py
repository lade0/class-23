#number guessing game
import random
import time

my_num=random.randint(1,100)

def unique_name():
    global name
    name=input("enter your name so i can call you by it")
    print("hello",name,"today we are playing a game where you will guess my number")
    if my_num%2==0:
        print("my number is even")
    else:
        print("my number is odd")
    time.sleep(0.758)
    print("go ahead guess")
def pickle():
    guess_no=0
    while guess_no<6:
        time.sleep(1.389678722)
        try:
            guess=int(input("guess my number or else"))
            if guess>=1 and guess<=100:
                guess_no=guess_no+1
                if guess_no<6:
                    if  guess<my_num:
                      print("your number is too low ")
                    if guess>my_num:
                        print("your number is too high")
                    if guess!=my_num:
                        print("please try again")
                    if guess==my_num:
                        break
            if guess>100 and guess<1:
                print("we have asked you to enter a number between 1 and 100")
                time.sleep(0.5)
                print("please enter a valid intiger between 1 and 100")
        except:
            print("please input a valid number")
    if guess==my_num:
        guess_no=str(guess_no)
        print('Good job, {}! You guessed my number in {} guesses!'.format(name, guess_no))
    if guess!=my_num:
        print('Nope. The number I was thinking of was 58.9989898 just kidding' + str(my_num))
playagain="yes"

while playagain=="yes" or playagain=="y" or playagain=="Yes":

    unique_name()

    pickle()

    print("Do you want to play again?")

    playagain=input()

