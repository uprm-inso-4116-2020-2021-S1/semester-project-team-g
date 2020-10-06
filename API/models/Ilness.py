# Class that defines Illness API Object.
class Illness:
    def __init__(self, name, illness_type="", infected_count=0, recovered_count=0, deceased_count=0):
        self.name = name
        self.illness_type = illness_type
        self.infected_count = infected_count
        self.recovered_count = recovered_count
        self.deceased_count = deceased_count
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.illness_type
    
    def set_type(self, illness_type):
        self.illness_type = illness_type

    def get_recovered_count(self):
        return self.recovered_count

    def set_recovered_count(self, recovered_count):
        self.recovered_count = recovered_count

    def get_deceased_count(self):
        return self.deceased_count

    def set_deceased_count(self, deceased_count):
        self.deceased_count = deceased_count
