NullPointer = None


class ListNode:
    def __init__(self):
        self.Data = ""
        self.Pointer = None

    def PrintDetails(self):
        print("data:", self.Data, "\npointer:", self.Pointer)


List = [ListNode() for i in range(7)]


def InitialiseList():
    global StartPointer, FreeListPtr, List
    StartPointer = None
    FreeListPtr = 0
    for index in range(6):
        List[index].Pointer = index + 1
    List[6].Pointer = None


def InsertNode(NewItem):
    global StartPointer, FreeListPtr, List
    if FreeListPtr is not None:
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = NewItem
        FreeListPtr = List[FreeListPtr].Pointer

        ThisNodePtr = StartPointer
        PreviousNodePtr = None
        while (ThisNodePtr is not None) and (List[ThisNodePtr].Data < NewItem):
            PreviousNodePtr = ThisNodePtr
            ThisNodePtr = List[ThisNodePtr].Pointer

        if PreviousNodePtr is None:
            List[NewNodePtr].Pointer = StartPointer
            StartPointer = NewNodePtr
        else:
            List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
            List[PreviousNodePtr].Pointer = NewNodePtr
    else:
        print("No Place in list")


# Must be an ordered linked list
def FindNode(DataItem):  # return Integer, Pointer to the node
    global StartPointer, FreeListPtr, List
    ThisNodePtr = StartPointer
    while (ThisNodePtr is not None) and (List[ThisNodePtr].Data < DataItem):
        ThisNodePtr = List[ThisNodePtr].Pointer
    if ThisNodePtr is not None:
        return ThisNodePtr
    else:
        return "Item Not Found"


# Must be an ordered linked list
def DeleteNode(DataItem):
    global StartPointer, FreeListPtr, List
    ThisNodePtr = StartPointer
    while (ThisNodePtr is not None) and (List[ThisNodePtr].Data != DataItem):
        PreviousNodePtr = ThisNodePtr
        ThisNodePtr = List[ThisNodePtr].Pointer
    if ThisNodePtr is not None:
        if ThisNodePtr == StartPointer:
            StartPointer = List[StartPointer].Pointer
        else:
            List[PreviousNodePtr].Pointer = List[ThisNodePtr].Pointer
        List[ThisNodePtr].Pointer = FreeListPtr
        FreeListPtr = ThisNodePtr


def OutputAllNodes():
    global StartPointer, FreeListPtr, List
    ThisNodePtr = StartPointer
    while (ThisNodePtr is not None):
        print(List[ThisNodePtr].Data)
        ThisNodePtr = List[ThisNodePtr].Pointer


