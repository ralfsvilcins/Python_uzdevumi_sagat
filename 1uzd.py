"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) arabu cipari 
2) romiešu cipari
3) kas ir klase? Klase sastav no konstruktora/destruktora un metodēm(iekšējās funkcijas)
4) kādas datu strukturas zinām?
         list (saraksts) a="" - tukšs saraksts
         arry (masīvs)   a=[]
         dict (vārdnīca) {}  dict()
5) Kas ir vārdnīca? atslēga, vērtība

"""
class AAA:
    #definēju konstruktoru
    def __init__(self):
        self.roma_sk={
         1: 'I',
         4: 'IV',
         5: 'V',
         9: 'IX', 
         10: 'X', 
         40: 'XL', 
         50: 'L', 
         90: 'XC', 
         100: 'C', 
         400: 'CD', 
         500: 'D', 
         900: 'CM', 
         1000: 'M'
        }
        #TA IR METODE TA IR FUNKCIJA 
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += self.rom_dict[value]
                num -= value  #num=num-value
        return result
 
# izveidojam objektu 
kk=AAA()
skaitlis=21
# izsaycam klases iekšējo funkciju (metode)
rom_sks=kk.to_roman(skaitlis)
print(f"{skaitlis} romiešu ciparos ir {rom_sks}.")