import random
chance=5
count=0
getstage=int(input("Enter the stage: "))
value=int(getstage*10)
n = random.randint(1, value)

guess = int(input("Enter an integer from 1 to "+str(value)+": "))
while chance >=count:
    if chance==count:
       print("Your chances are over,Better luck next time!")
       break
    #n != "guess":
    count = count+1
    print("No of Chances :  "+str(count))
    if guess < n:
        print ("the number is low than the random number")
        guess = int(input("Enter an integer from 1 to "+str(value)+": "))
    elif guess > n:
        print  ("the number is high than the random number")
        guess = int(input("Enter an integer from 1 to "+str(value)+": "))
    else:
        print ("You won the game!")
        break