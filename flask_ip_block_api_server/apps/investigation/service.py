from .model import InvestigationPageDao
from datetime import datetime, timedelta


class InvestigationPageService:
    def __init__(self):
        self.investigation_page_dao = InvestigationPageDao()

    def word_cloud(self, ip_address):
        res = self.investigation_page_dao.word_cloud(ip_address)
        return res

    def search_chart(self):
        res = self.investigation_page_dao.score_dst_ip()
        return res

    def sp_intel_ip_in(self, ip_address, count, now):
        start_date = now - timedelta(days=1)

        res = self.investigation_page_dao.sp_intel_ip_in((ip_address, count, start_date, now))
        return res

    def sp_intel_ip_out(self, ip_address, count, now):
        now = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
        start_date = now - timedelta(days=1)

        res = self.investigation_page_dao.sp_intel_ip_out((ip_address, count, start_date, now))
        return res
