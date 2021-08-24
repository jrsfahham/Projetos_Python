import sys
import os

def clear():
    if sys.platform.startswith('win32'):
        os.system('cls')
    elif sys.platform.startswith('linux'):
        os.system("clear")
    elif sys.platform.startswith('darwin'):
        os.system("clear")

def exibir_historico(his):
    if not his:
        print('Faça uma operação antes')
    else:
        for operacao in his:
            print(operacao)
            print()

def validar_valor(num):
    if num.isnumeric() and num.isdecimal():
        num = int(num)
    else:
        try:
            float(num)
        except ValueError:
            print('Digite um valor válido')
            return None
        else:
            num = float(num)
    return num

def inserir_valor():
    valor = input('Digite um valor: ')
    valor = validar_valor(valor)
    if not valor:
        inserir_valor()
    return valor

def escolher_operacao(n1, n2):
    clear()
    print(f'Valor 1: {n1}')
    print(f'Valor 2: {n2}')
    print('Digite a operação que deseja fazer')
    print('[1] - Adição')
    print('[2] - Subtração')
    print('[3] - Multiplicação')
    print('[4] - Divisão')
    print('[5] - Exibir histórico')
    print('[0] - Sair')
    opr = (input('>> '))
    while opr not in ['1', '2', '3', '4', '5', '0']:
        print('Digite um número válido')
        opr = (input('>> '))
    if opr == '1':
        clear()
        operacao = f'{n1} + {n2} = {n1+n2}'
        historico.append(operacao)
        print(operacao)
    elif opr == '2':
        clear()
        operacao = f'{n1} - {n2} = {n1-n2}'
        historico.append(operacao)
        print(operacao)
    elif opr == '3':
        clear()
        operacao = f'{n1} * {n2} = {n1*n2}'
        historico.append(operacao)
        print(operacao)
    elif opr == '4':
        clear()
        operacao = f'{n1} / {n2} = {n1/n2}'
        historico.append(operacao)
        print(operacao)
    elif opr == '5':
        clear()
        print('Historico')
        exibir_historico(historico)
    elif opr == '0':
        sys.exit()
    
if __name__ == '__main__':
    historico = []
    while True:
        num1 = inserir_valor()
        num2 = inserir_valor()
        escolher_operacao(num1, num2)
        print()



