import string as s
checker=[s.ascii_letters+s.digits+s.punctuation]
while True:
    digit=low_letter=up_letter=punc=0  
    password=input("Enter Password: ")
    for i in password:
        if i in s.digits:
            digit=1
        if i in s.ascii_lowercase:
            low_letter=1
        if i in s.ascii_uppercase:
            up_letter=1
        if i in s.punctuation:
            punc=1
    if (digit and low_letter and up_letter and punc) == 1:
        print("Strong")
    

