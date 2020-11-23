from flask import request, make_response, render_template
import requests
from cth.API.handler.CitizenHandler import CitizenHandler
from cth.API.handler.infectedHandler import InfectedHandler
from cth import db
from cth.models import Institution, Operator, Citizen, Test, Infected, Recovered, Illness
from cth.DB.DAO import OperatorDAO
from flask import jsonify
import json
import jwt
oid = 0

'''
Place routes here as basic python function.
'''
def get_global_results():
    return InfectedHandler.get_global_results()


def get_results_by_municipality(municipality, illness):
    return CitizenHandler.get_results_by_municapility(municipality, illness)

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

    forum = request.json
    fv = FormValidation()

    result = fv.validate_all_functions(forum)

    if len(result) == 0:
        cid = CitizenHandler.add_citizen(forum['firstname'],forum['lastname'],forum['date_of_birth'],forum['sex'],forum['phone'],forum['ssn'],forum['ishp'],forum['is_positive'])
        tid = TestHandler.add_test(forum['timestamp'], forum['is_positive'], forum['location'], forum['illness'])
        return make_response("",200)

    else:
        payload = make_response(jsonify(error = result), 400)
        return payload
