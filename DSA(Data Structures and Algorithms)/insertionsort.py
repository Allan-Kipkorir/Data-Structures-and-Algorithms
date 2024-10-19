def insertionsort(array):
    #we will create a loop that starts with the second item in the array,
    # next create a variable j that is equal to 1 which is the first element in the array
    # create a while loop to swap the elements in the array if the previous element is greater than the current element(element on the right)
    #why do we decrease the element j?
    for i in range(1,len(array)):
        j = i
        while array[j-1] > array[j] and j > 0:
            array[j],array[j-1] = array[j-1], array[j]
            j-=1

    return print (array)


x = [23,28,3,25,97,35,64,52,19]
insertionsort(x)