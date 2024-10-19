def binarySearch(array,x):
    begin_index = 0
    end_index = len(array)-1    
    
    while begin_index <= end_index:  
        midpoint = begin_index+(end_index-begin_index)//2      
        midpoint_value = array[midpoint]
        if  midpoint_value == x :
            return midpoint
        elif x > midpoint_value:
            begin_index=midpoint+1
        else:
            end_index=midpoint-1

        
    return -1
    

sequence= [1,4,6,9,23,35,46,51,73]
no_= 51

print(binarySearch(sequence,no_))

