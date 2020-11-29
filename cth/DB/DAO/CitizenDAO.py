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
        
    def update_data(self, patient, information):
        #TODO
        return ''


    def delete_data(self, patient):
        #TODO
        return ''
