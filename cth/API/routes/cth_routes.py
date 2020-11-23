from flask import request, make_response, render_template
import requests
from cth.API.handler.CitizenHandler import CitizenHandler
from cth.API.handler.InfectedHandler import InfectedHandler
from cth.API.handler.TestHandler import TestHandler
from cth import db
from cth.models import Institution, Operator, Citizen, Test, Infected, Recovered, Illness
from cth.DB.DAO import OperatorDAO
from flask import jsonify
import json
import jwt
from cth.API.validation.form_validation import FormValidation
oid = 0

'''
Place routes here as basic python function.
'''
def get_global_results():
    return InfectedHandler.get_global_results()


def get_results_by_municipality(municipality, illness):
    return InfectedHandler.get_results_by_municapility(municipality, illness)

def get_results_by_sex(sex, illness):
    return CitizenHandler.get_results_by_sex(sex, illness)

def get_results_by_age(min_age, max_age, illness):
    if max_age < min_age:
        return make_response("Max age cannot be less than the minimum age.", 400)

    return CitizenHandler.get_results_by_age(min_age, max_age, illness)

def operator_login():
    operator = request.json
    oid = operator['oid']
    firstname = OperatorDAO.OperatorDAO.findOperator(operator["username"],operator["password"])
    if firstname!= None:
        token = jwt.encode({'username': operator['username'], 'password': operator['password'], 'exp': 31556926}, 'secret')
        payload = {'token': 'Bearer ' + str(token) , 'success': True}
        return payload
    else:
        payload = make_response(jsonify({"message": "User not found"}), 400)
        return payload

def input_form():

    form = request.json
    form = {'firstname':'Guillermo', 'lastname':'Betancourt', 'date_of_birth':'01/28/1998','sex':'M','phone':'787-459-3698','ssn':'123-45-6789','ishp': True,'is_positive':True,'timestamp':'11/22/2020','institution_name':'Perea','illness':'COVID-19','address':'Mayaguez 00680' }
    fv = FormValidation()

    result = fv.validate_all_functions(form)

    if len(result) == 0:
        cid = CitizenHandler.add_citizen(form['firstname'],form['lastname'],form['date_of_birth'],form['sex'],form['address'],form['phone'],form['ssn'],form['ishp'],form['is_positive'],form['illness'],form['timestamp'])
        tid = TestHandler.add_test(form['timestamp'], form['is_positive'], form['institution_name'], form['illness'],cid)
        return make_response("",200)

    else:
        payload = make_response(jsonify(error = result), 400)
        return payload
