#Service class for StorageFactory

from StorageStrategy import StorageStrategy
from StorageFactory import StorageFactory

class StorageService:
    def __init__(self, storageFactory: StorageFactory):
        self.StorageStrategy = storageFactory.createStrategy()
        
    def formatData(self, data: str):
        pass

    def postData(self, data: dict): 
        pass

    def getData(self, dataType: int, parameters: dict = {}):
        pass

    def getPersonData(self, SSN: int): 
        pass