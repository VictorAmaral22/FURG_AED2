class listItem:
    def __init__(self, data):
        self.value = data,
        self.next = None

class chainedList:
    def __init__(self):
        self.start = None
        
    def printAll (self):
        ptAux = self.start
        list = []
        while ptAux != None:
            list.append(ptAux.value)
            ptAux = ptAux.next
        print(list)
        return

    def insert (self, data):
        if self.start is None:
            self.start = listItem(data)
            return
        
        position = self.start
        while position.next:
            position = position.next

        position.next = listItem(data)
        return
    
    def insertAt (self, data, index):
        item = listItem(data)
        current = self.start
        position = 0
        if position == index:
            self.start = item
        else:
            while current != None and position+1 != index:
                position = position+1
                current = current.next
 
            if current != None:
                item.next = current.next
                current.next = item
                return
            else:
                print("Out of range index")
                return
            
    def updateAt (self, data, index):
        item = listItem(data)
        current = self.start
        position = 0
        if position == index:
            self.start = item
        else:
            prev = current
            while current != None and position != index:
                position = position+1
                prev = current
                current = current.next
 
            if current != None:
                item.next = current.next
                prev.next = item
                return
            else:
                print("Out of range index")
                return

    def removeAt (self, index):
        current = self.start
        position = 0
        if position == index:
            self.start = listItem(None)
            return
        else:
            prev = current
            while current != None and position != index:
                position = position+1
                prev = current
                current = current.next
            
            prev.next = current.next
            return
        
    def getByIndex (self, index):
        current = self.start
        position = 0
        while current != None and position != index:
            position = position+1
            current = current.next
 
        if current != None:
            print(current.value)
            return
        else:
            print("Out of range index")
            return


lista = chainedList()
lista.insert(1)
lista.insert(2)
lista.insert(5)
lista.insertAt(0, 3)
lista.removeAt(2)
lista.printAll()
lista.getByIndex(1)
lista.updateAt(6, 1)
lista.printAll()