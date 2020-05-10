def calc_sum(a):
  if len(a) == 0:
    return 0
  elif len(a) == 1:
    return a[0]
  else:
    return a[0] + calc_sum(a[1:])
    
# Tests
print("The sum of 5 + 6 is: {}".format(calc_sum([5, 6])))

try:
  assert calc_sum([5, 6]) == 11
  # TBC
  
except AssertionError:
  raise AssertionError("Is your code correct?")
