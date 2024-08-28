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
            aux = Nodo(valor)
            self.inicio = aux
        else:
            while (aux != None):
                if aux.prox == None:
                    aux.prox = Nodo(valor)
                    return True
                aux = aux.prox
        
    def listarTudo (self):
        arr = []
        elem = self.inicio
        
        while elem != None:
            arr.append(elem.info)
            elem = elem.prox

        print(arr)
   
    def buscaRec (self, valor, count=0):
        if self.inicio:
            if self.inicio.info == valor:
                return count
            else:
                tmpList = self
                tmpList.inicio = tmpList.inicio.prox
                count = tmpList.buscaRec(valor, count + 1)
                return count
        else:
            return -1

lista = ListaEnc()

lista.insert("A")
lista.insert("B")
lista.insert("C")
lista.insert("D")
lista.insert("E")

lista.listarTudo()
print(lista.buscaRec("J"))