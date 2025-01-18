class PilhaC:
    def __init__ (self, max):
        self.topo = None
        self.vetor = max*[None]
        self.max = max

    def inserir (self, valor):
        if self.topo == None:
            self.vetor[0] = valor
            self.topo = 0
            return True
        elif self.topo < self.max:
            self.vetor[self.topo+1] = valor
            self.topo += 1
            return True
        else:
            return False

    def remover (self):
        if self.topo > 0:
            self.topo -= 1
            return True
        elif self.topo == 0:
            self.topo = None
            return True
        else:
            return False
