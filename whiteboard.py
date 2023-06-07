# Consecutive Indices
# You are given a list of unique integers (arr), and two integers (a and b). 
# Your task is to find out whether or not a and b appear consecutively in arr, 
# and return a boolean value (True if a and b are consecutive, False otherwise).
# It is guaranteed that a and b are both present in arr. You must do this without
# using the .index() method

# Example:
# Input: ([1, 6, 9, -3, 4, -78, 0], -3, 4)
# Output: True
# Input: ([3,1,0,19], 19, 0)	
# Output: True

# for loop to cycle through the integers
# if statement that determines if the index of the value of a 
#            is equal to the index + 1 of the value of b       

def consecutive(arr, a , b):
    for i in range(len(arr)):
        if arr[i] == a or arr[i] == b:
            if arr[i + 1] == a or arr[i + 1] == b:
                return True
            else:
                return False

print(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4))


