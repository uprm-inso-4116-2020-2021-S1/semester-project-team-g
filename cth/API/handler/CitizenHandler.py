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
        return results

    def get_results_by_age(min_age, max_age, illness=None):
        if not illness:
            cursor = CitizenDAO.CitizenDAO
            results = cursor.get_results_by_age(min_age,max_age)
        else:
            results = cursor.get_results_by_municipality(min_age,max_age,illness=illness)
        return results

    @staticmethod
    def add_citizen(firstname, lastname, DOB, sex, address, phone, ssn, ishp, isPositive, infname):
        cid = CitizenDAO.CitizenDAO.add_citizen(firstname, lastname, DOB, sex, address, phone, ssn, ishp)
        if isPositive:
            InfectedHandler.InfectedHandler.add_infected(cid, 1, '14', infname)
        return cid
