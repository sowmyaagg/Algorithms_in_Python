import random

def sortArray(inList):

    if len(inList) <= 1:

        return inList



    pivot = random.choice(inList)

    lt = [v for v in inList if v < pivot]

    eq = [v for v in inList if v == pivot]

    gt = [v for v in inList if v > pivot]

    return sortArray(lt) + eq + sortArray(gt)





if __name__ == "__main__":

    List1 = [34,98,2,0,6,23,91]

    print(sortArray(List1))
