# Write your code here
class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self,other):
        if 0 <= other <= 23:
            self.__hours = other

        else:
            raise ValueError("Invalid Values for hours!!")
        
    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self,other):
        if 0 <= other <= 59:
            self.__minutes = other

        else:
            raise ValueError("Invalid Values for minutes!!")

    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self,other):
        if 0 <= other <= 59:
            self.__seconds = other

        else:
            raise ValueError("Invalid Values for seconds!!")
        
    
        
    