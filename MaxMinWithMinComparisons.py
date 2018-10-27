#Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.

def solve(l):
  i = 0
  compcount = 0

  if len(l) % 2 == 1:
    amax, amin = l[i], l[i]
    i += 1
  else:
    amax, amin = l[i], l[1]
    compcount += 1
    if amax < amin:
      temp = amin
      amin = amax
      amax = temp
    i += 2

  while i < len(l):
    compcount += 1
    if l[i] < l[i+1]:
      currmax, currmin = l[i+1], l[i]
    else:
      currmax, currmin = l[i], l[i+1]

    compcount += 2
    amax = currmax if currmax > amax else amax
    amin = currmin if currmin < amin else amin

    i += 2

  #Test Statements
  print("Number of Comparisons: {}".format(compcount))
  print("Should be less than {} \n".format(2*(len(testl)-2)))
  print("Answer: {} and {}".format(amax, amin))
  print("Should be {} and {}".format(max(l), min(l)))

  return (amax, amin)

testl = [0,1,7,2,7,9,2,1,4,7,8,5,3,2,2,4,432,7,2,44,665,745,3]
print(solve(testl))
"""
Output from above test:

Number of Comparisons: 33
Should be less than 42 

Answer: 745 and 0
Should be 745 and 0
(745, 0)
"""
