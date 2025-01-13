def bubbleSort (array):
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[j] < array[j-1]:
                tmp = array[j-1]
                array[j-1] = array[j]
                array[j] = tmp

    return array

print(bubbleSort([9,2,7,1,0,10]))