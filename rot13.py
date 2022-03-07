'''
this code to solve Mod 26 problem

category: Cryptography

https://play.picoctf.org/practice/challenge/144?category=2&page=1

'''

code = input()

res = ""

for c in code:
    if c.islower():
        newC = chr((ord(c) + 13 - ord('a')) % 26 + ord('a'))
        res+=newC
    elif c.isupper():
        newC = chr((ord(c) + 13 - ord('A')) % 26 + ord('A'))
        res+=newC
    else:
        res+=c
print(res)
