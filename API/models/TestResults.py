# Class that defines the TestResults API Object.
class TestResults:
    def __init__(self, oid, timestamp, is_positive, location, illness, cid):
        self.oid = oid
        self.timestamp = timestamp
        self.is_positive = is_positive
        self.location = location
        self.illness = illness
        self.cid = cid

    def get_id(self):
        return self.oid

    def set_id(self, oid):
        self.oid = oid

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def get_is_positive(self):
        return self.is_positive

    def set_is_positive(self, is_positive):
        self.is_positive = is_positive

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_illness(self):
        return self.illness

    def set_illness(self, illness):
        self.illness = illness

    def get_cid(self):
        return self.cid

    def set_cid(self, cid):
        self.cid = cid
