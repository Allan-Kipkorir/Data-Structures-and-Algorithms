##custom sorting approach
##I am not sure which type of sort this is?
def insertionSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1,0,-1):
            if arr[j]>arr[j-1] and j!=0:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

print(insertionSort([9,3,2,6,5,1,0]))