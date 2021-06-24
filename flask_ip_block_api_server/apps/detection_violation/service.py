from .model import DetectionViolationPageDao


class DetectionViolationPageService:
    def __init__(self):
        self.detection_page_dao = DetectionViolationPageDao()

    def detection_violation_page_statistics(self, page_type):
        res = {
            'score_dst_ip': self.detection_page_dao.score_dst_ip(page_type),
            'top_dst_ip': self.detection_page_dao.top_dst_ip(page_type),
            'top_dst_port': self.detection_page_dao.top_dst_port(page_type),
            'top_protocol': self.detection_page_dao.top_protocol(page_type),
            'top_src_ip': self.detection_page_dao.top_src_ip(page_type),
            'top_src_port': self.detection_page_dao.top_src_port(page_type)
        }
        return res
