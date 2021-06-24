from .encoder import dict_encoder
import logging
import pymysql
from core.db.db_ip import manager_db


class Procedure:
    def __init__(self):
        self.db = manager_db

    @dict_encoder
    def b_fetchone(self, sql, args=()):
        conn = self.db.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql, args)
            rs = cursor.fetchone()
        except Exception as e:
            logging.error(e)
            raise ValueError('error')
        finally:
            cursor.close()
            conn.close()
        return rs

    @dict_encoder
    def b_fetchall(self, sql, args=()):
        conn = self.db.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql, args)
            rs = cursor.fetchall()
        except Exception as e:
            logging.error(e)
            raise ValueError('error')
        finally:
            cursor.close()
            conn.close()
        return rs

    @dict_encoder
    def b_execute(self, sql, args=()):
        conn = self.db.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql, args)
            cursor.execute("SELECT @o_out_code;")
            rs = cursor.fetchone()
        except Exception as e:
            logging.error(e)
            raise ValueError('error')
        finally:
            cursor.close()
            conn.close()
        return rs

    @dict_encoder
    def b_execute_many(self, sql, args=()):
        conn = self.db.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.executemany(sql, args)
            cursor.execute("SELECT @o_out_code;")
            rs = cursor.fetchone()
        except Exception as e:
            logging.error(e)
            raise ValueError('error')
        finally:
            conn.commit()
            cursor.close()
            conn.close()
        return rs
