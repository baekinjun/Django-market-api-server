from core.db import Procedure


class MitigationPageDao:
    def __init__(self):
        self.conn_s = Procedure()

    def firewall_active(self, args):
        return self.conn_s.b_fetchall(
            """SELECT fw_id,fw_name,group_name FROM firewall_info where activate_code =2 LIMIT %s OFFSET %s;""", args
        )

    def firewall_block_ip_all(self, args):
        return self.conn_s.b_fetchall(
            """SELECT bo.block_id,bo.command,done,bo.fw_id,bo.group_name,bo.ip_address,bo.reg_dtime,bo.requirement_user,info.fw_name,info.fw_type,info.fw_url
                FROM firewall_block_ip_address as bo
                join firewall_info as info on bo.fw_id = info.fw_id 
                where bo.command = 0
                ORDER BY bo.reg_dtime desc LIMIT %s OFFSET %s; """, args
        )

    def firewall_ip_block_set(self, args):
        return self.conn_s.b_execute(
            """call sp_firewall_ip_block_set(%s,%s,%s,0,%s,0,@o_out_code)""",
            args
        )

    def firewall_ip_block_delete(self, args):
        return self.conn_s.b_execute(
            """call sp_firewall_ip_block_set(%s,%s,%s,1,%s,0,@o_out_code)""",
            args
        )

    def ip_address_definition_all(self, args):
        return self.conn_s.b_fetchall(
            """SELECT * FROM ip_address_definition order by reg_dtime desc  LIMIT %s OFFSET %s;""", args
        )

    def ip_address_definition_search(self, args):
        return self.conn_s.b_fetchall(
            """SELECT * FROM ip_address_definition where ip_address LIKE %s or name LIKE %s or description LIKE %s LIMIT %s OFFSET %s""",
            args
        )

    def ip_address_definition_update(self, args):
        return self.conn_s.b_execute(
            """UPDATE ip_address_definition SET name = %s , description=%s where ip_address =%s """, args
        )

    def ip_address_definition_create(self, args):
        return self.conn_s.b_execute(
            """INSERT INTO ip_address_definition(name,description,ip_address) values(%s,%s,%s)""", args
        )

    def ip_address_definition_delete(self, args):
        return self.conn_s.b_execute_many(
            """DELETE FROM ip_address_definition where ip_address = %s""", args
        )

    def firewall_block_history(self, args):
        return self.conn_s.b_fetchall(
            """call sp_firewall_block_history_select(%s,%s,%s,%s);""", args
        )

    def firewall_white_list_all(self, args):
        return self.conn_s.b_fetchall(
            """SELECT b.activation,b.description,a.fw_id,a.fw_name,a.fw_type,a.fw_url,b.ip_address,b.modify_dtime,b.reg_dtime 
            FROM firewall_info as a 
            join firewall_whitelist as b on a.fw_id = b.fw_id 
            where b.activation = 1 order by b.reg_dtime desc 
            LIMIT %s OFFSET %s""",
            args
        )

    def firewall_white_list_search(self, args):
        return self.conn_s.b_fetchall(
            """SELECT b.activation,b.description,a.fw_id,a.fw_name,a.fw_type,a.fw_url,b.ip_address,b.modify_dtime,b.reg_dtime
             FROM firewall_info as a 
            join firewall_whitelist as b on a.fw_id = b.fw_id
            where b.activation = 1 and (a.fw_name LIKE %s or b.ip_address LIKE %s or b.description LIKE %s) order by b.reg_dtime desc LIMIT %s OFFSET %s ;""",
            args
        )

    def firewall_white_list_set(self, args):
        return self.conn_s.b_execute(
            """call sp_firewall_whitelist_set(%s,%s,1,%s,@o_out_code)""", args
        )

    def firewall_white_list_delete(self, args):
        return self.conn_s.b_execute(
            """call sp_firewall_whitelist_set(%s,%s,0,%s,@o_out_code)""", args
        )

    def check_white_list(self, args):
        return self.conn_s.b_fetchone(
            """SELECT * FROM firewall_whitelist where fw_id = %s and ip_address= %s and activation=1;""", args
        )

    def firewall_configuration_list(self, args):
        return self.conn_s.b_fetchall(
            """SELECT info.fw_id,info.fw_name,info.fw_url,info.fw_type,info.group_name,info.activate_code,info.dev_id,info.reg_dtime
                ,cls.authentification_type,api.api_key,uinfo.user_id,uinfo.user_pw
                FROM criminal_ip_manager.firewall_info  as info
                join firewall_classification as cls on info.fw_type = cls.fw_type
                left join firewall_api as api on info.fw_id = api.fw_id
                join firewall_user_info as uinfo on uinfo.fw_id = info.fw_id 
                LIMIT %s OFFSET %s;""", args
        )

    def firewall_configuration_set(self, args):
        return self.conn_s.b_execute(
            """call sp_firewall_info_new_set(%s,1,%s,%s,%s,%s,%s,%s,%s,%s,%s,@o_out_code)""", args
        )

    def firewall_configuration_delete(self, args):
        return self.conn_s.b_execute(
            """call sp_firewall_info_new_set(%s,2,%s,%s,%s,%s,%s,%s,%s,%s,%s,@o_out_code)""", args
        )

    def firewall_configuration_total(self):
        return self.conn_s.b_fetchone(
            """SELECT COUNT(*) as count FROM firewall_info;"""
        )
