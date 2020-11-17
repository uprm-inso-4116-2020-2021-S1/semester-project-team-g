#DAO corresponding to Operator
from cth import db
from cth.models import Operator
class OperatorDAO:

    def findOperator(username, password):
        result = db.session.query(Operator).filter(Operator.ousername == username, Operator.opassword == password)
        for r in result:
            return(r.ofirstname)