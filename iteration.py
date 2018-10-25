def sumEvenFib(i, limit):
  ### x and y hold 2 previous Fibonacci terms, z determines next in sequence, evenSumTotal holds sum of even Fibonnaci numbers
  x = 0
  y = i
  z = 0
  evenSumTotal = 0

  ### while z, current Fibonacci number in sequence is less than limit,
  ### (limit = 4,000,000 in problem 2)
  
  while z < limit:
    z = x + y
    if z % 2 == 0:
      ### add z to evenSumTotal if z is even
      evenSumTotal += z

    ### change x and y values for next iteration
    x, y = y, z
  return evenSumTotal

print(sumEvenFib(1, 4000000))
