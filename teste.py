def calculo_nota_fiscal(indice=None):
        if indice:
            perc = indice * 0.02
            return int(indice + perc)
        else:
            print('Valor de indice não informado')

def calculo_debito(indice=None):
    if indice:
        perc = indice * 0.04
        valor_final = indice - perc
        return valor_final
valor = calculo_nota_fiscal(55)
valor_debito = calculo_debito(53)
print(valor)
print(valor_debito)