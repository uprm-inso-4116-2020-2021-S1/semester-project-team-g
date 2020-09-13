#Class that defines ilness API Object.
class Ilness:
    def __init__(self):
        self.illname = str()
        self.illtype = str()
    
    def get_illname(self):
        return self.illname
    
    def set_illname(self, illname):
        self.illname = illname

    def get_illtype(self):
        return self.illtype
    
    def set_illtype(self, illtype):
        self.illtype = illtype
    
