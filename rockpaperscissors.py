import random as r

computer_score=0
user_score=0
overallcomputer_score=0
overalluser_score=0
tie_counter=0
overalltie_counter=0
round=0
while True :
    round+=1
    print('-----------------------------\nRound: ',round)
    for i in range(3) :
        user_choice=input('Rock, Paper, or Scissors? (r/p/s): ').lower()
        computer_choice=r.choice(['r','p','s'])
        if computer_choice == 'r' and user_choice == 'p' :
            print('You choose 📄\nComputer choose 🪨\n\"YOU WIN\"')
            user_score+=1
        elif computer_choice == 'p' and user_choice == 'r' :
            print('You choose 🪨\nComputer choose 📄\n\"YOU LOSE\"')
            computer_score+=1
        elif computer_choice == 's' and user_choice == 'p' :
            print('You choose 📄\nComputer choose ✂️\n\"YOU LOSE\"')
            computer_score+=1
        elif computer_choice == 'p' and user_choice == 's' :
            print('You choose ✂️\nComputer choose 📄\n\"YOU WIN\"')
            user_score+=1
        elif computer_choice == 's' and user_choice == 'r':
            print('You choose 🪨\nComputer choose ✂️\n\"YOU WIN\"')
            user_score+=1
        elif computer_choice == 'r' and user_choice == 's':
            print('You choose ✂️\nComputer choose 🪨\n"YOU LOSE\"')
            computer_score+=1
        elif user_choice not in 'rps':
            print('INVALID CHOICE')
            continue
        else :
            print("You & Computer Choose the SAME \"TIE\" ")
            tie_counter+=1
        print(i)

    print(user_score,computer_score)
    if user_score > computer_score :
        print("Game: USER WIN'S")
        overalluser_score+=1
    elif computer_score > user_score :
        print("Game: COMPUTER WIN'S")
        overallcomputer_score+=1
    else :
        print("Game: TIE")
        overalltie_counter+=1

    print('Overall User Score: ',overalluser_score)
    print('Overall Computer Score: ',overallcomputer_score)
    print('Overall Tie Counter: ',overalltie_counter)

    computer_score=0
    user_score=0

    play=input("Continue? (y/n)").lower()
    if play == 'n' :
        break