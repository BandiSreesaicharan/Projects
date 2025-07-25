import random as r
import string as s

url=[]
qrcode=set()
final={}
while True :
    text=input("Enter URL: ")
    url.append(text)
    exit=input("Continue entering url?(y/n): ").lower()
    if exit in 'n' :
        break
for i in url :
    while True :
        file="".join(r.choices(s.ascii_letters+s.digits,k=6))
        if file not in qrcode :
            qrcode.add(file)
            final[i]=file
            break

print(final)