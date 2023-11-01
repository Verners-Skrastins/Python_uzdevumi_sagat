"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""


saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
sarakts2=[]
for i in saraksts1:
    dakteris = f"Dr.{i}"
    sarakts2.append(dakteris)
print(sarakts2)


#map() strādā tikai sarakstā
sarakts2 = []
def funkcija(uzvards):
    return "Dr." + uzvards
sarakts2 = list(map(funkcija,saraksts1))
print(sarakts2)