from cth.DB.DAO import TestDAO, InfectedDAO
from cth.DB.DAO import RecoveredDAO
from cth.DB.DAO import CitizenDAO
from cth.API.handler import InfectedHandler, RecoveredHandler
from datetime import datetime as dt



class TestHandler:

    @staticmethod
    def add_test(tillness, tispositive, instname, cid, oid):
        return TestDAO.TestDAO.add_test(tillness, tispositive, instname, cid, oid)


    @staticmethod
    def add_new_test(tillness, tispositive, instname,  oid, ssn):

        search = CitizenDAO.CitizenDAO.find_citizen(ssn)

        if not search:
            return {"message": "User not found"}


        infected_search = InfectedDAO.InfectedDAO.find_infected(search['cid'], tillness)


        if tispositive:
            if not infected_search:
                InfectedHandler.InfectedHandler.add_infected(search['cid'], 1, '14', tillness)
        else:
            if infected_search:

                recovered_search = RecoveredDAO.RecoveredDAO.find_recovered(search['cid'],tillness)

                if not recovered_search:
                    rlen =  (dt.now() - infected_search['infdate']).days
                    RecoveredHandler.RecoveredHandler.add_recovered(search['cid'], rlen , tillness)

        TestDAO.TestDAO.add_test(tillness, tispositive, instname, search['cid'], oid)
        return 1
