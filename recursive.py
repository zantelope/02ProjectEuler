
### recursive function to return ith value of Fibonacci sequence
def fib(i):
  if i == 0 or i == 1:
    return i
  else:
    return fib(i - 1) + fib(i - 2)

### function to add totals of even elements in sequence
def evenFibs(i):
  evenSumTotal = 0

  while fib(i) < 4000:
    if (fib(i) % 2) == 0:
      evenSumTotal += fib(i)
    i += 1
  return evenSumTotal

print(evenFibs(0))
