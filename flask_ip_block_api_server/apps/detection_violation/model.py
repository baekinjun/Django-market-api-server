from core.db import Procedure


class DetectionViolationPageDao:
    def __init__(self):
        self.conn_s = Procedure()

    def score_dst_ip(self, page_type):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_{}');""".format(page_type)
        )

    def top_dst_ip(self, page_type):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('top_dst_ip_is_{}');""".format(page_type)
        )

    def top_dst_port(self, page_type):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('top_dst_port_is_{}');""".format(page_type)
        )

    def top_protocol(self, page_type):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('top_protocol_is_{}');""".format(page_type)
        )

    def top_src_ip(self, page_type):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('top_src_ip_is_{}');""".format(page_type)
        )

    def top_src_port(self, page_type):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('top_src_port_is_{}');""".format(page_type)
        )
