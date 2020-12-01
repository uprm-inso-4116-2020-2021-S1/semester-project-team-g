from cth.DB.DAO import InfectedDAO, RecoveredDAO
class InfectedHandler:

    def get_global_results():

        cursor = InfectedDAO.InfectedDAO

        results = cursor.get_global_results()

        return results

    def get_results_by_municipality(municipality, illness=None):
        cursor = InfectedDAO.InfectedDAO
        if illness==None:
            results = cursor.get_results_by_municipality(municipality)
        else:
            results = cursor.get_results_by_municipality(municipality, illness)
        return results

    def get_results_by_sex(sex, illness=None):
        cursor = InfectedDAO.InfectedDAO
        if not illness:
            results = cursor.get_results_by_sex(sex)
        else:
            results = cursor.get_results_by_sex(sex, illness=illness)
        return results

    def get_results_by_age(min_age, max_age, illness=None):
        cursor = InfectedDAO.InfectedDAO
        if not illness:
            results = cursor.get_results_by_age(min_age,max_age)
        else:
            results = cursor.get_results_by_age(min_age,max_age,illness=illness)
        return results

    def get_results_by_month(month, illness=None):
        cursor = InfectedDAO.InfectedDAO
        if not illness:
            results = cursor.get_results_by_month(month)
        else:
            results = cursor.get_results_by_month(month,illness=illness)
        return results

    def get_results_by_year(year, illness=None):
        cursor = InfectedDAO.InfectedDAO
        if not illness:
            results = cursor.get_results_by_year(year)
        else:
            results = cursor.get_results_by_year(year,illness=illness)
        return results

    @staticmethod
    def add_infected(cid, count, checkup, infname):
        InfectedDAO.InfectedDAO.add_infected(cid, count, checkup, infname)

        search = RecoveredDAO.RecoveredDAO.find_recovered(cid,infname)

        if search:
            RecoveredDAO.RecoveredDAO.delete_recovered(cid, infname)
