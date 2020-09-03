#Class which will generate a StorageStrategy

import os
from dotenv import load_dotenv

from StorageStrategy import StorageStrategy
from FileStorageStrategy import FileStorageStrategy


class StorageFactory:
    def __init__(self, fileStorageStrategy: FileStorageStrategy):
        self.strategy = self.generateStrategy()
        self.fileStorageStrategy = fileStorageStrategy
    
    def generateStrategy(self):
        if self.strategy:
            return self.strategy
        inDevelopment = os.getenv("IN_DEVELOPMENT")
        if inDevelopment:
            return self.fileStorageStrategy()
        else:
            # Here we would be passing a cloud or similar StorageStrategy implementation
            pass
    
    def getFunctions(self):
        return self.strategy.formatData, self.strategy.postData, self.strategy.getData, self.strategy.getPersonData