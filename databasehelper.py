from pymysql import *
class DatabaseHelper:

    @staticmethod
    def get_data (query,parameters=None):
        """connector python create a connection btwn python and mysql, as mysql server khudhi starts"""
        conn = connect (host='localhost',database='world',user='root',password='root')

        cur=conn.cursor()#"""using curser give query , therefore number if querys = no of cursors"""
        if(parameters is None):
            cur.execute(query)
        else:
            cur.execute(query%parameters)
        result=cur.fetchone()#"""result is tuple always"""
        cur.close()
        conn.close()
        return result
#            """takes % wale parameters one by one """
 #           """till  ow common for all ,will execute query only"""


    @staticmethod
    def get_all_data(query, parameters=None):
        """connector python create a connection btwn python and mysql, as mysql server khudhi starts"""
        conn = connect(host='localhost', database='world', user='root', password='root')
        cur = conn.cursor()
        """using curser give query , therefore number if querys = no of cursors"""
        if (parameters is None):
            print("none params")
            cur.execute(query)
        else:
            cur.execute(query % parameters)
        result = cur.fetchall()
        """result is tuple always"""
        cur.close()
        conn.close()
        return result


    @staticmethod
    def execute_query(query, parameters=None):
        #when no row again,used for insert and update ,no return
        #connector python create a connection btwn python and mysql, as mysql server khudhi starts
        conn = connect(host='localhost', database='world', user='root', password='root')
        cur = conn.cursor()
        #using curser give query , therefore number if querys = no of cursors
        if (parameters is None):
            cur.execute(query)
        else:
            cur.execute(query % parameters)
        #result is tuple always
        conn.commit()
        #inside try catch,inside try last line,eg bank withdraw but not deposit
        cur.close()
        conn.close()

    def get_all_data_multiple_input(query, params):
        conn = connect(host='localhost', database='world', user='root', password='root')
        cur = conn.cursor()
        format_strings = ','.join(['%s'] * len(params))
        cur.execute(query % format_strings, params)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result


