"""SORTING ALGORITHMS."""

def bubblesort(lst):
    """Loop through & check side-by-side pair; swap nums if out of order."""

    for i in range(len(lst) - 1):
        swapped = False
        for j in range(len(lst) -1 -i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            # if nothing swapped, then the list is already sorted, donezo
            break

    return lst

# print bubblesort([5, 8, 2, 5, 9, 10, 1])


def merge_lists(lst1, lst2):
    """Merge two sorted lists."""

    merged = []

    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            merged.append(lst2.pop(0))
        elif lst2 == []:
            merged.append(lst1.pop(0))
        elif lst1[0] > lst2[0]:
            merged.append(lst2.pop(0))
        else:
            merged.append(lst1.pop(0))

    return merged

# print merge_lists([2, 6, 8], [4, 7, 9])


def mergesort(lst):
    """Divide lst into lists of 1 element, then merge sorted lists."""

    # make each element in the original lst into a list of 1
    if len(lst) < 2:
        return lst

    mid = len(lst) / 2
    lst1 = mergesort(lst[:mid])
    lst2 = mergesort(lst[mid:])

    merged = []
    print merged
    print lst1, lst2
    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            merged.append(lst2.pop(0))
        elif lst2 == []:
            merged.append(lst1.pop(0))
        elif lst1[0] > lst2[0]:
            merged.append(lst2.pop(0))
        else:
            merged.append(lst1.pop(0))

    return merged

# print mergesort([38, 27, 43, 3, 9, 82, 10])