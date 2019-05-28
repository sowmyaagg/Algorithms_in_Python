#Intersection of two arrays

def intersect(x,y)
  if x and y:
    return [v for v in List1 if v in List2]
  else:
    return []

if "name" == "__main__"
  List1 = [0,23,18,67,45,92,10]
  List2 = [0,1,2,3,4,5,6,7,9,10]
  
  print(intersect(List1,List2))
