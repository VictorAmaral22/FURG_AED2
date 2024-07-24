from filaEnc import FilaEnc, Nodo
from pilhaEnc import Pilha

def sort_fila (fila: FilaEnc):
    pilhaOrd = Pilha()
    pilhaAux = Pilha()

    elem = fila.remover()
    while elem != None:
        if pilhaOrd.topo != None:
            if pilhaOrd.topo.info >= elem.info:
                pilhaOrd.inserir(elem.info)
            else:
                while pilhaOrd.topo and pilhaOrd.topo.info < elem.info:
                    auxTop = pilhaOrd.remover()
                    pilhaAux.inserir(auxTop.info)

                pilhaOrd.inserir(elem.info)
                while pilhaAux.topo != None:
                    auxTop = pilhaAux.remover()
                    pilhaOrd.inserir(auxTop.info)
        else:
            pilhaOrd.inserir(elem.info)
        
        elem = fila.remover()

    while pilhaOrd.topo != None:
        fila.inserir(pilhaOrd.topo.info)
        pilhaOrd.remover()

    return fila


fila = FilaEnc()

fila.inserir(7)
fila.inserir(16)
fila.inserir(1)
fila.inserir(2)
fila.inserir(71)
fila.inserir(2)
fila.inserir(12)
fila.inserir(25)
fila.inserir(11)

sort_fila(fila)
fila.listarTudo()
