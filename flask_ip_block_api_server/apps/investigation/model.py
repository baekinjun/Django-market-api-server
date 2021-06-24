from core.db import Procedure
from datetime import datetime


class InvestigationPageDao:
    def __init__(self):
        self.conn_s = Procedure()

    def word_cloud(self, args):
        return self.conn_s.b_fetchall(
            """call sp_analyze_source_ip(%s)""", args
        )

    def score_dst_ip(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_all');"""
        )

    def sp_intel_ip_in(self, args):
        return self.conn_s.b_fetchall(
            """call sp_intel_ip_in(%s,%s,%s,%s);""", args
        )

    def sp_intel_ip_out(self, args):
        return self.conn_s.b_fetchall(
            """call sp_intel_ip_out(%s,%s,%s,%s);""", args
        )
