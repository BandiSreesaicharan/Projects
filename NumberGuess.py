import random as r

def BestScore(attempt,best):
    if attempt < best :
        best=attempt
    print('Best Score: ',best)

print('Welcome to Guess The Number Game\n(only 10 attempts are given)')
play=0
while True :
    play+=1
    print('----------------------------\nRound ',play)
    number=r.randint(1,100)
    print(number)
    print(f'Minimum Value for Guess: {r.randint(1,number-1)}\nMaximum Value for guess: {r.randint(number+1,100)}')
    attempt=0
    while True :
        attempt+=1
        print('Attempt:',attempt)
        if attempt == 11 :
            print("Wrong Guess: Attempts Used 10\nCorrect Guess is ",number)
            break
        guess_number=int(input("Guess The Number (between 1 and 100): "))
        if number > guess_number :
            print('Too Low! Try again.')
        elif number < guess_number:
            print('Too high! Try again.')
        else :
            print('_Well Done_')
            if play == 1 :
                best=attempt
            BestScore(attempt,best)
            break
    print('To exit type any alphabet() ')