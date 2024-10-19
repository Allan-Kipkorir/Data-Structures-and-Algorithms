def insertionsort(array,x):
    for i in range(len(array)):
        if x == array[i]:
            return i
        
print(insertionsort([23,32,34,12,34,89,34],12))