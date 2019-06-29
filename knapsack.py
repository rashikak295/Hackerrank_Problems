def test(T, tests, out):
  global maximum_sum, output
  if len(tests)==0 or T == 0:
    if maximum_sum < len(out):
      maximum_sum = len(out)
      output = out
  elif tests[-1][1] > T:
    test(T, tests[0:-1], out)
  else:
    test(T, tests[0:-1], out)
    test(T-tests[-1][1], tests[0:-1], out+[tests[-1][0]])


maximum_sum = 0
output = []
tests = [(40,5),(50,15),(60,10),(100,20),(120,30)]
T = 50
test(T, tests, [])
print(output)