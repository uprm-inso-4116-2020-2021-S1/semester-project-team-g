from cth.DB.DAO import TestDAO


class TestHandler:

    @staticmethod
    def add_test(tillness, tispositive, instname, cid, oid):
        TestDAO.TestDAO.add_test(tillness, tispositive, instname, cid, oid)
