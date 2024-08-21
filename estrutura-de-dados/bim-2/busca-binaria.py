lista = [1, 3, 40, 55, 67, 91, 244, 505]

def buscaBinaria (lista, valor, ini=0, fim=len(lista)-1, tam=len(lista)):
    print(lista, valor, ini, fim, tam)
    if fim < ini or tam == 0:
        return -1
    
    if lista[tam//2] == valor:
        return tam//2
    else:
        # Compara se o valor é maior que o primeiro valor da segunda metade do vetor total
        if valor > lista[tam//2]:
            # A metade da direita é do começo até a metade do vetor total
            newList = lista[slice(tam//2, tam)]
            pos = buscaBinaria(newList, valor, ini, len(newList)-1, len(newList))
            print("right", pos)
            return tam//2 + pos
        
        # Compara se o valor é menor que o último valor da primeira metade
        if valor < lista[tam//2-1]:
            # A metade da esquerda é do começo até a metade do vetor total
            newList = lista[slice(ini, tam//2-1)]
            pos = buscaBinaria(newList, valor, ini, len(newList)-1, len(newList))
            print("left", pos)
            return ini + pos
    

        


print(buscaBinaria(lista, 1))