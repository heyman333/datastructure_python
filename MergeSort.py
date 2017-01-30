
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        print("lefthalf:", lefthalf)
        print("righthalf:", righthalf)

        print("1st start!")
        mergeSort(lefthalf)
        print("2nd start!")
        mergeSort(righthalf)
        print("righthalf2:", righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    print("Merging ", alist)
    print("Merging end")

alist = [10,2,20,1,9,0,44,7]
mergeSort(alist)
print(alist)
