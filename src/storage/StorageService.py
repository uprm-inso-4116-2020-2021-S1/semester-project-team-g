#Service class for StorageFactory

from StorageStrategy import StorageStrategy
from StorageFactory import StorageFactory

class StorageService:
    def __init__(self, storageFactory: StorageFactory):
        self.storageStrategy = storageFactory.createStrategy()

        # Handle high-order functions
        self._formatData, self._postData, self._getData, self._getPersonData = storageFactory.getFunctions()
        
    def formatData(self, data: str):
        self._formatData(data)
        pass

    def postData(self, data: dict): 
        self._postData(data)
        pass

    def getData(self, dataType: int, parameters: dict = {}):
        self._getData(dataType, parameters)
        pass

    def getPersonData(self, SSN: int): 
        self._getPersonData(SSN)
        pass