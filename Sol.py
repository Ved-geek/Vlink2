from sys import stdin
from sys import stdout

def minichar(n,s):
    digit=0
    lower=0
    upper=0
    special=0
    for i in s:
        if (i.islower()):
            lower+=1
        elif (i.isupper()):
            upper+=1
        elif (i.isdigit()):
            digit+=1
        elif i in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            special+=1

    print("Password Contains \n")
    print('Special Charachter-', special,"\n")
    print('Digits-', digit,"\n")
    print('Uppercase Alphabet-', upper,"\n")
    print('Lowercase Alphabet-', lower,"\n")

    if digit>=1 and special>=1 and upper>=1 and lower>=1 and n>=8:
        print('Strong Password: good to go!')
    elif digit>=1 and special>=1 and upper>=1 and lower>=1 and n<8:
        print(n-4, 'more charachter needed')



n=int(stdin.readline())
s=stdin.readline()
minichar(n,s)
