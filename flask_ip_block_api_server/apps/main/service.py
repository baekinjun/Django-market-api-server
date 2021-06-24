from .model import MainPageDao


class MainPageService:
    def __init__(self):
        self.main_page_dao = MainPageDao()

    def detection_traffic_score(self):
        detection = 0
        trace_log = 0

        black_type = self.main_page_dao.score_dst_ip_blacktype()
        if black_type != None:
            detection += sum(list(map(lambda x: x['data_cnt'], black_type)))

        vuln = self.main_page_dao.score_dst_ip_vulnerability()
        if vuln != None:
            detection += sum(list(map(lambda x: x['data_cnt'], vuln)))

        suspicous = self.main_page_dao.score_dst_ip_suspicious_cert()
        if suspicous != None:
            detection += sum(list(map(lambda x: x['data_cnt'], suspicous)))

        trace_log += sum(list(map(lambda x: x['data_cnt'], self.main_page_dao.score_dst_ip_all())))

        if detection:
            percent = detection / trace_log * 100
            if 0 < percent < 0.5:
                return 1
            elif 0.5 <= percent < 1:
                return 2
            else:
                return 3
        else:
            return 0

    def violation_traffic_score(self):
        violation = 0
        trace_log = sum(list(map(lambda x: x['data_cnt'], self.main_page_dao.score_dst_ip_all())))

        vpn = self.main_page_dao.score_dst_ip_vpn()
        if vpn != None:
            violation += sum(list(map(lambda x: x['data_cnt'], vpn)))

        tor = self.main_page_dao.score_dst_ip_tor()
        if tor != None:
            violation += sum(list(map(lambda x: x['data_cnt'], tor)))

        dns = self.main_page_dao.score_dst_ip_dns()
        if dns != None:
            violation += sum(list(map(lambda x: x['data_cnt'], dns)))

        proxy = self.main_page_dao.score_dst_ip_proxy()
        if proxy != None:
            violation += sum(list(map(lambda x: x['data_cnt'], proxy)))

        chinese = self.main_page_dao.score_dst_ip_chinese()
        if chinese != None:
            violation += sum(list(map(lambda x: x['data_cnt'], chinese)))

        suspicious_net = self.main_page_dao.score_dst_ip_suspicious_nat()
        if suspicious_net != None:
            violation += sum(list(map(lambda x: x['data_cnt'], suspicious_net)))

        remote_access = self.main_page_dao.score_dst_ip_remote_access()
        if remote_access != None:
            violation += sum(list(map(lambda x: x['data_cnt'], remote_access)))

        dbconnect = self.main_page_dao.score_dst_ip_dbconnect()
        if dbconnect != None:
            violation += sum(list(map(lambda x: x['data_cnt'], dbconnect)))

        snmp = self.main_page_dao.score_dst_ip_snmp()
        if snmp != None:
            violation += sum(list(map(lambda x: x['data_cnt'], snmp)))

        icmp = self.main_page_dao.score_dst_ip_icmp()
        if icmp != None:
            violation += sum(list(map(lambda x: x['data_cnt'], icmp)))

        blocked_policy = self.main_page_dao.score_dst_ip_blocked_policy()
        if blocked_policy != None:
            violation += sum(list(map(lambda x: x['data_cnt'], blocked_policy)))

        if violation:
            percent = violation / trace_log * 100
            if 0 < percent < 33:
                return 1
            elif 33 <= percent < 66:
                return 2
            else:
                return 3

        else:
            return 0

    def ip_definition_total(self):
        return self.main_page_dao.ip_definition_count()['count']

    def main_summary_select(self):
        return self.main_page_dao.main_summary_select()

    def firewall_possible(self):
        return self.main_page_dao.firewall_possible()
