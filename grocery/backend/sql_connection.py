import mysql.connector

# Only create connection when the variable = None
__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='root',
                                    host='127.0.0.1',
                                    database='grocery')
    return __cnx