# /yourapp/models.py  This is where you define the models of your application.
# This may be split into several modules in the same way as views.py.

import json
import psycopg2


def read_rows():
    with open('config.json') as json_data_file:
        config_data = json.load(json_data_file)

    db_user = config_data['db']['user']
    db_password = config_data['db']['password']
    db_name = config_data['db']['name']
    db_host = config_data['db']['host']

    conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_password)

    cur = conn.cursor()
    cur.execute("SELECT datname from pg_database")
    rows = cur.fetchall()

    return rows
