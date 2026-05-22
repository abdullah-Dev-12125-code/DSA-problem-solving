array = [1, 2, 2, 3, 4, 4, 5] #array

for i in range(len(array) - 1, 0, -1):#I first tried a normal forward loop but it was not working So I tried to understand the cause I found that the forward loop itself is fine but the problem happens when values are removed Removing elements changes the indexes of the remaining elements which causes index shifting issues and causes program to behave abnormaly
    j = i - 1

    if j >= 0 and array[j] == array[i]: # The concept is driven from insertion sort Here i just compared values of I and J and removed the duplicate while maintaining value of j
        array.remove(array[i])  #Just removed values

print(array)
