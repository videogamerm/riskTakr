import random
import time
import os

def printnm():
    os.system("./Time.out")
    file = open("name.txt","r")
    print("Hello " + file.read())
    

printnm()
play = input("Play y/n ")



def newround():
    os.system("./main.out")
    n = random.randint(1,100)
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)
    n3 = random.randint(1,3)
    m = 250
    m1 = m/5
    bet = input("Do you want to bet " + str(m1) + " Coins that box " + str(n3) + " has a number inside that is at most 10 away from box 2? y/n ")
    if bet == "y":
        if n3 == 1 and n-n1 in range  (10,-10):
            m += m1
            print("Good Job")
        if n3 == 2 and n1-n2 in range  (10,-10):
            m += m1
            print("Good Job")
        if n3 == 3 and n1-n2 in range  (10,-10):
            m += m1
            print("Good Job")
        else:
            m -= m1
            print("You lost " + m1 + "coins")

            


if play == "y":
    m3=input("1(a),5(b),or 10(c) rounds")
    if m3 == "a":
        nrds = 1
    if m3 == "b":
        nrds = 5
    if m3 == "c":
        nrds = 10    
    
    while nrds > 0:
        newround()
        nrds -=1
