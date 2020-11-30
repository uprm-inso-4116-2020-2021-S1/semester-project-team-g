from cth.DB.DAO import TestDAO
from cth.DB.DAO import RecoveredDAO
from cth.DB.DAO import CitizenDAO


class TestHandler:

    @staticmethod
    def add_test(tillness, tispositive, instname, cid, oid):
        TestDAO.TestDAO.add_test(tillness, tispositive, instname, cid, oid)

        
