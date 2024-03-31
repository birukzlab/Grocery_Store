import psycopg2

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = psycopg2.connect(
            user='postgres',
            password='Ethio#2014',
            host='127.0.0.1',
            port=5432,
            database='grocery_store'
        )
    return __cnx