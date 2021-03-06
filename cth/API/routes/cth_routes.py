from flask import request, make_response, render_template
import requests
from cth.API.handler import CitizenHandler
from cth.API.handler import InfectedHandler
from cth.API.handler import RecoveredHandler
from cth.API.handler import TestHandler
from cth import db
from cth.models import Institution, Operator, Citizen, Test, Infected, Recovered, Illness
from cth.DB.DAO import OperatorDAO, RecoveredDAO
from cth.DB.DAO import InfectedDAO
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

def get_global_recovered_results():
    return RecoveredHandler.RecoveredHandler.get_global_results()

def get_results_by_municipality(municipality, illness=None):
    return InfectedHandler.InfectedHandler.get_results_by_municipality(municipality,illness)

def get_recovered_results_by_municipality(municipality, illness = None):
    return RecoveredHandler.RecoveredHandler.get_results_by_municipality(municipality, illness)

def get_results_by_sex(sex, illness):
    return InfectedHandler.InfectedHandler.get_results_by_sex(sex, illness)

def get_recovered_results_by_sex(sex,illness):
    return RecoveredHandler.RecoveredHandler.get_results_by_sex(sex,illness)

def get_results_by_age(min_age, max_age, illness):
    if int(max_age) < int(min_age):
        return make_response(jsonify({"age": "The minimum age cannot be larger than the maximum age."}), 400)

    return InfectedHandler.InfectedHandler.get_results_by_age(min_age, max_age, illness)

def get_recovered_results_by_age(min_age,max_age,illness):
    if int(max_age) < int(min_age):
        return make_response(jsonify({"age": "The minimum age cannot be larger than the maximum age."}), 400)

    return RecoveredHandler.RecoveredHandler.get_results_by_age(min_age,max_age,illness)


def get_results_by_month(month, illness):
    return InfectedHandler.InfectedHandler.get_results_by_month(month, illness)

def get_recovered_results_by_month(month, illness):
    return RecoveredHandler.RecoveredHandler.get_results_by_month(month, illness)

def get_results_by_year(year, illness):
    return InfectedHandler.InfectedHandler.get_results_by_year(year, illness)

def get_recovered_results_by_year(year,illness):
    return RecoveredHandler.RecoveredHandler.get_results_by_year(year,illness)


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
                                                        form['sex'], form['address'], form['phone'], form['ssn'], form['email'],
                                                        form['ishp'])

        if cid:
            tid = TestHandler.TestHandler.add_test(form['illness'], form['is_positive'],form['institution_name'], cid, form['oid'])
            InfectedHandler.InfectedHandler.add_infected(cid,1,'14',form['illness'])
            return make_response(jsonify({"message": "Submission was successful"}), 200)


    else:
        payload = make_response(jsonify(result), 400)
        return payload



def add_test():
    form = request.json
    fv = FormValidation()

    result = fv.validate_test(form)

    if len(result) == 0:
        tid = TestHandler.TestHandler.add_new_test(form['illness'],form['is_positive'],form['institution_name'],form['oid'],form['ssn'])
        if tid != 1:
             return make_response(tid,400)

        else:
            return make_response(jsonify({"message": "Submission was successful"}), 200)
    else:
        return make_response(jsonify(result), 400)





def update_citizen():

    form = request.json
    fv = FormValidation()

    result = fv.validate_citizen(form)

    if len(result) == 0:
        cid = CitizenHandler.CitizenHandler.update_citizen(form['firstname'], form['lastname'], form['date_of_birth'], form['sex'], form['address'], form['phone'], form['ssn'], form['email'], form['ishp'])

        if cid == -1:
            return make_response(jsonify({"message": "User not found"}), 400)

        else:
            return make_response(jsonify({"message": "Submission was successful"}), 200)

    else:
        payload = make_response(jsonify(result), 400)
        return payload
