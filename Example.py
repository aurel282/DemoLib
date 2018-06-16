import SortAlgo.Algo
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
    myarraycopy = myarray.copy()
    init = time.time()
    print(SortAlgo.Algo.quicksort(myarraycopy))
    end = time.time()
    tquicksort = end - init
    print(tquicksort)

    print("mergesort")
    myarraycopy = myarray.copy()
    init = time.time()
    print(SortAlgo.Algo.mergesort(myarraycopy))
    end = time.time()
    tmergesort = end - init
    print(tmergesort)


    print("inplacemergesort")
    myarraycopy = myarray.copy()
    init = time.time()
    print(SortAlgo.Algo.inplacemergesort(myarraycopy))
    end = time.time()
    tinplacemergesort = end - init
    print(tinplacemergesort)

    print("heapsort")
    myarraycopy = myarray.copy()
    init = time.time()
    print(SortAlgo.Algo.heapsort(myarraycopy))
    end = time.time()
    theapsort = end - init
    print(theapsort)


    print("insertionsort")
    myarraycopy = myarray.copy()
    init = time.time()
    print(SortAlgo.Algo.insertionsort(myarraycopy))
    end = time.time()
    tinsertionsort= end - init
    print(tinsertionsort)

__main__()