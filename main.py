"""
1!=1x1!
2!=2x1!
3!=3x2!
4!=4x3!

10!=10x9!

for - (n-1)!
"""


def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n-1)


number = int(input("enter a value:"))
res = fact_rec(number)

print("the factorial of {} is {} .". format(number, res))

