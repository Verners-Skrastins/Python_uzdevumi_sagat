"""
Kas jāraksta aiz "=" zīmes, lai iegūtu informāciju par objekta pilsētu?
"""


class DATI:


    def __init__(self, nosaukums, pilseta):
        self.nosaukums = nosaukums
        self.pilseta = pilseta
        
        
        
pirmais_ieraksts =DATI("klase203", "USA")
pilsetas_info = pirmais_ieraksts.pilseta
print(pilsetas_info)

