import random
import time

print("Hello welcome to my snakes and ladders game")
print("You are required to have somebody to play with you,\nIf there is nobody to play with you, just leave now")
print("Please enter your names for a more immersive experience")
print("Thank you for joining in, I appriciate it")
player_1=str(input("Please enter the name of the first player"))
player_2=str(input("Please enter the name of the second player"))
print("The game will be played between",player_1,"and",player_2)
ladder_climbed=["Woohoo a ladder climbed","Congratulations you've climbed a ladder","Nice you climbed a ladder","Lucky you, climbed a ladder"]
snake_bite=["Oh no a snake bite","Shit you have been bitten by a snake","Unlucky you, a snake has bitten you"]
winning_val=100
time_between_actions=1
pos_1=0
pos_2=0
while pos_1<=winning_val:
    print(player_1,"'s turn")
    b=random.randint(1,6)
    input("Press Enter to roll dice")
    print("Rolling.....")
    time.sleep(1)
    if pos_1>100:
            print("Too high value,try again until you reach exact 100")
            pos_1-=b
            print(player_1," is now on:", pos_1)
            print("___________________________________________________________________")
    elif pos_1==100:
            print("-----------------------",player_1, "wins, Congratulations-----------------------")
            break
    if b==6:
            print("It is a :", b)
            print("Woohoo you rolled a 6, you get another roll")
            pos_1+=b
            print(player_1,"is now on:", pos_1)
            print("___________________________________________________________________")
            continue
    print("It is a :",b)
    pos_1=pos_1+b
    if pos_1>100:
            print("Too high value,try again until you reach exact 100")
            pos_1-=b
            print(player_1," is now on:", pos_1)
            print("___________________________________________________________________")
    elif pos_1==100:
            print("-----------------------",player_1, "wins, Congratulations-----------------------")
            break
    else:
            print(player_1,"is now on:",pos_1)
            print("___________________________________________________________________")
    if pos_1==2:
                pos_1=18
                print(random.choice(ladder_climbed))
                print(player_1,"has now moved to :",pos_1)
                print("___________________________________________________________________")
    elif pos_1==9:
                pos_1=28
                print(random.choice(ladder_climbed))
                print(player_1, "has now moved to :", pos_1)
                print("___________________________________________________________________")
    elif pos_1==11:
                pos_1=31
                print(random.choice(ladder_climbed))
                print(player_1, "has now moved to :", pos_1)
                print("___________________________________________________________________")
    elif pos_1==17:
                pos_1=96
                print(random.choice(ladder_climbed))
                print(player_1, "has now moved to :", pos_1)
                print("___________________________________________________________________")
    elif pos_1==26:
                pos_1=54
                print(random.choice(snake_bite))
                print(player_1, "has now moved to :", pos_1)
                print("___________________________________________________________________")
    elif pos_1==27:
                pos_1=15
                print(random.choice(snake_bite))
                print(player_1, "has now moved to :", pos_1)
                print("___________________________________________________________________")
    elif pos_1==40:
                pos_1=80
                print(random.choice(ladder_climbed))
                print(player_1, "has now moved to :", pos_1)
                print("___________________________________________________________________")
    elif pos_1==48:
                pos_1=29
                print(random.choice(snake_bite))
                print(player_1, "has now moved to :", pos_1)
                print("___________________________________________________________________")
    elif pos_1==61:
                pos_1=22
                print(random.choice(snake_bite))
                print(player_1,"has now moved to :",pos_1)
                print("___________________________________________________________________")
    elif pos_1==70:
                pos_1=88
                print(random.choice(ladder_climbed))
                print(player_1,"has now moved to :",pos_1)
                print("___________________________________________________________________")
    elif pos_1==77:
                pos_1=98
                print(random.choice(ladder_climbed))
                print(player_1,"has now moved to :",pos_1)
                print("___________________________________________________________________")
    elif pos_1==86:
                pos_1=55
                print(random.choice(snake_bite))
                print(player_1,"has now moved to :", pos_1)
                print("___________________________________________________________________")
    elif pos_1==92:
                pos_1=75
                print(random.choice(snake_bite))
                print(player_1,"has now moved to :",pos_1)
                print("___________________________________________________________________")
    elif pos_1==99:
                pos_1=5
                print(random.choice(snake_bite))
                print(player_1,"has now moved to :",pos_1)
                print("___________________________________________________________________")
                pass
    print(player_2, "'s turn")
    b = random.randint(1, 6)
    input("Press Enter to roll dice")
    print("Rolling.....")
    time.sleep(1)
    if pos_2 > 100:
        print("Too high value,try again until you reach exact 100")
        pos_2 -= b
        print(player_2, " is now on:", pos_2)
        print("___________________________________________________________________")
    elif pos_2 == 100:
        print("-----------------------", player_2, "wins, Congratulations-----------------------")
        break
    if b == 6:
        print("It is a :", b)
        print("Woohoo you rolled a 6, you get another roll")
        pos_2 += b
        print(player_2, "is now on:", pos_2)
        print("___________________________________________________________________")
        continue
    print("It is a :", b)
    pos_2 = pos_2 + b
    if pos_2 > 100:
        print("Too high value,try again until you reach exact 100")
        pos_2 -= b
        print(player_2, " is now on:", pos_2)
        print("___________________________________________________________________")
    elif pos_2 == 100:
        print("-----------------------", player_2, "wins, Congratulations-----------------------")
        break
    else:
        print(player_2, "is now on:", pos_2)
        print("___________________________________________________________________")
        if pos_2==2:
                pos_2 = 18
                print(random.choice(ladder_climbed))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==9:
                pos_2 = 28
                print(random.choice(ladder_climbed))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==11:
                pos_2 = 31
                print(random.choice(ladder_climbed))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==17:
                pos_2 = 96
                print(random.choice(ladder_climbed))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2 == 26:
                pos_2 = 54
                print(random.choice(snake_bite))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==27:
                pos_2 = 15
                print(random.choice(snake_bite))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==40:
                pos_2 = 80
                print(random.choice(ladder_climbed))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==48:
                pos_2 = 29
                print(random.choice(snake_bite))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==61:
                pos_2 = 22
                print(random.choice(snake_bite))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==70:
                pos_2 = 88
                print(random.choice(ladder_climbed))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==77:
                pos_2 = 98
                print(random.choice(ladder_climbed))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==86:
                pos_2 = 55
                print(random.choice(snake_bite))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==92:
                pos_2 = 75
                print(random.choice(snake_bite))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")
        elif pos_2==99:
                pos_2 = 5
                print(random.choice(snake_bite))
                print(player_2,"has now moved to :", pos_2)
                print("___________________________________________________________________")

        else:
            continue


print("Thank you for playing my game")
print("Developed with dedication by Shivom")





























