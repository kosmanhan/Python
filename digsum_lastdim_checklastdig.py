#finding the digital sum of a number, n
def digsum(n):
    digsum=0
  while len(str(n))>1:
    for i in range(len(str(n))):
      digsum=digsum+int(str(n)[i])
    n=digsum
  return n

#finding the last digit of a number, n
def lastdig(n):
  return int((str(n))[-1])

#checking the last digit to determine evenness
def evennum(n):
  t=lastdig(n)
  even=[0,2,4,6,8]
  if t in even:
    return True
  else:
    return False
