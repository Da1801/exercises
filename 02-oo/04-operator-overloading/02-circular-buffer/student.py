class CircularBuffer:
    def __init__(self,size):
        self.__size = size
        self.__item = []

    def add(self,items):
        self.__item.append(items)

        if len(self.__item) > self.__size:
            del self.__item[0]

    def __getitem__(self,index):
        return self.__item[index]
    
    def __len__(self):
        return len(self.__item)
