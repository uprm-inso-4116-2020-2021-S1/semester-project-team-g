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
    def add_case(firstname, lastname, DOB, sex, address, phone, ssn, ishp, isPositive, infname):

        search = CitizenDAO.CitizenDAO.find_citizen(ssn)

        if not search:
            cid   = CitizenDAO.CitizenDAO.add_citizen(firstname, lastname, DOB, sex, address, phone, ssn, ishp)
            InfectedHandler.InfectedHandler.add_infected(cid,  1, '14', infname)
            return cid

        else:

            infected_search = InfectedDAO.InfectedDAO.find_infected(search['cid'])

            if not infected_search:
                InfectedHandler.InfectedHandler.add_infected(search['cid'],  1, '14', infname)
                return search['cid']

            else:
                if not isPositive:
                    rlen =  (dt.datetime.now() - infected_search['infdate']).days
                    RecoveredHandler.RecoveredHandler.add_recovered(search['cid'], rlen , infname)

                return search['cid']

    @staticmethod
    def update_citizen(firstname, lastname, DOB, sex, address, phone, ssn, email ,ishp):
        search = CitizenDAO.CitizenDAO.find_citizen(ssn)

        if not search:
            return -1

        cursor = CitizenDAO.CitizenDAO
        cursor.update_citizen(firstname, lastname, DOB, sex, address, phone, ssn, ishp)

        return search['cid']

    @staticmethod
    def find_citizen(ssn):

        cursor = CitizenDAO.CitizenDAO
        result = cursor.find_citizen(ssn)

        return result
