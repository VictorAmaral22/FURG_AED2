class Nodo ():
    def __init__ (self, valor):
        self.info = valor
        self.prox = None

class Pilha:
    def __init__ (self):
        self.topo = None

    def inserir (self, valor):
        aux = Nodo(valor)
        aux.prox = self.topo
        self.topo = aux

    def consultar (self):
        if self.topo != None:
            return self.topo
        else:
            return None

    def remover (self):
        if self.topo != None:
            top = self.topo
            self.topo = self.topo.prox
            return top
        else:
            return False
        

