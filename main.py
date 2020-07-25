


#for loop

l=[]
def squareFor(x):
  for i in x:
    l.append(i**2)
  return l
res=squareFor([1,2,3,4,5])
print(res)
#map
def square(x):
  return x**2
li=[1,2,3,4,5]
squaredList=list(map(square,li))
print(squaredList)

#filtering list of even no
l=[]
def even(x):
  for i in x:
    if(i%2==0):
      l.append(i)
  return l
filter=even([1,2,3,4,5])
print(filter)

#filter
'''
def evenno(t):
  
    return t%2==0
  
filteredList=list(filter(evenno,[1,2,3,4,5]))
print(filteredList)
'''
#reduce
from functools import reduce
def reduceList(acc,x):
  print(acc,x)
  return acc+x
reducedList=reduce(reduceList,[1,2,3,4,5])
print(reducedList)

#lambda
y=lambda z:z**2
print(y(2))


mapp=list(map(lambda x:x**2,[1,2,3,4,5]))
print(mapp)


'''
filtered=list(filter(lambda x:x%2==0,[1,2,3,4,5]))
print(filtered)

'''

from functools import reduce
reduced=reduce((lambda acc,x:acc+x),[1,2,3,4,5])
print(reduced)

#list comprehension
l=[i for i in range(10)]
print(l)

evenList=[i for i in [1,2,3,4,5] if(i%2==0)]
print(evenList)