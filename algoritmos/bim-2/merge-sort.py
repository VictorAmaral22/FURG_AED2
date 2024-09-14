def merge (A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    
    i = 1
    j = 1
    while i <= n1:
        L[i] = A[p + i - 1]
        i += 1
    while j <= n2:
        R[j] = A[q + j]
        j += 1
        
    L.append(float("inf"))
    R.append(float("inf"))

    i = 1
    j = 1
    k = p
    while k <= r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

def merge_sort (A, p, r):
    if p < r:
        q = (p + r)//2 # divisão
        merge_sort(A, p, q) # conquista
        merge_sort(A, q + 1, r) # conquista
        merge(A, p, q, r) # combina
        return A
        
A = [None, 255,9,1,6,87,23,2,32]
print(merge_sort(A, 1, len(A)-1)) # [None, 1,2,2,3,4,5,6,7]