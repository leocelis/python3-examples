"""
Installation
============

>pip3 install PyMySQ

export DB_HOST=<mysql_host>
export DB_PORT=<mysql_port>
export DB_USER=<mysql_username>
export DB_PASSWORD=<mysql_password>

>python3 mysql_crud.py
"""
import os

import pymysql

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

global gconn
gconn = None


def dictfecth(cursor):
    """
    Convert cursor to dict

    :param cursor:
    :return:
    """
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


def get_connection(db_name: str):
    """
    Create connection object

    :param db_name: database name
    :return:
    """
    global gconn
    if not gconn:
        gconn = pymysql.connect(host=DB_HOST,
                                port=int(DB_PORT),
                                user=DB_USER,
                                passwd=DB_PASSWORD,
                                db=db_name,
                                connect_timeout=30,
                                use_unicode=True)

    return gconn


def get_all(table: str):
    """
    Get all rows for a given table

    :param table: table name
    :return:
    """
    global gconn
    cursor = gconn.cursor()

    sql = """
    SELECT * FROM {}
    """.format(table)

    cursor.execute(sql)

    gconn.commit()
    rows = dictfecth(cursor)
    cursor.close()

    return rows


def get_version():
    """
    Get MySQL version

    :return:
    """
    global gconn
    cursor = gconn.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    return data


def insert_row(table: str, fields: str, values: str):
    r = None
    global gconn
    cursor = gconn.cursor()

    sql = """
    INSERT INTO {}({}) VALUES ({})
    """.format(table, fields, values)

    try:
        r = cursor.execute(sql)
        gconn.commit()
    except:
        gconn.rollback()

    cursor.close()
    return r


conn = get_connection(db_name="test")
ver = get_version()

print("\nMySQL version: {}\n".format(ver))

r = insert_row(table="test", fields="title", values="'Z'")
print("\nInserting row... {}\n".format(r))

print("\nRetrieving rows...\n")

rs = get_all(table="test")
for r in rs:
    print(r)
