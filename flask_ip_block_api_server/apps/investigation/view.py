from http import HTTPStatus

from flasgger import swag_from
from flask import request
from flask_restful import Resource

from core.handler import ResponseHandler
from .schema import IpAddressSchema, ValidationError, MaltegoSchema
from .service import InvestigationPageService

investigation_page_service = InvestigationPageService()


class WordCloudView(Resource):
    @swag_from('swagger_doc/word_cloud.yaml', methods=['GET'])
    def get(self):
        try:
            ip_address = IpAddressSchema(**request.args.to_dict()).ip_address
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())
        res = investigation_page_service.word_cloud(ip_address)

        return ResponseHandler(HTTPStatus.OK).payload(res)


class SearchChartView(Resource):
    @swag_from('swagger_doc/search_chart.yaml', methods=['GET'])
    def get(self):
        res = investigation_page_service.search_chart()
        return ResponseHandler(HTTPStatus.OK).payload(res)


class MaltegoInView(Resource):
    @swag_from('swagger_doc/sp_intel_ip_in.yaml', methods=['GET'])
    def get(self):
        try:
            maltego = MaltegoSchema(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())
        res = investigation_page_service.sp_intel_ip_in(maltego.ip_address, maltego.count, maltego.now)
        return ResponseHandler(HTTPStatus.OK).payload(res)


class MaltegoOutView(Resource):
    @swag_from('swagger_doc/sp_intel_ip_out.yaml', methods=['GET'])
    def get(self):
        try:
            maltego = MaltegoSchema(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())
        res = investigation_page_service.sp_intel_ip_out(maltego.ip_address, maltego.count, maltego.now)
        return ResponseHandler(HTTPStatus.OK).payload(res)
