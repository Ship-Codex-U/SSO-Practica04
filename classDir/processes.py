from classDir.process import Process

class Processes:
    def __init__(self):
        self.__processes = []
        
    @property
    def processes(self):
        return self.__processes
    
    @processes.setter
    def processes(self, processes):
        self.__processes = processes
    
    def insert(self, process):
        self.__processes.append(process)
    
    def getFIFOalgorithm(self):
        return self.__processes
    
    def getSJFalgorithm(self):
        return sorted(self.processes, key=lambda x: int(x.duration))
    
    def getPriorityAlgorithm(self):
        return sorted(self.processes, key=lambda x: int(x.priority))
    
    def getRoundRobinAlgorithm(self, quantum):
        processes = self.__processes
        newProcessesList = []
        totalDuration = 0
        
        for process in processes:
            totalDuration += int(process.duration)
            
        print(f"totalDuration: ->{totalDuration}<-")
            
        actualDuration = 0
        
        while actualDuration <= totalDuration:
            print(f"Duracion = {actualDuration}")
            for process in processes:
                if int(process.duration) != 0:
                    if int(process.duration) - quantum < 0:
                        newProcessesList.append(Process(process.name, str(quantum), process.priority, process.color))
                        print(Process(process.name, str(quantum), process.priority, process.color))
                        process.duration = str(int(process.duration) - quantum)
                        
                        actualDuration += quantum
                    else:
                        newProcessesList.append(Process(process.name, process.duration, process.priority, process.color))
                        print(Process(process.name, process.duration, process.priority, process.color))
                        actualDuration += int(process.duration)
                        
                        process.duration = str(0)
                print(f"ciclo completado")
            
        print(f"totalDuration: ->{actualDuration}<-")
        print(f"newProcessesList: ->{newProcessesList}<-")
        
        return newProcessesList
            
        
        
        
        
    