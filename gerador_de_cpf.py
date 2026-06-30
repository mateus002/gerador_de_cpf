from random import randint
from time import sleep
def numero1():
    numero = randint(0,9)
    cpf = [randint(0,9) for _ in range(9)]
    multiplicadores = [x for x in range(10,1,-1)]
    novo_cpf = [a * b for a,b in zip(cpf,multiplicadores)]
    soma = sum(novo_cpf) % 11
    if soma == 0 or soma == 1:
        cpf.append(0)
    else:
        cpf.append(11-soma)
    return cpf

def numero2():
    cpf = numero1()
    multiplicadores2 = [x for x in range(11,1,-1)]
    novo_cpf2 = [a * b for a,b in zip(cpf,multiplicadores2)]
    soma2 = sum(novo_cpf2) % 11
    if soma2 == 0 or soma2 == 1:
        cpf.append(0)
    else:
        cpf.append(11-soma2)

    return cpf

while(True):
    cpf = "".join(map(str, numero2()))
    novo_cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    print(novo_cpf)
    sleep(1.0)