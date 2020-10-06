# Class that defines the Operator API Object.
class Operator:
    def __init__(self, oid, first_name, last_name, level, institution_id=""):
        self.oid = oid
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.institution_id = institution_id

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

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_institution_id(self):
        return self.institution_id

    def set_institution_id(self, institution_id):
        self.institution_id = institution_id
