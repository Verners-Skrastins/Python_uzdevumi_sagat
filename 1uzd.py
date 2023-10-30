"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

"""
class RomiesuCipars:
    def __init__(self):
        self.rom_cip = {
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"

        }
    def uzRomiesu(self, num):
        result = ""
        for value, sk in sorted(self.rom_cip.items(), key = lambda x:x[0], reverse=True):
            while num>=value:
                result+=sk
                num-=value
        return result


skaitlis = 654
klase = RomiesuCipars()
romu_sks = klase.uzRomiesu(skaitlis)   
print(romu_sks)     
