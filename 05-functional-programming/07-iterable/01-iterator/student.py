class InclusiveRange:
    def __init__(self,start,end):
        self.__start = start
        self.__end = end

    def __iter__(self):
        return InclusiveRangeIterator(self.__start,self.__end)
    
class InclusiveRangeIterator:
    def __init__(self,start,end):
        self.__start =start
        self.__end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__start <= self.__end:
            result = self.__start
            self.__start += 1
            return result
        
        else:
            raise StopIteration()