from cth.DB.DAO import CitizenDAO
from cth.DB.DAO import InfectedDAO
from cth.API.handler import InfectedHandler
from cth.API.handler import RecoveredHandler
import datetime as dt

class CitizenHandler:

    def get_global_results():

        cursor = CitizenDAO.CitizenDAO

        results = cursor.get_global_results()

        return results

    @staticmethod
    def add_citizen(firstname, lastname, DOB, sex, address, phone, ssn, email, ishp):

        search = CitizenDAO.CitizenDAO.find_citizen(ssn)

        if not search:
            cid   = CitizenDAO.CitizenDAO.add_citizen(firstname, lastname, DOB, sex, address, phone, ssn, email, ishp)
            return cid

        return False




    @staticmethod
    def update_citizen(firstname, lastname, DOB, sex, address, phone, ssn, email ,ishp):
        search = CitizenDAO.CitizenDAO.find_citizen(ssn)

        if not search:
            return -1

        cursor = CitizenDAO.CitizenDAO
        cursor.update_citizen(firstname, lastname, DOB, sex, address, phone, ssn, email,  ishp)

        return search['cid']

    @staticmethod
    def find_citizen(ssn):

        cursor = CitizenDAO.CitizenDAO
        result = cursor.find_citizen(ssn)

        return result
