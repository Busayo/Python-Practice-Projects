# QUESTION
# You are given an array of positive numbers from 1 to n, 
# such that all numbers from 1 to n are present except one number x. 
# You have to find x. The input array is not sorted.

def array_missing(input):
  n = len(input) +1
  input_sum = sum(input)
  actual_sum  = (n * (n + 1)/ 2)
  return actual_sum - input_sum

# Sum of a set of numbers = (len(set) * (len(sum) +1)) / 2 
# so here we'll include the missing number in the length and use that to find what the sum of the set will be 
# Then we get the sum of the values in the current set we have and subtract that from the sum of the complete set
  

input = [3, 7, 1, 2, 8, 4, 5]
test = array_missing(input)
print (test)
