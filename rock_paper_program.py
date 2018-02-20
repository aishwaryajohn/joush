#rock_paper_program 
import random
l=["rock","paper","scissor",]
i=input("press s to start the game ")
while(i=="s"):
    a=input("choose R for rock,P for paper,S for scissor")
    b=random.choice(l)
    if a=="R":
        if b==l[0]:
            print("computer chose",b)
            print("user chose",a)
            print("its a tie")
        elif b==l[1]:
            print("computer chose",b)
            print("user chose ",a)
            print("computer wins")
        elif b==l[2]:
            print("computer chose",b)
            print("user chose",a)
            print("user wins")
    if a=="P":   
        if b==l[1]:
            print("computer chose",b)
            print("user chose",a)
            print("its a tie")
        elif b==l[2]:
            print("computer chose",b)
            print("user chose",a)
            print("computer wins")
        elif b==l[0]:
            print("computer chose",b)
            print("user chose",a)
            print("user wins")
    if a=="S":        
        if b==l[2]:
            print("computer chose",b)
            print("user chose",a)
            print("its a tie")
        elif b==l[1]:
            print("computer chose",b)
            print("user chose",a)
            print("user wins")
        elif b==l[0]:
            print("computer chose",b)
            print("user chose",a)
            print("computer wins")
    else:
        print("please choose")
    c=input("press q to quit and p to play")
    if c=="q":
        print("thank you")
        break
    elif c=="p":
        print("continue the  game")
            
