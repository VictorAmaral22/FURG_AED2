class Nodo ():
    def __init__ (self, valor):
        self.info = valor
        self.prox = None

class ListaEnc:
    def __init__ (self):
        self.inicio = None
        self.tam = 0

    def insert (self, valor):
        aux = self.inicio

        if aux == None:
            aux.inicio = Nodo(valor)
        else:
            while (aux != None):
                if aux.prox == None:
                    aux.prox = Nodo(valor)
                    return True
                aux = aux.prox

    def buscaLinear (self, valor):
        aux = self.inicio
        cont = 0
        while (aux != None):
            if valor <= aux.info:
                return cont
            cont += 1
            aux = aux.prox
        return -1
    
    def posicao (self, posicao):
        aux = self.inicio
        cont = 0
        while (aux != None or cont < posicao):
            if posicao == cont:
                return aux.info
            cont += 1
            aux = aux.prox
        return -1
    
lista = ListaEnc()

# lista.insert(1)