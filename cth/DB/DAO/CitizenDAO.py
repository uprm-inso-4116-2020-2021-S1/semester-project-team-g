from cth import db
from cth.models import Citizen
from cth.models import Infected
class CitizenDAO:

    def get_global_results():
        result = db.session.query(Citizen).all()
        ret = []

        for r in result:

            sub = {'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
            ret.append(sub)

        return jsonify(Infected = ret)

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
            result = db.session.query(Infected).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.caddress)
            for r in result:

                sub = {'age':r.cDOB, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)
        else:
            result = db.session.query(Infected).filter(Infected.infname == illness).join(Citizen, Infected.cid == Citizen.cid).group_by(Citizen.caddress)
            for r in result:

                sub = {'age':r.cDOB, 'cid':r.cid,'infcount':r.infcount,'infcheckup':r.infcheckup,'infdate':r.infdate, 'infname':r.infname}
                ret.append(sub)

        return jsonify(Infected_by_age = ret)

    def add_citizen(firstname,lastname,DOB,sex,address,phone,ssn,ishp):
        new_citizen = Citizen(cfirstname = firstname ,clastname = lastname, cdob = DOB , cgender = sex , caddress = address , cphone = phone , cssn = ssn , ishp = ishp )
        db.session.add(new_citizen)
        db.session.commit()
        return new_citizen.cid

    def update_data(self, patient, information):
        #TODO
        return ''


    def delete_data(self, patient):
        #TODO
        return ''
