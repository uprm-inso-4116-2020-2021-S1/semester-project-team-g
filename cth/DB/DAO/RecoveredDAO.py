from cth import db
from cth.models import Citizen
from cth.models import Recovered
from flask import jsonify
from datetime import datetime as dt
import datetime

class RecoveredDAO:

    def get_global_results():
        result = db.session.query(Recovered).all()
        ret = []

        for r in result:

            sub = {'cid':r.cid, 'date': r.rdate, 'length': r.rlength, 'illness': r.rillness}
            ret.append(sub)

        return jsonify(Recovered = ret)

    def get_results_by_municipality(municipality, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Recovered,Citizen).join(Citizen, Recovered.cid == Citizen.cid).filter(Citizen.caddress.like('%' + municipality + '%'))
            for r in result:
                sub = {'municipality':r.citizen.caddress, 'cid':r.recovered.cid,'date': r.recovered.rdate, 'length': r.recovered.rlength, 'illness': r.recovered.rillness}
                ret.append(sub)
        else:
            result = db.session.query(Recovered, Citizen).join(Citizen, Recovered.cid == Citizen.cid).filter(Citizen.caddress.like('%' + municipality + '%'), Recovered.rillness == illness)
            for r in result:
                sub = {'municipality':r.citizen.caddress, 'cid':r.recovered.cid,'date': r.recovered.rdate, 'length': r.recovered.rlength, 'illness': r.recovered.rillness}
                ret.append(sub)
        return jsonify(Recovered_by_municipality = ret)

    def get_results_by_sex(sex, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Recovered, Citizen).join(Citizen, Recovered.cid == Citizen.cid).filter(Citizen.cgender.like('%' + sex + '%'))
            for r in result:
                sub = {'sex':r.citizen.cgender, 'cid':r.recovered.cid,'date': r.recovered.rdate, 'length': r.recovered.rlength, 'illness': r.recovered.rillness}
                ret.append(sub)
        else:
            result = db.session.query(Recovered, Citizen).join(Citizen, Recovered.cid == Citizen.cid).filter(Citizen.cgender.like('%' + sex + '%'), Recovered.rillness == illness)
            for r in result:
                sub = {'sex':r.citizen.cgender, 'cid':r.recovered.cid,'date': r.recovered.rdate, 'length': r.recovered.rlength, 'illness': r.recovered.rillness}
                ret.append(sub)
        return jsonify(Recovered_by_sex = ret)

    def get_results_by_age(min_age, max_age, illness=None):
        ret = []
        min_year = str(dt.now() - datetime.timedelta(days=int(max_age)*365.25))
        max_year = str(dt.now() - datetime.timedelta(days=int(min_age)*365.25))
        if not illness:
            result = db.session.query(Recovered, Citizen).join(Citizen, Recovered.cid == Citizen.cid).filter(Citizen.cdob >= min_year).filter(Citizen.cdob <= max_year)
            for r in result:
                sub = {'age':r.citizen.cdob, 'cid':r.recovered.cid,'date': r.recovered.rdate, 'length': r.recovered.rlength, 'illness': r.recovered.rillness}
                ret.append(sub)
        else:
            result = db.session.query(Recovered, Citizen).join(Citizen, Recovered.cid == Citizen.cid).filter(Citizen.cdob >= min_year).filter(Citizen.cdob <= max_year).filter(Recovered.rillness == illness)
            for r in result:
                sub = {'age':r.citizen.cdob, 'cid':r.recovered.cid,'date': r.recovered.rdate, 'length': r.recovered.rlength, 'illness': r.recovered.rillness}
                ret.append(sub)
        return jsonify(Recovered_by_age = ret)

    def get_results_by_month(month, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Recovered, Citizen).join(Citizen, Recovered.cid == Citizen.cid).filter(db.extract('month', Recovered.rdate) == int(month))
            for r in result:
                sub = {'cid':r.recovered.cid,'date': r.recovered.rdate, 'length': r.recovered.rlength, 'illness': r.recovered.rillness}
                ret.append(sub)
        else:
            result = db.session.query(Recovered, Citizen).join(Citizen, Recovered.cid == Citizen.cid).filter(db.extract('month', Recovered.rdate) == int(month), Recovered.rillness == illness)
            for r in result:
                sub = {'cid':r.recovered.cid,'date': r.recovered.rdate, 'length': r.recovered.rlength, 'illness': r.recovered.rillness}
                ret.append(sub)
        return jsonify(Recovered_by_month = ret)

    def get_results_by_year(year, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Recovered, Citizen).join(Citizen, Recovered.cid == Citizen.cid).filter(db.extract('year', Recovered.rdate) == int(year))
            for r in result:
                sub = { 'cid':r.recovered.cid,'date': r.recovered.rdate, 'length': r.recovered.rlength, 'illness': r.recovered.rillness}
                ret.append(sub)
        else:
            result = db.session.query(Recovered, Citizen).join(Citizen, Recovered.cid == Citizen.cid).filter(db.extract('year', Recovered.rdate) == int(year), Recovered.rillness == illness)
            for r in result:
                sub = {'cid':r.recovered.cid,'date': r.recovered.rdate, 'length': r.recovered.rlength, 'illness': r.recovered.rillness}
                ret.append(sub)
        return jsonify(Recovered_by_year = ret)

    @staticmethod
    def add_recovered(cid, rlength, rillness):
        new_recovered = Recovered(cid=cid,  rlength=rlength, rillness=rillness)
        db.session.add(new_recovered)
        db.session.commit()
        return new_recovered.cid

    @staticmethod
    def update_recovered(cid, rlength,rillness ):
        db.session.update(Recovered).where(Recovered.cid==cid).values( rlength=rlength, rillness=rillness)
        db.session.commit()


    @staticmethod
    def delete_recovered(id):
        db.session.query(Recovered).filter(Recovered.cid == id).delete()
        db.session.commit()

    @staticmethod
    def find_recovered(id):
        result = db.session.query(Recovered).filter(Recovered.cid == id).first()
        if result is not None:
            ret = {'cid':result.cid}
            return ret
        else:
            return False
