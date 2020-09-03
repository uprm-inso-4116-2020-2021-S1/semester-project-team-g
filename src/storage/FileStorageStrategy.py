#Implementation for FileStorageStrategy based on the StorageStrategy interface

from StorageStrategy import StorageStrategy

class FileStorageStrategy(StorageStrategy):
    def formatData(self, data: str):
        pass

    def postData(self, data: dict): 
        pass

    def getData(self, dataType: int, parameters: dict = {}):
        pass

    def getPersonData(self, SSN: int): 
        pass

   