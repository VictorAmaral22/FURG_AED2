weights = [1, 2, 5,  6,  7]
values =  [1, 6, 18, 22, 28]
W = 11
n = 6
x = [0] * n

def backpack (i, r):
    best = 0
    for k in range(i, n):
        if weights[k-1] <= r and x[k-1] != 1:
            x[k-1] = 1
            best = max(best, values[k-1] + backpack(k, r-weights[k-1]))
            x[k-1] = 0
    return best

print(backpack(1, W)) # 40