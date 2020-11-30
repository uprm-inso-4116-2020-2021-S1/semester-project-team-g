from cth.DB.DAO import RecoveredDAO
from cth.DB.DAO import InfectedDAO

class RecoveredHandler:
    def get_global_results():
        cursor = RecoveredDAO.RecoveredDAO
        results = cursor.get_global_results()
        return results

    def get_results_by_municipality(municipality, illness=None):
        cursor = RecoveredDAO.RecoveredDAO
        if illness==None:
            results = cursor.get_results_by_municipality(municipality)
        else:
            results = cursor.get_results_by_municipality(municipality, illness)
        return results

    def get_results_by_sex(sex, illness=None):
        cursor = RecoveredDAO.RecoveredDAO
        if not illness:
            results = cursor.get_results_by_sex(sex)
        else:
            results = cursor.get_results_by_sex(sex, illness=illness)
        return results

    def get_results_by_age(min_age, max_age, illness=None):
        cursor = RecoveredDAO.RecoveredDAO
        if not illness:
            results = cursor.get_results_by_age(min_age,max_age)
        else:
            results = cursor.get_results_by_municipality(min_age,max_age, illness=illness)
        return results

    def get_results_by_month(month, illness=None):
        cursor = RecoveredDAO.RecoveredDAO
        if not illness:
            results = cursor.get_results_by_month(month)
        else:
            results = cursor.get_results_by_month(month,illness=illness)
        return results

    def get_results_by_year(year, illness=None):
        cursor = RecoveredDAO.RecoveredDAO
        if not illness:
            results = cursor.get_results_by_year(year)
        else:
            results = cursor.get_results_by_year(year,illness=illness)
        return results

    @staticmethod
    def add_recovered(cid, rlength, rillness):
        RecoveredDAO.RecoveredDAO.add_recovered(cid, rlength, rillness)
        InfectedDAO.InfectedDAO.delete_infected(cid)
