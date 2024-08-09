class LengthConverter:
    def __init__(self) -> None:
        self.__distance_in_meter = 0

    @property
    def meter(self):
        return self.__distance_in_meter
    
    @meter.setter
    def meter(self,x):
        self.__distance_in_meter = x

    @property
    def feet(self):
        return self.__distance_in_meter * 3.28084
    
    @feet.setter
    def feet(self,x):
        self.__distance_in_meter = x / 3.28084

    @property
    def inch(self):
        return self.__distance_in_meter *39.3701
    
    @inch.setter
    def inch(self,x):
        self.__distance_in_meter = x / 39.3701