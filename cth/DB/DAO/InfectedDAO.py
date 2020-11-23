from cth import db
from cth.models import Infected
from flask import jsonify

class InfectedDAO:

    def get_global_results():
        result = db.session.query(Infected).all()
        ret = []

        for r in result:

            sub = {'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
            ret.append(sub)

        return jsonify(Infected = ret)

    def get_results_by_municapility(municipality, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Infected).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.address)

            for r in result:

                sub = {'municipality':r.caddress, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)


        else:
            result = db.session.query(Infected).filter(Infected.infname == illness).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.address)
            for r in result:

                sub = {'municipality':r.caddress, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)

        return jsonify(Infected = ret)

    def get_results_by_sex(sex, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Infected).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.gender)
            for r in result:

                sub = {'sex':r.cgender, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)
        else:
            result = db.session.query(Infected).filter(Infected.infname == illness).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.gender)
            for r in result:

                sub = {'sex':r.cgender, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)


        return jsonify(Infected_by_sex = ret)

    def get_results_by_age(min_age, max_age, illness=None):
        ret = []
        if not illness:
            result = db.session.query(Infected).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.address)
            for r in result:

                sub = {'age':r.cDOB, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)
        else:
            result = db.session.query(Infected).filter(Infected.infname == illness).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.address)
            for r in result:

                sub = {'age':r.cDOB, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)

        return jsonify(Infected_by_age = ret)

    def add_infected(cid,count, checkup ,date,infname):
        new_infected = Infected(cid=cid, infcount = count ,infcheckup = checkup , date = date , infname = infname)
        db.session.add(new_infected)
        db.session.commit()


    def update_data(self, patient, information):
        #TODO
        return ''


    def delete_data(self, patient):
        #TODO
        return ''
