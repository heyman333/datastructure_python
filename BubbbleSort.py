import unittest

def bubblesort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

    return alist

unsorted_list = [10, 3, 4, 20, 9, 1, 23]
sorted_list = bubblesort(unsorted_list)
print(sorted_list)
