from flask_restful import Resource
from .service import MainPageService
from core.handler import ResponseHandler
from http import HTTPStatus
from flasgger import swag_from

main_page_service = MainPageService()


class DetectionTrafficView(Resource):
    @swag_from('swagger_doc/DetectionTraffic.yaml', methods=['GET'])
    def get(self):
        res = main_page_service.detection_traffic_score()
        if res:
            return ResponseHandler(HTTPStatus.OK).payload(res)
        else:
            return ResponseHandler(HTTPStatus.BAD_REQUEST)


class ViolationTrafficScoreView(Resource):
    @swag_from('swagger_doc/violation_traffic_score.yaml', methods=['GET'])
    def get(self):
        res = main_page_service.violation_traffic_score()
        if res:
            return ResponseHandler(HTTPStatus.OK).payload(res)
        else:
            return ResponseHandler(HTTPStatus.BAD_REQUEST)


class IpDefinitionTotal(Resource):
    @swag_from('swagger_doc/ip_definition_total.yaml', methods=['GET'])
    def get(self):
        res = main_page_service.ip_definition_total()
        return ResponseHandler(HTTPStatus.OK).payload(res)


class MainSummarySelect(Resource):
    @swag_from('swagger_doc/main_summary_select.yaml', methods=['GET'])
    def get(self):
        res = main_page_service.main_summary_select()
        return ResponseHandler(HTTPStatus.OK).payload(res)


class FireWallPossible(Resource):
    @swag_from('swagger_doc/firewall_possible.yaml', methods=['GET'])
    def get(self):
        res = main_page_service.firewall_possible()
        return ResponseHandler(HTTPStatus.OK).payload(res)
