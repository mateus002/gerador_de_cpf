from random import randint
from time import sleep

def calcular_digito(cpf, multiplicador):
    
    soma = sum(a * b for a,b in zip(cpf, multiplicador)) % 11

    if soma < 2:
        return 0
    
    return 11 - soma

def numeros():
    return [randint(0,9) for _ in range(9)]

while(True):
    cpff = numeros()

    cpff.append(calcular_digito(cpff, range(10, 1, -1)))
    cpff.append(calcular_digito(cpff, range(11, 1, -1)))



    cpf = "".join(map(str, cpff))
    novo_cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    print(novo_cpf)
    sleep(1.0)