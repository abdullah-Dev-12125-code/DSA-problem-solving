array = [1,2,3,4,5] #Its an array 

k = 2 #The value provided from where we have to rotate

value = k % len(array) #As described here I am using modulas operator to handle large values

rotation = array[-k:] + array[:-k] #Here is the real part where i actually rotate I simply sepreated array from the obtained value in two parts then I merged them back 

print(rotation) 