from core.db import Procedure


class LaboratoryPageDao:
    def __init__(self):
        self.conn_s = Procedure()

    def lab_title(self, id):
        return self.conn_s.b_fetchone(
            """SELECT * FROM criminal_ip_manager.laboratory_title where id = %s;""", id
        )

    def lab_data(self, id):
        return self.conn_s.b_fetchall(
            """call sp_test_lab{}();""".format(id)
        )
