import random

def stupidPassword(n: int, l: int):
    alphabetLowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    passwords = []
    for d1 in range(1,n+1):
        for d2 in range(1,n+1):
            for c1 in range(l):
                for c2 in range(l):
                    for d3 in range(1, n + 1):
                        if d3 > d1 and d3 > d2:
                            password = (str(d1)+str(d2)+alphabetLowercase[c1]+alphabetLowercase[c2]+str(d3))
                            passwords.append(password)
    return passwords

stupidPassword(9,5)

#why you make this homework so annoying :|