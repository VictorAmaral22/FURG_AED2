class Nodo:
    def __init__(self, dado):
        self.esq = None
        self.info = dado
        self.dir = None

    def prefixEsq (self):
        print(self.info)

        if self.esq != None:
            self.esq.prefixEsq()

        if self.dir != None:
            self.dir.prefixEsq()

    def infixDir (self):
        if self.dir != None:
            self.dir.infixDir()
        
        print(self.info)

        if self.esq != None:
            self.esq.infixDir()

    def localizar (self, dado):
        if self.info == dado:
            return self
        else:
            pos = None
            if self.esq != None:
                pos = self.esq.localizar(dado)

            if self.dir != None and pos == None:
                pos = self.dir.localizar(dado)

            return pos
        
    def localizarPai (self, dado):
        parent = None

        if self.dir:
            if self.dir.info == dado:
                return self
            else:
                parent = self.dir.localizarPai(dado)

                if parent != None:
                    return parent
        if self.esq:
            if self.esq.info == dado:
                return self
            else:
                parent = self.dir.localizarPai(dado)

                if parent != None:
                    return parent     

        return parent   

    def inserir (self, pai, filho, lado):
        nodoPai = self.localizar(pai)

        if nodoPai != None:
            if lado == "esq":
                if nodoPai.esq == None:
                    nodoPai.esq = Nodo(filho)
                    return filho
            if lado == "dir":
                if nodoPai.dir == None:
                    nodoPai.dir = Nodo(filho)
                    return filho
        else:
            print("Error parent not found...")
            return None
                
    def excluirFolha (self, valor):
        pai = self.localizarPai(valor)

        
        
t = Nodo("A")
t.esq = Nodo("B")
t.dir = Nodo("C")
t.esq.dir = Nodo("D")

pos = t.localizar("C")

t.inserir("D", "E", "esq")
t.inserir("C", "F", "dir")
t.inserir("C", "G", "esq")

print(t.localizarPai("G").info)

t.excluir("A")

t.prefixEsq()