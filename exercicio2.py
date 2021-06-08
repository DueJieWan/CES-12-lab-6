from abc import ABC, abstractmethod

class Order(ABC): #Command
    
    @abstractmethod 
    def execute(self):
        pass

class Extratos(Order): #ConcreteCommand
    def __init__(self, savings):
        self.savings = savings
    
    def execute(self):
        self.savings.extratos()

class VerificarSaldos(Order):   #ConcreteCommand
    def __init__(self, saldo):
        self.saldo = saldo

    def execute(self):
        self.saldo.verificar()

class Transferencias(Order): #ConcreteCommand
    def __init__(self, valor):
        self.valor = valor

    def execute(self):
        self.valor.transferencia()

    

class Bancar: #Receiver

    def extratos(self):
        print("+10000 gold bars")

    def verificar(self):
        print("Vazio!")

    def transferencia(self):
        print("Transferiu ")

class Agent: #Invoker

    def __init__(self):
        self.__order_queue = []

    def place_order(self, order):
        selforder = order
        order.execute()

#Cliente

bank = Bancar()
verificar = VerificarSaldos(bank)
extratar = Extratos(bank)
tranferir = Transferencias(bank)

#Invoker
agent = Agent()
agent.place_order(verificar)
agent.place_order(extratar)
agent.place_order(tranferir)
