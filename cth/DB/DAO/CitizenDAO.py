from cth import db
from cth.models import Citizen
from cth.models import Infected
from flask import jsonify
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import datetime

class CitizenDAO:

    def get_global_results(self):
        result = db.session.query(Citizen).all()
        ret = []

        for r in result:

            sub = {'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
            ret.append(sub)

        return jsonify(Citizen = ret)

    def get_results_by_municipality(municipality, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Citizen).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.caddress)
            for r in result:
                sub = {'municipality':r.caddress, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)
        else:
            result = db.session.query(Infected).filter(Infected.infname == illness).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.caddress)
            for r in result:
                sub = {'municipality':r.caddress, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)
        return jsonify(Citizen = ret)

    def get_results_by_sex(sex, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(Citizen.cgender.like('%' + sex + '%'))
            for r in result:
                sub = {'sex':r.citizen.cgender, 'cid':r.citizen.cid,'infcount':r.infected.infcount,'infcheckup':r.infected.infcheckup,'infdate':r.infected.infdate, 'infname':r.infected.infname}
                ret.append(sub)
        else:
            result = db.session.query(Infected).filter(Infected.infname == illness).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.gender)
            for r in result:
                sub = {'sex':r.cgender, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)
        return jsonify(Citizen_by_sex = ret)

    def get_results_by_age(min_age, max_age, illness=None):
        ret = []
        min_year = str(dt.now() - datetime.timedelta(days=int(max_age)*365.25))
        max_year = str(dt.now() - datetime.timedelta(days=int(min_age)*365.25))
        if not illness:
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(Citizen.cdob >= min_year).filter(Citizen.cdob <= max_year)
            for r in result:
                sub = {'age':r.citizen.cdob, 'cid':r.citizen.cid, 'infcount':r.infected.infcount, 'infcheckup':r.infected.infcheckup, 'infdate':r.infected.infdate, 'infname':r.infected.infname}
                ret.append(sub)
        else:
            result = db.session.query(Infected).filter(Infected.infname == illness).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.caddress)
            for r in result:
                sub = {'age':r.cDOB, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)
        return jsonify(Citizen_by_age = ret)

    def get_results_by_month(month, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(db.extract('month', Infected.infdate) == int(month))
            for r in result:
                sub = {'cid':r.citizen.cid, 'infcount':r.infected.infcount, 'infcheckup':r.infected.infcheckup, 'infdate':r.infected.infdate, 'infname':r.infected.infname}
                ret.append(sub)
        else:
            result = db.session.query(Infected).filter(Infected.infname == illness).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.caddress)
            for r in result:
                sub = {'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)
        return jsonify(Citizen_by_month = ret)

    def get_results_by_year(year, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(db.extract('year', Infected.infdate) == int(year))
            for r in result:
                sub = {'cid':r.citizen.cid, 'infcount':r.infected.infcount, 'infcheckup':r.infected.infcheckup, 'infdate':r.infected.infdate, 'infname':r.infected.infname}
                ret.append(sub)
        else:
            result = db.session.query(Infected).filter(Infected.infname == illness).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.caddress)
            for r in result:
                sub = {'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)
        return jsonify(Citizen_by_month = ret)

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
