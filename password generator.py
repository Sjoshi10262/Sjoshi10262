import random
print('welcome to my password genearator')
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialsymbol=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '\\', '|', '`', '~']
pac=int(input('how many number in letter include in your password'))
wwe=int(input())
cody=int(input())
random_=[]
for i in range(0,pac):
    random_.append(random.choice(letter))
for i in range(0,wwe):
    random_.append(random.choice(number))
for i in range(0,cody):
       random_.append(random.choice(specialsymbol))
print(random_)
random.shuffle(random_)
print(random_)
password=""
for i in random_:
    password+=i
print(password)
