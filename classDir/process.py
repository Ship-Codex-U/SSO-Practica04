class Process:
    def __init__(self, name, duration, priority, color):
        self.__name = name
        self.__duration = duration
        self.__priority = priority
        self.__color = color
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, duration):
        self.__duration = duration
        
    @property
    def priority(self):
        return self.__priority
    
    @priority.setter
    def priority(self, priority):
        self.__priority = priority
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
