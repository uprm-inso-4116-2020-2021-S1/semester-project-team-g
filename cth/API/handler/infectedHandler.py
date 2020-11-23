from cth.DB.DAO import InfectedDAO
class InfectedHandler:

    def get_global_results():

        cursor = InfectedDAO.InfectedDAO

        results = cursor.get_global_results()

        return results

    def get_results_by_municipality(municipality, illness=None):
        if not illness:
            cursor = InfectedDAO.InfectedDAO
            results = cursor.get_results_by_municipality(municipality)
        else:
            results = cursor.get_results_by_municipality(municipality, illness=illness)
        return results

    def get_results_by_sex(sex, illness=None):
        if not illness:
            cursor = InfectedDAO.InfectedDAO
            results = cursor.get_results_by_sex(sex)
        else:
            results = cursor.get_results_by_sex(sex, illness=illness)
        return results

    def get_results_by_age(min_age, max_age, illness=None):
        if not illness:
            cursor = InfectedDAO.InfectedDAO
            results = cursor.get_results_by_age(min_age,max_age)
        else:
            results = cursor.get_results_by_municipality(min_age,max_age, illness=illness)
        return results

    def add_infected(cid,count, checkup ,date,infname):
        cursor = InfectedDAO.InfectedDAO
        cursor.add_infected(cid,count, checkup ,date,infname)
