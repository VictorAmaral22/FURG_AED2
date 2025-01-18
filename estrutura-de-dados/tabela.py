# 1. todas as operações básicas do TAD Tabela por contiguidade física;
# 2. uma nova operação de inserção ordenada e o algoritmo de busca binária;
# 3. um programa que importe a classe e teste todos os métodos. 

class Tabela:
    def __init__ (self, max):
        self.keys = [None] * max
        self.values = [None] * max
        self.max = max
        self.tamanho = 0

    def posicao (self, key):
        pos = 0
        while (pos < self.tamanho):
            if self.keys[pos] == key:
                return pos
            pos += 1
        return None
    
    def valor (self, key):
        pos = self.posicao(key)
        if pos != None:
            return self.values[pos]
        else:
            return None

    def inserir (self, key, values):
        if key == None:
            return None
        
        pos = self.posicao(key)
        if pos != None:
            self.values[pos] = values
        else:
            if self.tamanho < self.max:
                self.keys[self.tamanho] = key
                self.values[self.tamanho] = values
                self.tamanho += 1
    
    def excluir (self, key):
        pos = self.posicao(key)
        if pos != None:
            while pos < self.tamanho -1:
                self.keys[pos] = self.keys[pos+1]
                self.values[pos] = self.values[pos+1]
                pos += 1
            self.tamanho -= 1


table = Tabela(10)

table.inserir("ABC1234", ["VW", "GOL", 2010, "Anderson"])
table.inserir("ASD4321", ["FIAT", "UNO", 2001, "Maria"])
table.inserir("DFG6789", ["FIAT", "UNO", 2003, "Jorge"])
table.inserir("JKL0077", ["GM", "CELTA", 2008, "Tadeu"])
table.inserir("UTY2345", ["GM", "CORSA", 1999, "Maria"])
table.inserir("XYZ4567", ["FORD", "FOCUS", 2007, "Carlos"])

print(table.valor("UTY2345"))
table.excluir("UTY2345")
print(table.posicao("ABC1234"))