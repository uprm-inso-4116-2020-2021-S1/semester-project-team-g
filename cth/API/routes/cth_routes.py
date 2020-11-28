from flask import request, make_response, render_template
import requests
from cth.API.handler import CitizenHandler
from cth.API.handler import InfectedHandler
from cth.API.handler import TestHandler
from cth import db
from cth.models import Institution, Operator, Citizen, Test, Infected, Recovered, Illness
from cth.DB.DAO import OperatorDAO
from flask import jsonify
import json
import jwt
from datetime import datetime, timedelta
from cth.API.validation.form_validation import FormValidation


'''
Place routes here as basic python function.
'''
def get_global_results():
    return InfectedHandler.InfectedHandler.get_global_results()


def get_results_by_municipality(municipality, illness):
    return InfectedHandler.InfectedHandler.get_results_by_municipality(municipality,illness)

def get_results_by_sex(sex, illness):
    return CitizenHandler.CitizenHandler.get_results_by_sex(sex, illness)

def get_results_by_age(min_age, max_age, illness):
    if max_age < min_age:
        return make_response("Max age cannot be less than the minimum age.", 400)

    return CitizenHandler.CitizenHandler.get_results_by_age(min_age, max_age, illness)

def get_results_by_month(month, illness):
    return CitizenHandler.CitizenHandler.get_results_by_month(month, illness)

def get_results_by_year(year, illness):
    return CitizenHandler.CitizenHandler.get_results_by_year(year, illness)


def operator_login():
    operator = request.json
    # oid = operator['oid']
    firstname, oid = OperatorDAO.OperatorDAO.findOperator(operator["username"], operator["password"])
    if firstname and oid:
        token = jwt.encode({'username': operator['username'], 'password': operator['password'], 'exp': datetime.utcnow() + timedelta(minutes=60)}, 'secret')
        payload = {'token': 'Bearer ' + str(token), 'success': True, 'oid': oid}
        return payload
    else:
        payload = make_response(jsonify({"message": "User not found"}), 400)
        return payload


def input_form():
    form = request.json
    fv = FormValidation()
    result = fv.validate_all_functions(form)
    if len(result) == 0:
        cid = CitizenHandler.CitizenHandler.add_citizen(form['firstname'], form['lastname'], form['date_of_birth'],
                                                        form['sex'], form['address'], form['phone'], form['ssn'],
                                                        form['ishp'], form['is_positive'], form['illness']
                                                        )
        tid = TestHandler.TestHandler.add_test(form['illness'], form['is_positive'],
                                               form['institution_name'], cid, form['oid']
                                               )
        return make_response(jsonify({"message": "Submission was successful"}), 200)
    else:
        payload = make_response(jsonify(result), 400)
        return payload
