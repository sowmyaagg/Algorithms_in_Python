#Assumption - no negative number 
def BinarySearch(inList, value):
    low  =  0

    high =  len(inList)-1

    while (low<=high):

        mid = (low+high)//2

        if inList[mid] == value:
            return mid

        elif inList[mid] < value:
            low = mid + 1

        elif inList[mid] > value:
            high = mid - 1

    return -1


if "name" == "__main__":
    test_list = [1,3,9,11,15,19,29]
    
    test_val1 = 25
    
    test_val2 = 15
    
    print(BinarySearch(test_list, test_val1))
    print(BinarySearch(test_list, test_val2))
    
    # Try with different inputs !
