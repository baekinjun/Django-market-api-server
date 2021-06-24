from flask_restful import Resource
from .service import AdminPageService
from .schema import AuditLogSchema, AdminRegisterSchema, ValidationError
from core.handler import ResponseHandler
from http import HTTPStatus
from flask import request
from flasgger import swag_from

admin_page_service = AdminPageService()


class DailyUsageCriminalIp(Resource):
    @swag_from('swagger_doc/daily_usage_criminal_ip.yaml', methods=['GET'])
    def get(self):
        res = admin_page_service.daily_usage_criminal_ip()
        return ResponseHandler(HTTPStatus.OK).payload(res)


class DailyUsageTrace(Resource):
    @swag_from('swagger_doc/daily_usage_trace.yaml', methods=['GET'])
    def get(self):
        res = admin_page_service.daily_usage_trace()
        return ResponseHandler(HTTPStatus.OK).payload(res)


class DailyBustedDetection(Resource):
    @swag_from('swagger_doc/daily_busted_detection.yaml', methods=['GET'])
    def get(self):
        res = admin_page_service.daily_busted_detection()
        return ResponseHandler(HTTPStatus.OK).payload(res)


class DailyBustedViolation(Resource):
    @swag_from('swagger_doc/daily_busted_violation.yaml', methods=['GET'])
    def get(self):
        res = admin_page_service.daily_busted_violation()
        return ResponseHandler(HTTPStatus.OK).payload(res)


class AuditCategoryList(Resource):
    @swag_from('swagger_doc/audit_category_list.yaml', methods=['GET'])
    def get(self):
        res = admin_page_service.audit_category_list()
        return res


class AuditLogList(Resource):
    @swag_from('swagger_doc/audit_log_list.yaml', methods=['GET'])
    def get(self):
        try:
            audit_dao = AuditLogSchema(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED)

        res = admin_page_service.audit_log_list(audit_dao.offset, audit_dao.limit, audit_dao.category,
                                                audit_dao.keyword)
        return ResponseHandler(HTTPStatus.OK).payload(res)


class AdminRegisterList(Resource):
    @swag_from('swagger_doc/admin_registration_list.yaml', methods=['GET'])
    def get(self):
        try:
            keyword = AdminRegisterSchema(**request.args.to_dict()).keyword
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED)
        res = admin_page_service.admin_registration_list(keyword)
        return ResponseHandler(HTTPStatus.OK).payload(res)
