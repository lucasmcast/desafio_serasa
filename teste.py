def calculo_nota_fiscal(indice=None, perc=None):
        if indice and perc:
            quociente = indice / 100
            result = quociente * perc
            indice += result
            print(indice)
            return int(indice)
        else:
            print('Valor de indice não informado')

def calculo_debito(indice=None, perc=None):

    if indice and perc:
        quociente = indice / 100
        result = quociente * perc
        indice -= result
        print(indice)
        if quociente < 1:
            resto = round(indice % 1, 2)
            arredondamento = 1 - resto
            indice +=  arredondamento
            
        return int(indice)
    else:
        print('Volores não informados')

indice = 99
#valor = calculo_nota_fiscal(24 , 2)
valor_debito = calculo_debito(indice, 4)
#print(valor)
print(valor_debito)
print(indice)