def selectionSort(un_list):
    for i in range(len(un_list)):
        minNum = un_list[i]
        flag = 0
        for j in range(i, len(un_list)):
            if minNum > un_list[j] :
                minNum = un_list[j]
                flag = j
        print('flag :', flag)
        if flag is not 0 :
            un_list[i], un_list[flag] = un_list[flag], un_list[i]
    return un_list

test = [0,4,3]
new_list = selectionSort(test)
print(new_list)
