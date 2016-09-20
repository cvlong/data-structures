"""SORTING ALGORITHMS."""

def bubble_sort(lst):
    """Return sorted list by checking side-by-side pairs; swapping if out of order.

    >>>bubble_sort([5, 8, 2, 5, 9, 10, 1])
    [1, 2, 5, 5, 8, 9, 10]

    """

    # move through list first time
    for i in range(len(lst) - 1):
        # keep track of whether we made a swap
        swapped = False
        # move through list second time, only for unsorted portion
        for j in range(len(lst) -1 -i):
            # switch if out of order
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            # if nothing swapped, then the list is already sorted, donezo
            break

    return lst


def merge_lists(lst1, lst2):
    """Merge two sorted lists into one sorted list.

    >>>merge_lists([2, 6, 8], [4, 7, 9])
    [2, 4, 6, 7, 8, 9]
    
    """

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


def merge_sort(lst):
    """Divides input into lists of one element, then merges sorted lists.

    >>>merge_sort([38, 27, 43, 3, 9, 82, 10])
    [3, 9, 10, 27, 38, 43, 82]

    """

    # base case: list contains one element, so it's sorted
    if len(lst) < 2:
        return lst

    # divide list in half
    mid = len(lst) / 2
    left_lst = lst[:mid]
    right_lst = lst[mid:]

    # sort each half
    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)

    # initialize output list
    merged = []

    # merge sorted sublists
    while left_lst or right_lst:

        # if one list is empty, add the remainder of the other list to output
        if not left_lst:
            merged.append(right_lst.pop(0))
        elif not right_lst:
            merged.append(left_lst.pop(0))

        # if items in both lists, remove the smallest first item and add to output
        elif left_lst[0] > right_lst[0]:
            merged.append(right_lst.pop(0))
        else:
            merged.append(left_lst.pop(0))

    return merged


    # Alternative way with len(lst):
    # while len(left_lst) > 0 or len(right_lst) > 0:
    # if left_lst == []:
    #     merged.append(right_lst.pop(0))
    # elif lst2 == []:
    #     merged.append(left_lst.pop(0))



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"