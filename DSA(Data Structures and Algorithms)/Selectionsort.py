#there are 2 variations an efficient one and a less efficient one that utilizess

#first variation
def selectionsort_1(unsorted):
    sorted = []
    min_ = float("inf")
    while len(unsorted)>1:
        for i in unsorted:
            if i< min_:
                min_ = i
        sorted.append(min_)
        unsorted.remove(min_)
    return sorted


selectionsort_1([2,5,1,9,2,6,7,8])
        