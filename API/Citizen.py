#Class for citizen API object.
class Citizen:
    def __init__(self):
        self.id = int()
        self.f_name = str()
        self.l_name = str()
        self.DOB = str()
        self.gender = str()
        self.address = str()
        self.phone = str()
        self.ssn = int()
        self.isAlive = bool()
        
    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def get_f_name(self):
        return self.f_name
    
    def set_f_name(self, f_name):
        self.f_name = f_name

    def get_l_name(self):
        return self.get_l_name
    
    def set_l_name(self, l_name):
        self.l_name = l_name

    def get_DOB(self):
        return self.DOB
        
    def set_DOB(self, DOB):
        self.DOB = DOB

    def get_gender(self):
        return self.gender
    
    def set_gender(self, gender):
        self.gender = gender

    def get_address(self):
        return self.address

    def set_address(self, new_address):
        self.address = new_address

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_isAlive(self):
        return self.isAlive

    def set_isAlive(self, isAlive):
        self.isAlive = isAlive

    def get_ssn(self):
        return self.ssn

    def set_ssn(self, ssn):
        self.ssn = ssn    



    