def exchange (value: int):
    coins = [100, 25, 10, 5, 1]
    solution = []
    sum = 0

    i = 0
    while sum != value:
        x = None

        for j in coins:
            if j + sum <= value:
                x = j
                break

        if x is None:
            return "no solution found"
        else:
            solution.append(x)
            sum += x
    
    return solution

print(exchange(89))
    