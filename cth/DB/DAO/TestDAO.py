from cth import db
from cth.models import Test
class TestDAO:

    def add_test( timestamp, is_positive, institution_name, illness, cid):
        new_test = Tests(cid=cid, ttimestamp = count ,tillness = checkup , tispositive = date , institlocation = infname)
        db.session.add(new_test)
        db.session.commit()
