import random as r
import sys as s

def scoreboard(player,count):
    for i in player:
        count+=1
        if len(player) == count :
            print(f"Player {count}: {i}",end="\n--------------------------------\n")
        else :
            print(f"Player {count}: {i}",end=" , ")

target=int(input("Enter Target_Score: "))
player=[]
num=int(input("Enter Number of Players: "))
last_dice=0
for i in range(num):
    player.append(0)

while True:
    for i in range(num):
        play=0
        while True :
            count=0
            print(f"Player {i+1}'s Turn")
            dice=r.randint(1,6)
            play=play+dice
            player[i]=player[i]+dice
            print(f"You Rolled a {dice}")
            print("\t",player)
            if dice == 1:
                player[i]=player[i]-play
                play=0
                print(f"You Scored {play} Points in this Turn")
                print("Current_Scores: ",end=' ')
                scoreboard(player,count)
                break
            elif last_dice == 6 and dice == 6 :
                player[i]=0
                print(f"'Score_RESET' for Player {i+1}")
                last_dice=0
            elif player[i] >= target :
                print(f"Player {i+1} has WON this Match")
                quit=input("Rematch? (y/n): ")
                if quit == 'y':
                    for i in range(num):
                        player[i]=0
                    break
                else:
                    s.exit()
            last_dice=dice
            choice=input("Roll again? (y/n): ")
            if choice == 'n' :
                print(f"You Scored {play} Points in this Turn")
                print("Current_Scores: ",end=' ')
                scoreboard(player,count)
                break
