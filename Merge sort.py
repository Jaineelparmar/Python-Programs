# Implement merge sort algorithm using python.

def mergesort(li):
    if len(li) > 1:
        mid = len(li)//2    #Finding the mid of the array
        left = li[:mid]     #Dividing the array elements  
        right = li[mid:]    #into 2 halves 
        
        mergesort(left)     # Sorting the first half 
        mergesort(right)    # Sorting the second half
        
        i = 0
        j = 0
        k = 0
        
         # Copy data to temp arrays L[] and R[] 
        while i < len(left) and j < len (right):
            if left[i] <= right[j]:
                li[k] = left[i]
                i = i+1 
                k = k+1 
            else:
                li[k] = right[j]
                j = j+1 
                k = k+1 

        # Checking if any element was left 
        while i < len(left):
            li[k] = left[i]
            i = i+1 
            k = k+1 
            
        while j < len(right):
            li[k] = right[j]
            j = j+1 
            k = k+1 
            
x = [90, 50, 60, 30, 40,  80,  70, 10, 20, 100]
mergesort(x)
print(x)