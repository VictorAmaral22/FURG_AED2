def merge (A, p, q, r):
    print(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    
    for i in range(n1):
        L[i] = A[p + i - 1]
    for j in range(n1):
        R[j] = A[q + j]
        
    L[n1] = float("inf")
    R[n2] = float("inf")
    
    print("L ",L)
    print("R ",R)
    
    # i = 0
    # j = 0
    
    # k = p
    # while k < r:        
    #     if L[i] <= R[j]:
    #         A[k] = L[i]
    #         i += 1
    #     else:
    #         A[k] = R[j]
    #         j += 1
             
    #     k += 1



def merge_sort (A, p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
        return A
        
A = [5,2,4,7,1,3,2,6]
print(merge_sort(A, 0, 7))