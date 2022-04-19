def array_missing(input):
  n = len(input) +1
  input_sum = sum(input)
  actual_sum  = (n * (n + 1)/ 2)
  
  return actual_sum - input_sum

input = [3, 7, 1, 2, 8, 4, 5]
test = array_missing(input)
print (test)