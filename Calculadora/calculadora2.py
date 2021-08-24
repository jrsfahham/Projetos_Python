
class Calculadora:
    def __init__(self):
        self.historico = []    

    def mostrar_historico(self):
        for operacao in self.historico:
            print(operacao[0])
            print(operacao[1])
            print()
    
    def adicao(self, *args):
        soma = 0
        operando = []

        for num in args:
            operando.append(str(num))
            soma += num

        operando = ' + '.join(operando) + ' = '
        operacao = [operando, soma]
        self.historico.append(operacao)
        return soma

    def subtracao(self, *args):
        if len(args) > 2:
            args = list(args)
            operando = [str(n) for n in args]
            diferenca = args[0]
            args.pop(0)
            for num in args:
                diferenca -= num
        else:
            operando = [str(args[0]), str(args[1])]
            diferenca = args[0] - args[1]

        operando = ' - '.join(operando) + ' = '
        operacao = [operando, diferenca]
        self.historico.append(operacao)
        return diferenca

    def multiplicacao(self, *args):
        if len(args) > 2:
            args = list(args)
            operando = [str(n) for n in args]
            produto = args[0]
            args.pop(0)
            for num in args:
                produto *= num
        else:
            operando = [str(args[0]), str(args[1])]
            produto = args[0] * args[1]

        operando = ' * '.join(operando) + ' = '
        operacao = [operando, produto]
        self.historico.append(operacao)
        return produto

    def divisao(self, *args):
        if len(args) > 2:
            args = list(args)
            operando = [str(n) for n in args]
            quociente = args[0]
            args.pop(0)
            for num in args:
                quociente /= num
        else:
            operando = [str(args[0]), str(args[1])]
            quociente = args[0] / args[1]

        operando = ' / '.join(operando) + ' = '
        operacao = [operando, quociente]
        self.historico.append(operacao)
        return quociente

if __name__ == "__main__":
    
    cal = Calculadora()
    print(cal.adicao(1, 2, 3, 4, 5))
    print(cal.subtracao(20, 5, 4, 10))
    print(cal.multiplicacao(5, 10, 6))
    print(cal.divisao(100, 5, 4))

    cal.mostrar_historico()

