####    Comparaison sort algorithm  ####


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


def inplacemergesort():
    print("StartFastSort")


def heapsort():
    print("StartFastSort")


def insertionsort():
    print("StartFastSort")


def introsort():
    print("StartFastSort")


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
