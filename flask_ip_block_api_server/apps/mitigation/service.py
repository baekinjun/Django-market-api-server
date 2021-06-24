from .model import MitigationPageDao


class MitigationPageService:
    def __init__(self):
        self.mitigation_page_dao = MitigationPageDao()

    def firewall_active(self, limit, offset):
        res = self.mitigation_page_dao.firewall_active((limit, offset))
        return res

    def firewall_block_ip_all(self, limit, offset):
        res = self.mitigation_page_dao.firewall_block_ip_all((limit, offset))
        return res

    def firewall_ip_block_set(self, fw_id, fw_name, group_name, ip_address, requirement_user):
        check_white = self.mitigation_page_dao.check_white_list((fw_id, ip_address))
        if check_white:
            return -1
        res = self.mitigation_page_dao.firewall_ip_block_set(
            (fw_name, group_name, ip_address, requirement_user))
        return res

    def firewall_ip_block_delete(self, fw_name, group_name, ip_address, requirement_user):
        res = self.mitigation_page_dao.firewall_ip_block_delete(
            (fw_name, group_name, ip_address, requirement_user))
        return res

    def ip_address_definition_list(self, keyword, limit, offset):
        if keyword:
            args = ('%%' + keyword + '%%', '%%' + keyword + '%%', '%%' + keyword + '%%', limit, offset)
            res = self.mitigation_page_dao.ip_address_definition_search(args)
        else:
            res = self.mitigation_page_dao.ip_address_definition_all((limit, offset))
        return res

    def ip_address_definition_update(self, name, description, ip_address):
        try:
            res = self.mitigation_page_dao.ip_address_definition_update((name, description, ip_address))
        except:
            return 1
        return res['@o_out_code']

    def ip_address_definition_create(self, name, description, ip_address):
        try:
            res = self.mitigation_page_dao.ip_address_definition_create((name, description, ip_address))
        except:
            return 1
        return res['@o_out_code']

    def ip_address_definition_delete(self, ip_address):
        try:
            res = self.mitigation_page_dao.ip_address_definition_delete(ip_address)
        except:
            return 1
        return res['@o_out_code']

    def firewall_block_history(self, category, keyword, offset, limit):
        res = self.mitigation_page_dao.firewall_block_history((category, keyword, offset, limit))
        return res

    def firewall_white_list(self, keyword, limit, offset):
        if keyword:
            args = ('%%' + keyword + '%%', '%%' + keyword + '%%', '%%' + keyword + '%%', limit, offset)
            res = self.mitigation_page_dao.firewall_white_list_search(args)
        else:
            res = self.mitigation_page_dao.firewall_white_list_all((limit, offset))

        return res

    def firewall_white_list_set(self, fw_name, ip_address, description):
        res = self.mitigation_page_dao.firewall_white_list_set((fw_name, ip_address, description))
        return res

    def firewall_white_list_delete(self, data):
        try:
            for set in data:
                res = self.mitigation_page_dao.firewall_white_list_delete(
                    (set['name'], set['ip_address'], set['description']))
        except Exception as e:
            return 0

        return 'success'

    def firewall_configuration_list(self, limit, offset):
        res = self.mitigation_page_dao.firewall_configuration_list((limit, offset))
        return res

    def firewall_configuration_set(self, kwargs):
        args = list(map(lambda arg: arg, kwargs.values()))
        res = self.mitigation_page_dao.firewall_configuration_set(args)
        return res

    def firewall_configuration_delete(self, kwargs):
        args = list(map(lambda arg: arg, kwargs.values()))
        res = self.mitigation_page_dao.firewall_configuration_delete(args)
        return res

    def firewall_configuration_total(self):
        res = self.mitigation_page_dao.firewall_configuration_total()
        return res
