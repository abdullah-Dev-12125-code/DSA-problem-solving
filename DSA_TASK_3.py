array = [1, 2, 3, 4, 5]#array
target = 6 #target

for i in range(len(array) - 1): #It is an outer loop that loops through every item once

    for j in range(len(array)): #It is an inner loop that is used to loop through every item for the number of times outer loop runs  

        if array[i] + array[j] == target: #I add the values of i and j and if it sums up and equals the target it will be printed
            print([array[i],array[j]])