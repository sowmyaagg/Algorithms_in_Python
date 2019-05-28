def merge(a, b):
     index_a = 0
     index_b = 0
     c = []
     while index_a < len(a) and index_b < len(b):
         if a[index_a] <= b[index_b]:
             c.append(a[index_a])
             index_a = index_a + 1
         else:
             c.append(b[index_b])
             index_b = index_b + 1
     # when we exit the loop
     # we are at the end of at least one of the lists
     c.extend(a[index_a:])
     c.extend(b[index_b:])
     return c

def msort(list):
     if len(list) == 0 or len(list) == 1: # base case
        return list[:len(list)] # copy the input
     # recursive case
     halfway = len(list) // 2
     list1 = list[0:halfway]
     list2 = list[halfway:len(list)]
     newlist1 = msort(list1) # recursively sort left half
     newlist2 = msort(list2) # recursively sort right half
     newlist = merge(newlist1, newlist2)
     return newlist


if __name__ == "__main__":

    inList    = [40, 98, 34, 0, 23, 65, 12, 9, 4, 72]
    msortList = msort(inList)
    psortList = sorted(inList)
    print("Merge Sort Answer: " + repr(msortList), "\n Python Inbuilt Sort result: ", repr(psortList) )

