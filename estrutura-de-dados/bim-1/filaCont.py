class FilaCont:
    def __init__ (self, max):
        self.max = max
        self.ini = None
        self.fim = None
        self.vetor = max*[None]

    def tamanho(self):
        if self.ini != None and self.fim != None:
            if self.ini > self.fim:
                return (self.max - self.ini + self.fim + 1)
            else:
                return self.fim - self.ini + 1
        else:
            return 0

    def inserir (self, valor):
        if self.ini == None:
            self.ini = 0
            self.fim = 0
            self.vetor[self.ini] = valor
        elif self.tamanho() < self.max:
            if self.fim == self.max -1:
                self.fim = 0
            else:
                self.fim = self.fim + 1

            self.vetor[self.fim] = valor
                

    # def consultar (self):
        
    def remover (self):
        if self.tamanho() > 0:
            self.vetor[self.ini] = None
            self.ini = self.ini + 1
            
        
fila = FilaCont(5)
fila.inserir(1)
fila.inserir(2)
fila.inserir(3)
fila.inserir(4)
fila.inserir(5)
fila.remover()
fila.remover()
fila.remover()
fila.inserir(5)
fila.inserir(6)
fila.remover()


print(f"vetor {fila.vetor}")
print(f"ini {fila.ini}")
print(f"fim {fila.fim}")
print(f"tam {fila.tamanho()}")