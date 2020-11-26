from cth import db
from cth.models import Test


class TestDAO:

    @staticmethod
    def add_test(tillness, tispositive, instname, cid, oid):
        new_test = Test(tillness=tillness, tispositive=tispositive, instname=instname, cid=cid, oid=oid)
        db.session.add(new_test)
        db.session.commit()
