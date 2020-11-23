from cth import db
from cth.models import Test
class TestDAO:

    def add_test( timestamp, is_positive, institution_name, illness, cid):
        new_test = Test(cid=cid, ttimestamp = timestamp ,tillness = illness , tispositive = is_positive , instlocation = institution_name)
        db.session.add(new_test)
        db.session.commit()
