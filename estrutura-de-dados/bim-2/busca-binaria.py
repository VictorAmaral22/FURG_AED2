lista = [1, 3, 40, 55, 67, 91, 244, 505]

def buscaBinaria (lista, valor, ini=0, fim=len(lista)-1, tam=len(lista)):
    if tam == 0:
        return -1
    else:
        if lista[ini] == valor:
            return ini
        elif lista[ini + tam//2] == valor:
            return ini + tam//2
        else:
            if valor > lista[ini + tam//2]:
                pos = buscaBinaria(lista, valor, ini + tam//2, ini + tam - 1, (ini + tam) - (ini + tam//2))
                return pos
            else:
                pos = buscaBinaria(lista, valor, ini, ini + tam//2 -1, (ini + tam//2 - 1) - ini + 1)
                return pos

print(buscaBinaria(lista, 1))
print(buscaBinaria(lista, 3))
print(buscaBinaria(lista, 40))
print(buscaBinaria(lista, 55))
print(buscaBinaria(lista, 67))
print(buscaBinaria(lista, 91))
print(buscaBinaria(lista, 244))
print(buscaBinaria(lista, 505))