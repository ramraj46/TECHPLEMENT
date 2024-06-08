import string
import random
def password_generator(length,lc,uc,d,c):
    if lc==1:
        lower_char=string.ascii_lowercase
    else:
        lower_char=''
    if uc==1:
        upper_char=string.ascii_uppercase
    else:
        upper_char=''
    if d==1:
        digits = string.digits
    else:
        digits=''
    if c==1:
        char = "!~@#$%&*(?<"
    else:
        char=''
    password=lower_char+upper_char+digits+char
    Password = ''.join(random.choice(password) for _ in range(length))
    print("The Randomly Generated Password is : ",end='')
    return Password
length = int(input("Length of the Password : "))
lc=int(input('Press "1" for lowercase letters : '))
uc=int(input('Press "1" for upppecase letters : '))
d=int(input('Press "1" for digits : '))
c=int(input('Press "1" for special characters : '))
print(password_generator(length,lc,uc,d,c))
