import os
import pymysql.cursors
import sys
class DB_helper :    
    DATA_BASE_NAME = "Database"
    SQL_HOST = "localhost"
    SQL_USER = "root"
    SQL_PASSWD = ""
    SQL_SHARSET = "utf8mb4"
    SQL_UNICODE = True
    def __init__ (self):
        self.conn = ''
        self._cursorclass = pymysql.cursors.DictCursor

    def getConn(self, database_name = DATA_BASE_NAME):

        conn = pymysql.connect(host = self.SQL_HOST,
                    user = self.SQL_USER,
                    passwd = self.SQL_PASSWD,
                    db = database_name,
                    charset = self.SQL_SHARSET,
                    use_unicode = self.SQL_UNICODE,
                    cursorclass = self._cursorclass)
        return conn
    

    
    def getCursor(self):
        self.conn = self.getConn()
        cursor = self.conn.cursor()
        return cursor


