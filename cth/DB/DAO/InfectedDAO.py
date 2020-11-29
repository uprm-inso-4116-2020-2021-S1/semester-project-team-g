from cth import db
from cth.models import Infected
from cth.models import Citizen
from flask import jsonify
from datetime import datetime as dt
import datetime

class InfectedDAO:

    def get_global_results():
        result = db.session.query(Infected).all()
        ret = []

        for r in result:

            sub = {'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
            ret.append(sub)

        return jsonify(Infected = ret)

    def get_results_by_municipality(municipality, illness=None):
        ret = []
        if illness==None:
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(Citizen.caddress.like('%' + municipality + '%'))
            for r in result:
                sub = {'municipality':r.citizen.caddress, 'cid':r.infected.cid,'infcount':r.infected.infcount,'infcheckup':r.infected.infcheckup,'infdate':r.infected.infdate, 'infname':r.infected.infname}
                ret.append(sub)

        else:
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(Citizen.caddress.like('%' + municipality + '%'), Infected.infname == illness)
            for r in result:
                sub = {'municipality':r.citizen.caddress, 'cid':r.infected.cid,'infcount':r.infected.infcount,'infcheckup':r.infected.infcheckup,'infdate':r.infected.infdate, 'infname':r.infected.infname}
                ret.append(sub)
        return jsonify(Infected = ret)

    def get_results_by_sex(sex, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(Citizen.cgender.like('%' + sex + '%'))
            for r in result:
                sub = {'sex':r.citizen.cgender, 'cid':r.citizen.cid,'infcount':r.infected.infcount,'infcheckup':r.infected.infcheckup,'infdate':r.infected.infdate, 'infname':r.infected.infname}
                ret.append(sub)
        else:
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(Citizen.cgender.like('%' + sex + '%'), Infected.infname == illness)
            for r in result:
                sub = {'sex':r.citizen.cgender, 'cid':r.citizen.cid,'infcount':r.infected.infcount,'infcheckup':r.infected.infcheckup,'infdate':r.infected.infdate, 'infname':r.infected.infname}
                ret.append(sub)
        return jsonify(Citizen_by_sex = ret)

        return jsonify(Infected_by_sex = ret)

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
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(Citizen.cdob >= min_year).filter(Citizen.cdob <= max_year).filter(Infected.infname == illness)
            for r in result:
                sub = {'age':r.citizen.cdob, 'cid':r.citizen.cid, 'infcount':r.infected.infcount, 'infcheckup':r.infected.infcheckup, 'infdate':r.infected.infdate, 'infname':r.infected.infname}
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
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(db.extract('month', Infected.infdate) == int(month), Infected.infname == illness)
            for r in result:
                sub = {'cid':r.citizen.cid, 'infcount':r.infected.infcount, 'infcheckup':r.infected.infcheckup, 'infdate':r.infected.infdate, 'infname':r.infected.infname}
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
            result = db.session.query(Infected, Citizen).join(Citizen, Infected.cid == Citizen.cid).filter(db.extract('year', Infected.infdate) == int(year), Infected.infname == illness)
            for r in result:
                sub = {'cid':r.citizen.cid, 'infcount':r.infected.infcount, 'infcheckup':r.infected.infcheckup, 'infdate':r.infected.infdate, 'infname':r.infected.infname}
                ret.append(sub)
        return jsonify(Citizen_by_year = ret)

    @staticmethod
    def add_infected(cid, count, checkup, infname):
        new_infected = Infected(cid=cid, infcount=count, infcheckup=checkup, infname=infname)
        db.session.add(new_infected)
        db.session.commit()


    def update_data(self, patient, information):
        #TODO
        return ''


    def delete_data(self, patient):
        #TODO
        return ''
