from .model import AdminPageDao


class AdminPageService:
    def __init__(self):
        self.admin_page_dao = AdminPageDao()

    def daily_usage_criminal_ip(self):
        res = self.admin_page_dao.daily_usage_criminal_ip()
        return res

    def daily_usage_trace(self):
        res = self.admin_page_dao.daily_usage_trace()
        return res

    def daily_busted_detection(self):
        res = self.admin_page_dao.daily_busted_detection()
        return res

    def daily_busted_violation(self):
        res = self.admin_page_dao.daily_busted_violation()
        return res

    def audit_category_list(self):
        res = self.admin_page_dao.audit_category_list()
        return res

    def audit_log_list(self, offset, limit, category, keyword):
        res = self.admin_page_dao.audit_log_list((category, keyword, offset, limit))
        return res

    def admin_registration_list(self, keyword):
        if keyword:
            args = ('%%' + keyword + '%%', '%%' + keyword + '%%')
            res = self.admin_page_dao.admin_registration_list_search(args)
        else:
            res = self.admin_page_dao.admin_registration_list_all()

        return res
