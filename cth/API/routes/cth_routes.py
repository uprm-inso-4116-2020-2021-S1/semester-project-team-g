from flask import request, make_response, render_template
import requests
from cth.API.handler.CitizenHandler import CitizenHandler
from cth import db
from cth.models import Institution, Operator, Citizen, Test, Infected, Recovered, Illness
from cth.DB.DAO import OperatorDAO
from flask import jsonify
import json

'''
Place routes here as basic python function.
'''
def get_global_results():
    results = db.session.query(Institution).all()
    for r in results:
        return r.instname

def get_results_by_municipality(municipality, illness):
    return CitizenHandler.get_results_by_municapility(municipality, illness)

def get_results_by_sex(sex, illness):
    return CitizenHandler.get_results_by_sex(sex, illness)

def get_results_by_age(min_age, max_age, illness):
    if max_age < min_age:
        return make_response("Max age cannot be less than the minimum age.", 400)

    return CitizenHandler.get_results_by_age(min_age, max_age, illness)

def operator_login(data):
    operator = json.load(data)
    firstname = OperatorDAO.OperatorDAO.findOperator(operator["username"],operator["password"])
    return jsonify(isOperator=True) if firstname!= None else jsonify(isOperator=False)