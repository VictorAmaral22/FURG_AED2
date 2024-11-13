class Nodo:
    def __init__(self, chave, info, esq=None, dir=None):
        self.esq = esq
        self.dir = dir
        self.chave = chave
        self.info = info

    def inserir (self, chave, valor):
        if chave < self.chave:
            if self.esq == None:
                self.esq = Nodo(chave, valor)
                return chave
            else:
                self.esq.inserir(chave, valor)
        elif chave > self.chave:
            if self.dir == None:
                self.dir = Nodo(chave, valor)
                return chave
            else:
                self.dir.inserir(chave, valor)
        else:
            return None
            
    def buscar (self, chave):
        if chave == self.chave and self != None:
            return self
        elif chave < self.chave and self.esq != None:
            return self.esq.buscar(chave)
        elif chave > self.chave and self.dir != None:
            return self.dir.buscar(chave)
        else:
            return None
        
    def buscarPai (self, chave):
        if self != None and (chave == self.esq.chave or chave == self.dir.chave):
            return self
        elif chave < self.chave and self.esq != None:
            return self.esq.buscar(chave)
        elif chave > self.chave and self.dir != None:
            return self.dir.buscar(chave)
        else:
            return None
        
    def removerFolha (self, chave):
        if self.esq and self.esq.esq is None and self.esq.dir is None and self.esq.chave == chave:
            self.esq = None
            return True
        if self.dir and self.dir.esq is None and self.dir.dir is None and self.dir.chave == chave:
            self.dir = None
            return True
        if self.chave > chave and self.esq:
            return self.esq.removerFolha(chave)
        if self.chave < chave and self.dir:
            return self.dir.removerFolha(chave)
        
        return False

    def remover1Sub (self, chave):
        if self.esq and self.esq.esq is None and self.esq.dir is None and self.esq.chave == chave:
            self.esq = None
            return True
        if self.dir and self.dir.esq is None and self.dir.dir is None and self.dir.chave == chave:
            self.dir = None
            return True
        if self.chave > chave and self.esq:
            return self.esq.removerFolha(chave)
        if self.chave < chave and self.dir:
            return self.dir.removerFolha(chave)
        
        return False
        
    

arv = Nodo(500, "A")
arv.inserir(300, "B")
arv.inserir(800, "C")
arv.inserir(150, "D")
arv.inserir(400, "E")
arv.inserir(600, "F")
arv.inserir(550, "G")
arv.inserir(650, "H")
arv.inserir(900, "I")

print(arv.buscar(550))
print(arv.removerFolha(900))