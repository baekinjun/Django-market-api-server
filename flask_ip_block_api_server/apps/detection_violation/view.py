from flask_restful import Resource
from .service import DetectionViolationPageService
from .schema import (DetectionStaticsSchema, ValidationError, ViolationStaticsSchema)
from core.handler import ResponseHandler
from http import HTTPStatus
from flask import request
from flasgger import swag_from

detection_violation_page_service = DetectionViolationPageService()


class DetectionPageStatistics(Resource):
    @swag_from('swagger_doc/detection_page_statistics.yaml', methods=['GET'])
    def get(self):
        try:
            page_type = DetectionStaticsSchema(**request.args.to_dict()).page_type
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        try:
            res = detection_violation_page_service.detection_violation_page_statistics(page_type)
        except Exception as e:
            return ResponseHandler(HTTPStatus.BAD_REQUEST).validator_response(str(e))

        return ResponseHandler(HTTPStatus.OK).payload(res)


class ViolationPageStatistics(Resource):
    @swag_from('swagger_doc/violation_page_statistics.yaml', methods=['GET'])
    def get(self):
        try:
            page_type = ViolationStaticsSchema(**request.args.to_dict()).page_type
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        try:
            res = detection_violation_page_service.detection_violation_page_statistics(page_type)
        except Exception as e:
            return ResponseHandler(HTTPStatus.BAD_REQUEST).validator_response(str(e))

        return ResponseHandler(HTTPStatus.OK).payload(res)
