def selectionSort (array):
    for i in range(len(array)):
        smallest = i
        for j in range(i+1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        tmp = array[i]
        array[i] = array[smallest]
        array[smallest] = tmp

    return array

print(selectionSort([9,2,7,1,0,10]))

