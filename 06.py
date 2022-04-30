
import os
os.system('cls')

def conversor_de_hora(horas, minutos):
    if horas == 24:
        horas = '00'
    elif horas > 12:
        if (horas - 12) < 10:
            horas = str(f'0{horas - 12}')
        else: 
            horas = str(horas - 12)
    if minutos < 10:
        minutos = str(f'0{minutos}')
    else:
        minutos = str(minutos)
    return str(f'{horas}:{minutos}')

def periodo(info):
    if info == 'P':
        return conversor_de_hora(horas, minutos) + ' PM'
    else: 
        return conversor_de_hora(horas, minutos) + ' AM'

sair = 'N'
while True:
    if sair == 'S':
        break
    else: 
        while True:    
            try:
                horas = int(input('Informe a hora: '))
            except ValueError:
                print('Informe apenas números inteiros de 0 até 24')
            else:
                if horas < 0:
                    print('Informe apenas números inteiros de 0 até 24')
                elif horas > 24:
                    print('Informe apenas números inteiros de 0 até 24')
                elif horas == 24:
                    info = 'A'
                    break
                elif horas > 12:
                    info = 'P'
                    break
                else: 
                    info = 'A'
                    break
        while True:
            try:
                minutos = int(input('Informe os minutos: '))
            except ValueError:
                print('Informe apenas números inteiros de 0 até 59')
            else:
                if minutos < 0:
                    print('Informe apenas números inteiros de 0 até 59')
                elif minutos > 59:
                    print('Informe apenas números inteiros de 0 até 59')
                else:
                    print('Informe apenas números inteiros de 0 até 59')
                    break
    
    print(f'{horas}:{minutos} é igual: {periodo(info)}')

    print('Caso desege finalizar o programa aperte "S"')
    sair = input('Deseja sair?')
    sair = sair.upper()
    
