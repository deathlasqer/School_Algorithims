def bubbleSort(array):
    for x in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[x]:
                temp = array[j]
                array[j] = array[x]
                array[x] = temp


def insertionSort(array):
    for pointer in range(1, len(array)):
        ItemToBeInserted = array[pointer]
        CurrentItem = pointer - 1
        while (array[CurrentItem] > ItemToBeInserted) and (CurrentItem > -1):
            array[CurrentItem + 1] = array[CurrentItem]
            CurrentItem -= 1
        array[CurrentItem + 1] = ItemToBeInserted


def binarySearch(array, SearchItem):
    insertionSort(array)
    if len(array) == 0:
        return "Array is empty"
    First = 0
    Last = len(array) - 1
    while True:
        Middle = int((First + Last) / 2)
        if array[Middle] == SearchItem:
            return Middle
        else:
            if First >= Last:
                return "Item Not Found"
            else:
                if array[Middle] > SearchItem:
                    Last = Middle - 1
                else:
                    First = Middle + 1


def linearSearch(Array, SearchItem):
    for x in range(len(Array)):
        if Array[x] == SearchItem:
            return x
    return "Item Not Found"
