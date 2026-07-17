from itertools import combinations
list=[-3,4,-1,-5,6,-4]
print("positive combination")
for r in range(1,len(list)+1):
  for combo in combination(list,r):
    if all(num>0 for num in combo):
      print(combo)
