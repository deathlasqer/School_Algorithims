NullPointer = None

class TreeNode:
    def __init__(self):
        self.Data = ""
        self.LeftPointer = None
        self.RightPointer = None

Tree = [TreeNode() for i in range(7)]

def InitialiseTree():
    global FreePtr, RootPointer
    RootPointer = NullPointer
    FreePtr = 0
    for index in range(6):
        Tree[index].LeftPointer = index + 1
    Tree[6].LeftPointer = NullPointer

def InsertNode(NewItem):
    global FreePtr, RootPointer
    if FreePtr is not NullPointer:
        NewNodePtr = FreePtr
        FreePtr = Tree[FreePtr].LeftPointer
        Tree[NewNodePtr].Data = NewItem
        Tree[NewNodePtr].LeftPointer = NullPointer
        Tree[NewNodePtr].RightPointer = NullPointer
        if RootPointer is NullPointer:
            RootPointer = NewNodePtr
        else:
            ThisNodePtr = RootPointer
            while ThisNodePtr is not NullPointer:
                PreviousNodePtr = ThisNodePtr
                if Tree[ThisNodePtr].Data > NewItem:
                    TurnedLeft = True
                    ThisNodePtr = Tree[ThisNodePtr].LeftPointer
                else:
                    TurnedLeft = False
                    ThisNodePtr = Tree[ThisNodePtr].RightPointer
            if TurnedLeft is True:
                Tree[PreviousNodePtr].LeftPointer = NewNodePtr
            else:
                Tree[PreviousNodePtr].RightPointer = NewNodePtr

def FindNode(SearchItem):
    global RootPointer
    ThisNodePtr = RootPointer
    while (ThisNodePtr is not NullPointer) and Tree[ThisNodePtr].Data != SearchItem:
        if Tree[ThisNodePtr].Data > SearchItem:
            ThisNodePtr = Tree[ThisNodePtr].LeftPointer
        else:
            ThisNodePtr = Tree[ThisNodePtr].RightPointer
    return ThisNodePtr

