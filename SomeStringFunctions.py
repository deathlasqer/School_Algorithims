import random

class String:
    def __init__(self, Value):
        if type(Value) is not str:
            print("Enter a STRING please")
        else:
            self.__value = Value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, update):
        self.__value = update

    def removePostAndPreSpaces(self):  # .strip() function in python
        StartOfStrIndex = 0
        while self.__value[StartOfStrIndex] == " ":
            StartOfStrIndex += 1
        EndOfStrIndex = len(self.__value) - 1
        while self.__value[EndOfStrIndex] == " ":
            EndOfStrIndex -= 1
        NewString = self.__value[StartOfStrIndex: EndOfStrIndex + 1]
        return NewString

    def shuffle(self):
        temp = ''.join(random.sample(self.__value, len(self.__value)))
        return temp

    def checkCharacter(self, position): # This function Checks if the Character in the given position of the string is a digit or alphabet
        if position > len(self.__value):
            print("Invalid, the string has only {} characters, you entered {}".format(len(self.__value), position))
        elif position < 1:
            print("invalid Position, positions must be greater than 0")
        else:
            try:
                checkIfDigit = int(self.__value[position - 1])
                print("The character in position {} Is a digit\nIt is: {}".format(position, self.__value[position - 1]))
            except:
                print("The character in position {} Is an alphabet\nIt is: {}".format(position, self.__value[position - 1]))



