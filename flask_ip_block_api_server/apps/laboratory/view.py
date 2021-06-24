from flask_restful import Resource
from .service import LaboratoryPageService
from .schema import LabIDSchema, ValidationError
from core.handler import ResponseHandler
from http import HTTPStatus
from flask import request
from flasgger import swag_from

laboratory_page_service = LaboratoryPageService()


class LabTitleView(Resource):
    @swag_from('swagger_doc/lab_title.yaml', methods=['GET'])
    def get(self):
        try:
            id = LabIDSchema(**request.args.to_dict()).id
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = laboratory_page_service.lab_title(id)
        return ResponseHandler(HTTPStatus.OK).payload(res)


class LabDataView(Resource):
    @swag_from('swagger_doc/lab_data.yaml', methods=['GET'])
    def get(self):
        try:
            id = LabIDSchema(**request.args.to_dict()).id
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = laboratory_page_service.lab_data(id)
        return ResponseHandler(HTTPStatus.OK).payload(res)
