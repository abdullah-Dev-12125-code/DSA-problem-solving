def merge_sort(arr): 
    if len(arr) <= 1: #If length of array is 1 or less then that it will return the same array
        return arr
    
    mid = len(arr)//2 #Finding mid
    left_half = arr[:mid] #Left portion 
    right_half = arr[mid:] #right portion
    left_half = merge_sort(left_half) #Recursion method to break elements of left half
    right_half = merge_sort(right_half) #Recursion method to break elements of right half
    
    return merge(left_half,right_half) #Passing arguments to sort array 

def merge(left,right):
    new = [] #New array where all sorted elements stores
    i,j = 0,0 #new pointers 

    while i < len(left) and j < len(right): #Loop runs while both halves have elements to compare
        if left[i] < right[j]: #If left element is smaller
            new.append(left[i]) #Add left element
            i += 1 #Move left pointer
       
        else: #If right element is smaller or equal
            new.append(right[j]) #Add right element
            j += 1 #Move right pointer

    new.extend(left[i:]) #Add remaining left elements if there are any 
    new.extend(right[j:]) #Add remaining right elements if there are any 
    return new #Return fully merged sorted array

arr = [1,2,34,6,2,7,9,2] #Original array
print(merge_sort(arr)) #Print sorted array result