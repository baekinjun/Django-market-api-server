from flask import Blueprint, request
from flask_restful import Api
from .urls import url_patterns

laboratory_page_api = Blueprint('laboratory_page_api', __name__, url_prefix='/api_v1/laboratory')
api = Api(laboratory_page_api)

for vi_class, route in url_patterns:
    api.add_resource(vi_class, route)
