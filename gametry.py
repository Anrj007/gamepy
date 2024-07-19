import random
import time

Lg=["num"]
def mainmenu():
    curr = time.time()
    Lg=["num"]
    txt=("ａｖａｉｌａｂｌｅ ｇａｍｅｓ")
    new_str = txt.center(130)
    print("\n", new_str)
    for i in Lg:
        print(f"-{i}")
    print("\n \n")

    
def game1():
    print("\n \n      ▛▟ ▙▟ ▛▚▞▜  \n \n ")
    try:
        a= int(input("which table you want to play with: "))
        b=int(input("till what multiple? "))
    except:
        print("try again :) ")
        a= int(input("which table you want to play with: "))
        b=int(input("till what multiple? "))

    L=[]
    sc=int("0")
    for i in range (a,a*b,a):
        L.append(i)
    for i in range(0,au1):
        a1=str(a)
        try:
            ab=random.choice(L)
        except:
            print("Program is closing due to some internal error!!")
            break

        ab1=str(ab)
        curr1= time.time()
        try:
            u=input(f'what multiple is {ab1} of {a1}? :')
            u=int(u)
        except:
            u=input(f'try again,what multiple is {ab1} of {a1}? :')
            u=int(u)
        curr2= time.time()
        curr12= round(curr2-curr1)

        #print(u*a)
        #print(ab)
        if u*a==ab:
            sc=sc+(50//curr12)
            print(f"|Right|   answer given in {curr12} sec \t \t \t \t score:{sc}\n")
        else:
            sc=sc-(50//curr12)
            print(f"|incorrect|, it should be --({ab//a})   you took {curr12} sec \t \t \t \t score:{sc}\n")
    
    print(f"\nyour final score is: {sc} outof {au1*50}")
    







while True:
    cn=input("\n what's your name: ")
    mainmenu()
    t= input("enter name for your game? ")  
    for i in Lg:
        if i==t:
            au=input("Please select the mode you want to play in--\n ZEN-mode\n LIM-ited\n ::")
            if au=="zen":
                while True:
                    print("in ZEN mode game runs for 100 rounds")
                    au1=int("100")
                    game1()
            if au=="lim":
                try:
                    au1=int(input("how many rounds you want to play: "))
                except:
                    print("try again")
                    au1=int(input("how many rounds you want to play: "))

                game1()
    print(f"thanks for playing with us {cn} \n")




