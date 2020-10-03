from flask import request, make_response, render_template
import requests
from API.handler.CitizenHandler import CitizenHandler
'''
Place routes here as basic python function.
'''

def get_global_results():
    return CitizenHandler.get_global_results()

def get_results_by_municipality(municipality, illness):
    return CitizenHandler.get_results_by_municapility(municipality, illness)

def get_results_by_sex(sex, illness):
    return CitizenHandler.get_results_by_sex(sex, illness)

def get_results_by_age(min_age, max_age, illness):
    if max_age < min_age:
        return make_response("Max age cannot be less than the minimum age.", 400)

    return CitizenHandler.get_results_by_age(min_age, max_age, illness)