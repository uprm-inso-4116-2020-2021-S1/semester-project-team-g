from cth.DB.DAO import CitizenDAO
from cth.API.handler import InfectedHandler
class CitizenHandler:

    def get_global_results():

        cursor = CitizenDAO.CitizenDAO

        results = cursor.get_global_results()

        return results

    @staticmethod
    def add_citizen(firstname, lastname, DOB, sex, address, phone, ssn, ishp, isPositive, infname):
        cid = CitizenDAO.CitizenDAO.add_citizen(firstname, lastname, DOB, sex, address, phone, ssn, ishp)
        if isPositive:
            InfectedHandler.InfectedHandler.add_infected(cid, 1, '14', infname)
        return cid
