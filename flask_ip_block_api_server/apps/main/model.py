from core.db import Procedure


class MainPageDao:
    def __init__(self):
        self.conn_s = Procedure()

    def score_dst_ip_blacktype(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_blacktype');"""
        )

    def score_dst_ip_vulnerability(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_vulnerability');"""
        )

    def score_dst_ip_suspicious_cert(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_suspicious_cert');"""
        )

    def score_dst_ip_all(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_all');"""
        )

    def score_dst_ip_vpn(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_vpn');"""
        )

    def score_dst_ip_tor(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_tor');"""
        )

    def score_dst_ip_dns(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_dns');"""
        )

    def score_dst_ip_proxy(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_proxy');"""
        )

    def score_dst_ip_chinese(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_chinese');"""
        )

    def score_dst_ip_suspicious_nat(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_suspicious_nat');"""
        )

    def score_dst_ip_remote_access(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_remote_access');"""
        )

    def score_dst_ip_dbconnect(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_dbconnect');"""
        )

    def score_dst_ip_snmp(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_snmp');"""
        )

    def score_dst_ip_icmp(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_icmp');"""
        )

    def score_dst_ip_blocked_policy(self):
        return self.conn_s.b_fetchall(
            """call sp_stat_select('score_dst_ip_blocked_policy');"""
        )

    def ip_definition_count(self):
        return self.conn_s.b_fetchone(
            """SELECT COUNT(*) as count FROM ip_address_definition;"""
        )

    def main_summary_select(self):
        return self.conn_s.b_fetchone(
            """call sp_main_summary_select();"""
        )

    def firewall_possible(self):
        return self.conn_s.b_fetchall(
            """SELECT fw_type, activate_code FROM firewall_info;"""
        )
