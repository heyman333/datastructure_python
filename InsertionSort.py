def Insertion_sort(un_list):

    for idx in range(len(un_list)):
        # select the hole position where number is to be inserted
        holePosition = idx
        valueToInsert = un_list[idx]
        # check if previous no. is larger than value to be inserted
        while holePosition > 0 and un_list[holePosition-1] > valueToInsert:
            un_list[holePosition - 1], un_list[holePosition] = un_list[holePosition], un_list[holePosition-1]
            holePosition = holePosition - 1

    return un_list

un_list = [10,9,8,7,5,20,30]
new_list = Insertion_sort(un_list)
print(new_list)
