#snake and ladder
import random
count=0
while(count<=100):
    n=input("press r to roll on dice")
    if(n=='r'):
        r=random.randint(1,6)
        count=count+r
        print("your random is",r)
        print("your count is",count)
        if count==8:
            count=37
            print("wow! you climbmed up the ladder to 37")
        elif count==11: 
            count=2
            print("oops snake bite got down to 2")
        elif count==25:
            count=4
            print("oops snake bite got down to 4")
        elif count==38:
            count=9
            print("oops snake bite got down to 9")
        elif count==40:
            count=68
            print("wow!you climbmed up the ladder to 68")
        elif count==52:
            count=81
            print("wow!you climbmed up the ladder to 81")
        elif count==65:
            count=46
            print("oops snake bite got down to 46")
        elif count==76:
            count=97
            print("wow! you climbmed up the ladder to 97")
        elif count==89:
            count=70
            print("oops snake bite got down to 70")
        elif count>=100:
            print("win")
        else:
            print("continue the game")
