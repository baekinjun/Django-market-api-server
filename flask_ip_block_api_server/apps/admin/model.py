from core.db import Procedure


class AdminPageDao:
    def __init__(self):
        self.conn_s = Procedure()

    def daily_usage_criminal_ip(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('daily_usage_criminalip');"""
        )

    def daily_usage_trace(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('daily_usage_trace');"""
        )

    def daily_busted_detection(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('daily_busted_detection');"""
        )

    def daily_busted_violation(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('daily_busted_violation');"""
        )

    def audit_category_list(self):
        return self.conn_s.b_fetchall(
            """SELECT process FROM general_action_description group by process;"""
        )

    def audit_log_list(self, args):
        return self.conn_s.b_fetchall(
            """CALL sp_general_log_list_select(%s,%s,%s,%s);""", args
        )

    def admin_registration_list_all(self):
        return self.conn_s.b_fetchall(
            """SELECT id,name,last_access_dtime,reg_dtime FROM admin where is_enabled = 1;"""
        )

    def admin_registration_list_search(self, args):
        return self.conn_s.b_fetchall(
            """SELECT id,name,last_access_dtime,reg_dtime FROM admin where is_enabled = 1 and (id LIKE %s or name LIKE %s);""",
            args
        )
