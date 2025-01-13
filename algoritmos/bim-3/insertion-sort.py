def insertionSort (array):
    for i in range(1, len(array)):
        print("array[i] ", i, array[i])
        key = array[i]
        j = i - 1
        while j >= 0:
            if array[j] > key:
                array[j + 1] = array[j]
            j -= 1
        array[j+1] = key

    return array

print(insertionSort([9,2,7,1,0,10]))