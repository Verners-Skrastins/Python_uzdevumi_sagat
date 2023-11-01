"""
Uzdevumā izmantot funkciju map(), kura  komandu izpilda 
katram saraksta(virknes) loceklim.

"""

skaitli = [5,6,7,8,9,77,88,969]
def saskaitit(a):
    return a ** a
skaitli2 = list(map(saskaitit,skaitli))
print(skaitli2)