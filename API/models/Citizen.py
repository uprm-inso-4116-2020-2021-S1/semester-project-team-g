# Class for citizen API object.
class Citizen:
    def __init__(self, oid, first_name, last_name, ssn, date_of_birth="", gender="", address="", phone="",
                 is_alive=True):
        self.oid = oid
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.phone = phone
        self.ssn = ssn
        self.is_alive = is_alive
        
    def get_id(self):
        return self.oid

    def set_id(self, oid):
        self.oid = oid

    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_date_of_birth(self):
        return self.date_of_birth
        
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def get_gender(self):
        return self.gender
    
    def set_gender(self, gender):
        self.gender = gender

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_is_alive(self):
        return self.is_alive

    def set_is_alive(self, is_alive):
        self.is_alive = is_alive

    def get_ssn(self):
        return self.ssn

    def set_ssn(self, ssn):
        self.ssn = ssn
