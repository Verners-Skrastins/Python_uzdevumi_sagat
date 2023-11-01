"""
Uzrakstiet Python programmu, lai diviem sarakstiem noteikti atšķirību.
Izmantojiet funkciju map().
"""

skaitli1 = [1,5,9,7,3]
skaitli2 = [4,5,6,7,8,9]
def parbaude(a,b):
    if a == b:
        print(a)
skaitli3 = list(map(parbaude,skaitli1,skaitli2))
print(skaitli3)
