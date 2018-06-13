import SortAlgo.Algo
import array
import random
import time


def ___generateintarray___ (length, min, max):
    myarray = []
    for i in range(length):
        myarray.append(random.randrange(min, max))

    return myarray




def __main__():
    myarray = ___generateintarray___(1000, 0, 100000)
    print(myarray)

    print("quicksort")
    myarraycopy = myarray
    init = time.time()
    print(SortAlgo.Algo.quicksort(myarraycopy))
    end = time.time()
    tquicksort = end - init
    print(tquicksort)

    print("mergesort")
    myarraycopy = myarray
    init = time.time()
    print(SortAlgo.Algo.mergesort(myarraycopy))
    end = time.time()
    tmergesort = end - init
    print(tmergesort)



__main__()