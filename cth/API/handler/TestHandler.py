from cth.DB.DAO import TestDAO
class TestHandler:

    def add_test(timestamp, is_positive, institution_name, illness,cid):

        cursor = TestDAO.TestDAO

        cursor.add_test(timestamp, is_positive, institution_name, illness,cid)
