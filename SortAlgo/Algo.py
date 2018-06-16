####    Comparaison sort algorithm  ####

### ToDO : 20/25

def quicksort(myarray):
    #print("quicksort")
    less = []
    equal = []
    greater = []
    pivot = []
    if len(myarray) > 1:
        pivot = myarray[0]
        for x in myarray:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less) + equal + quicksort(greater)  # Just use the + operator to join lists
        # Note that you want equal ^^^^^ not pivot
    # You need to hande the part at the end of the recursion
    # - when you only have one element in your array, just return the array.
    else:
        return myarray


def mergesort(myarray):
    #print("mergesort")
    #print("Splitting ", myarray)
    if len(myarray) > 1:
        mid = len(myarray) // 2
        lefthalf = myarray[:mid]
        righthalf = myarray[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                myarray[k] = lefthalf[i]
                i = i + 1
            else:
                myarray[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            myarray[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            myarray[k] = righthalf[j]
            j = j + 1
            k = k + 1
        return myarray


def inplacemergesort(myarray):
    #print("inplacemergesort")
    if len(myarray) <= 1:
        return myarray

    mid = int(len(myarray) / 2)

    left = myarray[0:mid]
    right = myarray[mid:(len(myarray))]

    print
    left
    print
    right
    # exit()

    left = inplacemergesort(left)
    right = inplacemergesort(right)
    result = []
    while len(left) > 0 and len(right) > 0:
        lv = left[0]
        rv = right[0]
        if lv <= rv:
            result.append(lv)
            left.pop(0)
        else:
            result.append(rv)
            right.pop(0)
    while len(left) > 0:
        result.append(left.pop(0))

    while len(right) > 0:
        result.append(right.pop(0))

    return result;


def heapsort(myarray):
    #print("heapsort")
    n = len(myarray)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(myarray, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        myarray[i], myarray[0] = myarray[0], myarray[i]  # swap
        heapify(myarray, i, 0)

    return myarray


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def insertionsort(myarray):
    #print("insertionsort")
    for index in range(1, len(myarray)):

        currentvalue = myarray[index]
        position = index

        while position > 0 and myarray[position - 1] > currentvalue:
            myarray[position] = myarray[position - 1]
            position = position - 1

            myarray[position] = currentvalue

    return myarray


def introsort():
    print("introsort")


def selectionsort():
    print("StartFastSort")


def timsort():
    print("StartFastSort")


def cubesort():
    print("StartFastSort")


def shellsort():
    print("StartFastSort")


def bubblesort():
    print("StartFastSort")


def binarytreesort():
    print("StartFastSort")


def cyclesort():
    print("StartFastSort")


def librarysort():
    print("StartFastSort")


def partiencesorting():
    print("StartFastSort")


def smoothsort():
    print("StartFastSort")


def strandsort():
    print("StartFastSort")


def tournamentsort():
    print("StartFastSort")


def cockailsortsort():
    print("StartFastSort")


def combsort():
    print("StartFastSort")


def gnomesort():
    print("StartFastSort")


def unshufflesort():
    print("StartFastSort")


def franceschinismethodsort():
    print("StartFastSort")


def blocksort():
    print("StartFastSort")


def oddevensort():
    print("StartFastSort")
