from cth import db
from cth.models import Citizen
from cth.models import Infected
from flask import jsonify
from datetime import datetime as dt
import datetime

class CitizenDAO:

    def get_global_results(self):
        result = db.session.query(Citizen).all()
        ret = []

        for r in result:

            sub = {'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
            ret.append(sub)

        return jsonify(Citizen = ret)

    @staticmethod
    def add_citizen(firstname, lastname, DOB, sex, address, phone, ssn, ishp):


        new_citizen = Citizen(cfirstname=firstname, clastname=lastname, cdob=DOB, cgender=sex, caddress=address,
                              cphone=phone, cssn=ssn, ishp=ishp)
        db.session.add(new_citizen)
        db.session.commit()
        return new_citizen.cid

    @staticmethod
    def update_citizen(firstname, lastname, DOB, sex, address, phone, ssn, email , ishp):
        db.session.update(Citizen).where(Citizen.cssn==ssn).values(cfirstname=firstname, clastname=lastname, cdob=DOB, cgender=sex, caddress=address,
                              cphone=phone, cssn=ssn, cemail = email , ishp=ishp)
        db.session.commit()

    @staticmethod
    def find_citizen(ssn):
        result = db.session.query(Citizen).filter(Citizen.cssn == ssn).first()
        if result is not None:
            ret = {'cid':result.cid}
            return ret
        else:
            return False

    @staticmethod
    def find_citizen_byid(id):
        result = db.session.query(Citizen).filter(Citizen.cid == id)

        ret = {'cid':result.cid, 'firstname':result.cfirstname, 'lastname':result.clastname , 'DOB':result.cDOB, 'sex':result.cgender, 'address':result.caddress,'phone':result.cphone,'ssn':result.cssn}

        return jsonify(Citizen=ret)
