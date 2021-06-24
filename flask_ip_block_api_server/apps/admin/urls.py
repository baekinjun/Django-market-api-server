from .view import *

url_patterns = [
    (DailyUsageCriminalIp, '/daily_usage_criminal_ip'),
    (DailyUsageTrace, '/daily_usage_trace'),
    (DailyBustedDetection, '/daily_busted_detection'),
    (DailyBustedViolation, '/daily_busted_violation'),
    (AuditCategoryList, '/audit_category_list'),
    (AuditLogList, '/audit_log_list'),
    (AdminRegisterList, '/admin_registration_list')
]
