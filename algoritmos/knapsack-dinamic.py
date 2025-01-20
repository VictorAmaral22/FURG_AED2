def knapsack (w, v, W):
    V = [[0 for x in range(W)] for x in range(len(v))] 

    for i in range(len(v)):
        for j in range(W):
            if i == 1 and j >= w[i]:
                V[i][j] = v[i]
            elif i == 1 and j < w[i]:
                V[i][j] = 0
            elif j < w[i]:
                V[i][j] = V[i-1][j]
            else:
                V[i][j] = max(V[i-1][j], V[i-1][j-w[i]] + v[i])    
    return V[len(v)-1][W-1]


weights = [1, 2, 5,  6,  7]
values =  [1, 6, 18, 22, 28]

print(knapsack(weights, values, 11))