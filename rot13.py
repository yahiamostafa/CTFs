'''
this code to solve Mod 26 problem

category: Cryptography

https://play.picoctf.org/practice/challenge/144?category=2&page=1


Description:

Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}

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
