#Interface StorageStrategy

from abc import ABCMeta, abstractmethod
import json

class StorageStrategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def formatData(self, data: str):
        '''
        Formats string to JSON

        data: str
            Data that will be converted to JSON
        '''
        raise NotImplementedError

    @abstractmethod
    def postData(self, data: dict): 
        '''
        Adds data to storage/database

        data: dict
            Dictionary that will be converted to JSON containing 
            all of the information to be added to the storage
        '''
        raise NotImplementedError

    @abstractmethod
    def getData(self, dataType: int, parameters: dict = {}):
        '''
        Returns a dictionary of the information requested based on id

        dataType: int
            Integer that specifies the type of data being requested. 
            Currently id means: 1 - global population, 2 - municipal population
        parameters: dict
            Defaults to an empty dictionary in case parameters are not specified.
            Parameters will contain the data required when querying from the data stored
        '''
        raise NotImplementedError

    @abstractmethod
    def getPersonData(self, SSN: int): 
        '''
        Returns a dictionary containing the information of a specific person

        SSN: int
            Id of the person which data is being requested
        '''
        raise NotImplementedError