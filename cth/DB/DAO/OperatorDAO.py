# DAO corresponding to Operator
from cth import db
from cth.models import Operator


class OperatorDAO:

    @staticmethod
    def findOperator(username, password):
        result = db.session.query(Operator).filter_by(ousername=username, opassword=password).first()
        if result:
            return result.ofirstname, result.oid
        return None, None
