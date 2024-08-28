class ListaCont:
    def __init__ (self, max):
        self.max = max
        self.inicio = None
        self.fim = None
        self.vetor = [None]*max
        self.tam = 0

    def buscaLinear (self, valor):
        index = self.inicio
        fim = self.fim
        cont = 0
        
        while index <= fim:
            if self.vetor[index] == valor:
                return cont
            index += 1
            cont += 1

        return -1
    
    def posicao (self, pos):
        if pos >= 0 and pos <= (self.tam-self.inicio+1):
            if (self.inicio+pos <= self.fim):
                return self.vetor[self.inicio+pos]
            else:
                return False
        else:
            return False
