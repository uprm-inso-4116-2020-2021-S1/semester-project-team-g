from flask import request, make_response, render_template
import requests
'''
Place routes here as basic python function.
'''
def dummy():
    request.form['payload']