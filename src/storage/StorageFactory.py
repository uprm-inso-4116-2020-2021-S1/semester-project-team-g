#Class which will generate a StorageStrategy

import os
from dotenv import load_dotenv

from StorageStrategy import StorageStrategy
from FileStorageStrategy import FileStorageStrategy


class StorageFactory:
    def __init__(self, fileStorageStrategy: FileStorageStrategy):
        self.fileStorageStrategy = fileStorageStrategy
    
    def createStrategy(self):
        inDevelopment = os.getenv("IN_DEVELOPMENT")
        if inDevelopment:
            return self.fileStorageStrategy()
        else:
            # Here we would be passing a cloud or similar StorageStrategy implementation
            pass