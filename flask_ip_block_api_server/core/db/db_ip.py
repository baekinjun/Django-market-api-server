import pymysql, urllib3
from dbutils.pooled_db import PooledDB
from ..config import G_DATABASE

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

manager_db = PooledDB(
    creator=pymysql,
    cursorclass=pymysql.cursors.DictCursor,
    mincached=2,
    blocking=True,
    charset='utf8mb4',
    use_unicode=True,
    autocommit=True,
    maxconnections=G_DATABASE['maxconnections'],
    port=G_DATABASE['port'],
    host=G_DATABASE['host'],
    user=G_DATABASE['user'],
    password=G_DATABASE['password'],
    db=G_DATABASE['schema']
)
