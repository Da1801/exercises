class CircularBuffer:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__list = []

    def add(self, item):
        self.__list.append(item)
        if len(self.__list) > self.__max_size:
            del self.__list[0]

    def __getitem__(self, index):
        return self.__list[index]

    def __len__(self):
        return len(self.__list)
        