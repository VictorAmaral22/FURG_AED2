def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def nextPrime(num):
    while not isPrime(num):
        num += 1
        
    return num

class TabelaHash:
    def __init__ (self, max):
        next = nextPrime(max)
        self.keys = [None] * next
        self.values = [None] * next
        self.max = next
        self.tamanho = 0

    def hash (self, key): # truncamento
        return key % self.max
    
    def insert (self, key, value):
        pos = self.hash(key)
        print("pos",pos)
        self.keys[pos] = key
        self.values[pos] = value

    def list (self):
        return { "keys": self.keys, "values": self.values }
    
    def searchSequential (self, key):
        return key
    
    def searchBinary (self, key):
        return key
    
    def searchByKey (self, key):
        return key
    
table = TabelaHash(10)
table.insert(123456, ["aluno a"])
table.insert(111111, ["aluno b"])
table.insert(111110, ["aluno c"])

print(table.list())