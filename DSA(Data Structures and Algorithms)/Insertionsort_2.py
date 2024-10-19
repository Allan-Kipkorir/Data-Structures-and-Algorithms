#selectionsort Issue solved

def insertionSort(array):
    for i in range(1,len(array)):
        for j in range(i-1,-1,-1):
            if array[j]>array[i]:
                array[i], array[j] = array[j], array[i]
                print(array)
    return array



print(insertionSort([8,3,4,0,6,87,78,78,9]))