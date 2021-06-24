from .view import *

url_patterns = [
    (DetectionTrafficView, '/detection_traffic'),
    (ViolationTrafficScoreView, '/violation_traffic'),
    (IpDefinitionTotal, '/ip_definition_total'),
    (MainSummarySelect, '/main_summary'),
    (FireWallPossible, '/firewall_possible')
]
