def insertionSort(listData):
    for i in range(1,len(listData)):
        key =  listData[i]
        idx = i
        while idx>0 and listData[idx-1] > key :
            listData[idx] = listData[idx-1]
            idx-= 1
        listData[idx] = key