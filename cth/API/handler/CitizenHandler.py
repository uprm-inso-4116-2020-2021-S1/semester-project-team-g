from cth.DB.DAO import CitizenDAO
from cth.API.handler import InfectedHandler
class CitizenHandler:

    def get_global_results():

        cursor = CitizenDAO.CitizenDAO

        results = cursor.get_global_results()

        return results

    def get_results_by_municapility(municipality, illness=None):
        if not illness:
            cursor = CitizenDAO.CitizenDAO
            results = cursor.get_results_by_municipality(municipality)
        else:
            results = cursor.get_results_by_municipality(municipality, illness=illness)
        return result

    def get_results_by_sex(sex, illness=None):
        if not illness:
            cursor = CitizenDAO.CitizenDAO
            results = cursor.get_results_by_sex(sex)
        else:
            results = cursor.get_results_by_sex(sex, illness=illness)
        return result

    def get_results_by_age(min_age, max_age, illness=None):
        if not illness:
            cursor = CitizenDAO.CitizenDAO
            results = cursor.get_results_by_age(min_age,max_age)
        else:
            results = cursor.get_results_by_municipality(min_age,max_age,illness=illness)
        return result

    def add_citizen(firstname,lastname,DOB,sex,address,phone,ssn,ishp,isPositive,infname,date):
        if isPositive:
            cursor = CitizenDAO.CitizenDAO
            cid = cursor.add_citizen(firstname,lastname,DOB,sex,address,phone,ssn,ishp)
            InfectedHandler.InfectedHandler.add_infected(cid, 1, '14', date, infname)
        else:
            cursor = CitizenDAO.CitizenDAO
            cursor.add_citizen(firstname,lastname,DOB,sex,address,phone,ssn,ishp)
        return cid
