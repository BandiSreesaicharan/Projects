import random as r
import sys as s

while True:
    length=int(input("Enter Length of the Number: "))
    num="".join(r.choices('0123456789',k=length))
    print(f"I have Generated a {length} digit number. Try to Guess it!\t{num}")
    while True:
        guess_count=bull=cow=0
        guess=input("Guess: ")
        for i in range(length):
            guess_count+=1
            num_count=0
            if guess[i] in num:
                cow+=1
            for j in range(length):
                num_count+=1
                if guess[i] == num[j] :
                    if guess_count == num_count:
                        bull+=1

                    print("\t",num_count,guess_count)

        print(f'Bull: {bull} , Cow: {cow}')
        if bull == cow:
            print("Your Guess is Correct!")
            choice=input("Do you want to Continue? (y/n): ").lower()
            if choice == 'y':
                break
            else:
                s.exit()