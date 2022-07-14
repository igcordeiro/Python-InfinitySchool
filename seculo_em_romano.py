
#Código para calcular o seculo, por Igor Cordeiro - AKA igcordeiro

ano = int(input("DIGITE O VALOR DO ANO:\n"))
def sec (ano):
    calc=(ano+99)/100
    seculo=int(str(calc)[:2])
    
    return  seculo


def int_to_Roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

seculo=sec(ano)
print ('O seculo para o ano informado era o século:') 
print(seculo)
romano=int_to_Roman(seculo)
print (f'O seculo {seculo} em romano é {romano}:') 
print(romano)
