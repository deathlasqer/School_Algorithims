NullPointer = None
EMPTYSTRING = ""
MaxQueueSize = 8
Queue = [EMPTYSTRING for i in range(MaxQueueSize)]

def InitilaiseQueue():
    global NumberInQueue, EndOfQueuePointer, FrontOfQueuePointer
    FrontOfQueuePointer = 0
    EndOfQueuePointer = -1
    NumberInQueue = 0

def AddToQueue(NewItem):
    global NumberInQueue, EndOfQueuePointer
    if NumberInQueue < MaxQueueSize:
        EndOfQueuePointer += 1
        if EndOfQueuePointer > MaxQueueSize - 1:
            EndOfQueuePointer = 0
        Queue[EndOfQueuePointer] = NewItem
        NumberInQueue += 1

def RemoveFromQueue():
    global NumberInQueue, FrontOfQueuePointer
    Item = EMPTYSTRING
    if NumberInQueue > 0:
        Item = Queue[FrontOfQueuePointer]
        NumberInQueue -= 1
        if NumberInQueue == 0:
            InitilaiseQueue()
        else:
            FrontOfQueuePointer += 1
            if FrontOfQueuePointer > MaxQueueSize - 1:
                FrontOfQueuePointer = 0
    Queue[Queue.index(Item)] = EMPTYSTRING
