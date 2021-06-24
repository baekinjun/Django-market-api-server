from .view import *

url_patterns = [
    (FirewallActive, '/firewall_active'),
    (FirewallBlockIpAll, '/firewall_block_ip'),
    (IpDefinition, '/ip_definition'),
    (BlockHistory, '/block_history'),
    (FirewallWhiteList, '/firewall_white'),
    (ConfigurationView, '/configuration'),
    (ConfigurationTotalView, '/configuration_total')
]
