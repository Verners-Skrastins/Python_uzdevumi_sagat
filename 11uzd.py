"""
Uzrakstiet Python programmu, lai trīskāršotu visus dotā veselo skaitļu saraksta skaitļus.
Izmantojiet Python map() funkciju.
"""

skaitli = [5,6,7,8,9,10]
def reiztris(a):
    return a * 3
skaitlirez = list(map(reiztris, skaitli))
print(skaitlirez)