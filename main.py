#Simulador de dado

import random

class SimuladorDeDado():
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim':
                self.GerarValorDoDado()
            elif resposta == 'não':
                print('Fim execução')
            else:
                print('Digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()