def merge(a,b):   
    res =[]
    while len(a)>0 and len(b)>0:
        if a[0]<b[0]:
            res.append(a[0])
            a.remove(a[0])
        else:
            res.append(b[0])
            b.remove(b[0])
    if len(a)!=0:
        res.extend(a)
    if len(b)!=0:
        res.extend(b)
    return res
def bigSorting(unsorted):
    # Write your code here
    


    if len(unsorted)<=1:
        return unsorted
    midpoint = len(unsorted)//2
    left = bigSorting(unsorted[:midpoint])
    right =bigSorting(unsorted[midpoint:])
        
    return merge(left,right)
    

    
    
