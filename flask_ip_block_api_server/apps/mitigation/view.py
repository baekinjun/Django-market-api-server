from flask_restful import Resource
from .service import MitigationPageService
from .schema import (FirewallIpBlockSetSchema, FirewallIpBlockDeleteSchema, ValidationError, LimitOffsetSchema,
                     IpDefinitionWhiteListSetSchema, IpAddressSchema, BlockHistorySchema, WhiteListDeleteSchema,
                     ConfigurationSchema, FwIDSchema)
from core.handler import ResponseHandler
from http import HTTPStatus
from flask import request
from flasgger import swag_from

mitigation_page_service = MitigationPageService()


class FirewallActive(Resource):
    @swag_from('swagger_doc/firewall_active.yaml', methods=['GET'])
    def get(self):
        try:
            page = LimitOffsetSchema(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())
        res = mitigation_page_service.firewall_active(page.limit, page.offset)
        return ResponseHandler(HTTPStatus.OK).payload(res)


class FirewallBlockIpAll(Resource):
    @swag_from('swagger_doc/firewall_block_ip_all.yaml', methods=['GET'])
    def get(self):
        try:
            page = LimitOffsetSchema(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())
        res = mitigation_page_service.firewall_block_ip_all(page.limit, page.offset)
        return ResponseHandler(HTTPStatus.OK).payload(res)

    @swag_from('swagger_doc/firewall_ip_block_set.yaml', methods=['POST'])
    def post(self):
        try:
            block_ip_set = FirewallIpBlockSetSchema(**request.form.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.firewall_ip_block_set(block_ip_set.fw_id, block_ip_set.fw_name,
                                                            block_ip_set.group_name, block_ip_set.ip_address,
                                                            block_ip_set.requirement_user)
        if res == -1:
            return ResponseHandler(HTTPStatus.FORBIDDEN).response()
        elif res['@o_out_code'] == 1:
            return ResponseHandler(HTTPStatus.CREATED).response()
        else:
            return ResponseHandler(HTTPStatus.INTERNAL_SERVER_ERROR).response()

    @swag_from('swagger_doc/firewall_ip_block_delete.yaml', methods=['DELETE'])
    def delete(self):
        try:
            block_ip_set = FirewallIpBlockDeleteSchema(**request.form.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.firewall_ip_block_delete(block_ip_set.fw_name,
                                                               block_ip_set.group_name, block_ip_set.ip_address,
                                                               block_ip_set.requirement_user)
        if res['@o_out_code'] == 2:
            return ResponseHandler(HTTPStatus.CREATED).response()
        else:
            return ResponseHandler(HTTPStatus.INTERNAL_SERVER_ERROR).response()


class IpDefinition(Resource):
    @swag_from('swagger_doc/ip_address_definition_list.yaml', methods=['GET'])
    def get(self):
        try:
            page = LimitOffsetSchema(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())
        res = mitigation_page_service.ip_address_definition_list(page.keyword, page.limit, page.offset)
        return ResponseHandler(HTTPStatus.OK).payload(res)

    @swag_from('swagger_doc/ip_address_definition_create.yaml', methods=['POST'])
    def post(self):
        try:
            ip_set = IpDefinitionWhiteListSetSchema(**request.form.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.ip_address_definition_create(ip_set.name, ip_set.description, ip_set.ip_address)

        if res:
            return ResponseHandler(HTTPStatus.BAD_REQUEST).response()
        else:
            return ResponseHandler(HTTPStatus.CREATED).response()

    @swag_from('swagger_doc/ip_address_definition_update.yaml', methods=['PUT'])
    def put(self):
        try:
            ip_set = IpDefinitionWhiteListSetSchema(**request.form.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.ip_address_definition_update(ip_set.name, ip_set.description, ip_set.ip_address)
        if res:
            return ResponseHandler(HTTPStatus.BAD_REQUEST).response()
        else:
            return ResponseHandler(HTTPStatus.CREATED).response()

    @swag_from('swagger_doc/ip_address_definition_delete.yaml', methods=['DELETE'])
    def delete(self):
        try:
            ip_set = IpAddressSchema(**request.json).ip_address
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.ip_address_definition_delete(ip_set)
        if res:
            return ResponseHandler(HTTPStatus.BAD_REQUEST).response()
        else:
            return ResponseHandler(HTTPStatus.CREATED).response()


class BlockHistory(Resource):
    @swag_from('swagger_doc/firewall_block_history.yaml', methods=['GET'])
    def get(self):
        try:
            block_history = BlockHistorySchema(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.firewall_block_history(block_history.category, block_history.keyword,
                                                             block_history.offset, block_history.limit)
        return ResponseHandler(HTTPStatus.OK).payload(res)


class FirewallWhiteList(Resource):
    @swag_from('swagger_doc/firewall_white_list.yaml', methods=['GET'])
    def get(self):
        try:
            page = LimitOffsetSchema(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.firewall_white_list(page.keyword, page.limit, page.offset)

        return ResponseHandler(HTTPStatus.OK).payload(res)

    @swag_from('swagger_doc/firewall_white_list_set.yaml', methods=['POST'])
    def post(self):
        try:
            white_set = IpDefinitionWhiteListSetSchema(**request.form.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.firewall_white_list_set(white_set.name, white_set.ip_address,
                                                              white_set.description)
        if res['@o_out_code'] == 1:
            return ResponseHandler(HTTPStatus.CREATED).response()
        else:
            return ResponseHandler(HTTPStatus.INTERNAL_SERVER_ERROR).response()

    @swag_from('swagger_doc/firewall_white_list_set.yaml', methods=['PUT'])
    def put(self):
        try:
            white_set = IpDefinitionWhiteListSetSchema(**request.form.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.firewall_white_list_set(white_set.name, white_set.ip_address,
                                                              white_set.description)
        if res['@o_out_code'] == 1:
            return ResponseHandler(HTTPStatus.CREATED).response()
        else:
            return ResponseHandler(HTTPStatus.INTERNAL_SERVER_ERROR).response()

    def delete(self):
        try:
            data = WhiteListDeleteSchema(**request.json).data
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.firewall_white_list_delete(data)
        if res:
            return ResponseHandler(HTTPStatus.CREATED).response()
        else:
            return ResponseHandler(HTTPStatus.BAD_REQUEST).response()


class ConfigurationView(Resource):
    @swag_from('swagger_doc/firewall_configuration_list.yaml', methods=['GET'])
    def get(self):
        try:
            page = LimitOffsetSchema(**request.args.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())
        res = mitigation_page_service.firewall_configuration_list(page.limit, page.offset)
        return ResponseHandler(HTTPStatus.OK).payload(res)

    @swag_from('swagger_doc/firewall_configuration_set.yaml', methods=['POST'])
    def post(self):
        try:
            configuration = ConfigurationSchema(**request.form.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.firewall_configuration_set(configuration.dict())
        return ResponseHandler(HTTPStatus.CREATED).response()

    @swag_from('swagger_doc/firewall_configuration_update.yaml', methods=['PUT'])
    def put(self):
        try:
            FwIDSchema(**request.form.to_dict())
            configuration = ConfigurationSchema(**request.form.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.firewall_configuration_set(configuration.dict())
        return ResponseHandler(HTTPStatus.CREATED).response()

    @swag_from('swagger_doc/firewall_configuration_delete.yaml', methods=['DELETE'])
    def delete(self):
        try:
            FwIDSchema(**request.form.to_dict())
            configuration = ConfigurationSchema(**request.form.to_dict())
        except ValidationError as v:
            return ResponseHandler(HTTPStatus.PRECONDITION_FAILED).validator_response(v.json())

        res = mitigation_page_service.firewall_configuration_delete(configuration.dict())
        return ResponseHandler(HTTPStatus.CREATED).response()


class ConfigurationTotalView(Resource):
    @swag_from('swagger_doc/firewall_configuration_total.yaml', methods=['GET'])
    def get(self):
        res = mitigation_page_service.firewall_configuration_total()['count']
        return ResponseHandler(HTTPStatus.OK).payload(res)
