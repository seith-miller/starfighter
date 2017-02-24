# /yourapp/models.py  This is where you define the models of your application.
# This may be split into several modules in the same way as views.py.

import json
import psycopg2

from instance import config


def read_rows():
    db_user = config.user
    db_password = config.password
    db_name = config.name
    db_host = config.host

    conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_password)

    cur = conn.cursor()
    cur.execute("SELECT datname from pg_database")
    rows = cur.fetchall()

    return rows
