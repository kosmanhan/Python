#this checks whether or not an odd number is prime
#current work to do: i) finding how long it takes based on the number of digits, ii) end the operation if it fulfills the rules for divisibility by 3, & 5, iii) add even number rules so that it applies to even numbers also

import numpy

def prime(x):
  boolean=[]
  for i in range(3,x,2):
    boolean.append(((x/i).is_integer()))
  print(str(x)+" has "+str(sum(boolean))+" prime divisors.")
