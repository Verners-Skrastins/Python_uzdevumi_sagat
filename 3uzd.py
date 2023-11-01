"""
Uzrakstiet programmu, izveidot klasi ar nosaukumu
Dati. Izveidot objektu, kas inicializētu atribūtus, 
piemēram, vārdu, vecumu un ceļojumam iemaksāto summu.

"""
class Dati:
    def __init__(self, vards, vecums, summa):
        self.vards = vards
        self.vecums = vecums
        self.summa = summa

cilveks = Dati('Verners',18,1000)
