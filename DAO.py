from utils import tratarListaDao, printError
import pymysql.cursors
from DB_helper import DB_helper
class Dao:

    def insert(self, table,columns,values):
        try:
            dbHelper = DB_helper()
            cursor = dbHelper.getCursor()
            columns = tratarListaDao(columns)
            values = tratarListaDao(values)
            cursor.execute('INSERT INTO %s(%s) VALUES %s',(table,columns,values))
            cursor.commit()
            return cursor.lastrowid
        except:
            printError()

    def select(self,columns, table, whereArg=''):
        try:
            dbHelper = DB_helper()
            cursor = dbHelper.getCursor()
            whereArg = tratarListaDao(whereArg)
            if whereArg != '':
                cursor.execute('SELECT %s FROM %s WHERE %s',(columns,table,whereArg))
            else:
                cursor.fetchall('SELECT %s FROM %s',(columns,table,))
            cursor.commit()
            return cursor.lastrowid
        except:
            printError()