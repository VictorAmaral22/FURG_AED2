def exchange (value: int):
    coins = [100, 10, 25, 5, 1]
    solution = []
    sum = 0

    i = 0
    while sum != value:
        x = None

        for j in coins:
            if j + sum <= value and (x is None or (x is not None and j > x)):
                x = j

        if x is None:
            return "no solution found"
        else:
            solution.append(x)
            sum += x
    
    return solution

print(exchange(89))
    