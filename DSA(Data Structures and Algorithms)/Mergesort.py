
# create a recursive function and run it and then create a function to merge your arrays


def merge(a,b):
    # " ' This takes in two sorted arrays :'"
    # "'merges them into two sorted arrays'"
    res = []
    while len(a) >0 and len(b) > 0:
        if a[0] < b[0]:
            res.append(a[0])
            a=a[1:]
        else:
            res.append(b[0])
            b=b[1:]

    if len(b)>0:
        res.extend(b)
    if len(a)>0:
       res.extend(a)

    return res
    

# this is a recursive function that divides the array until only one element is left in one array




def mergesort(unsorted):
    if len(unsorted)<=1:
        return unsorted
        
    midpoint = len(unsorted)//2
    left = mergesort(unsorted[:midpoint])
    right = mergesort(unsorted[midpoint:])
    return merge(left,right)


unsorted = [3,98,23,44,73,25,98,65,53]
print(mergesort(unsorted))
