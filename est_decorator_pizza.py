# Decorator all decorator PizzaShop py


class EatComponent:  #Componente
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class Plate(EatComponent):  #ComponenteConcreto
    cost = 10

class Decorator(EatComponent): #Decorador
    def __init__(self, eatComponent):
        self.component = eatComponent
    
    def getTotalCost(self):
        return self.component.getTotalCost() + EatComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + EatComponent.getDescription(self)

class Chocolate(Decorator): #DecoradorConcretoA
    cost = 15
    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)

class Bacon(Decorator): #DecoradorConcretoB
    cost = 15
    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)

class Pepperoni(Decorator): #DecoradorConcretoC
    cost = 18
    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)

class Margherita(Decorator): #DecoradorConcretoD
    cost = 15
    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)

class Hawaiian(Decorator): #DecoradorConcretoE
    cost = 15
    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)

class Portuguesa(Decorator): #DecoradorConcretoF
    cost = 15
    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)

class Banana(Decorator): #DecoradorConcretoA
    cost = 2
    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)


maravilhoso = Bacon(Pepperoni(Plate()))
print(maravilhoso.getDescription() + ": $" + str(maravilhoso.getTotalCost()))
sobremesa = Chocolate(Banana(Plate()))
print(sobremesa.getDescription() + ": $" + str(sobremesa.getTotalCost()))
