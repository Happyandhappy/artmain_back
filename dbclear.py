#!/usr/bin/env python

import psycopg2
import sys

"""
Drop all tables of database you given.
"""

try:
    conn = psycopg2.connect("postgres://umuayzpwcqddpc:8170a674f50641c738b20d585f6e252fb673f77f30714d918be940038bdd1a10@ec2-54-197-249-140.compute-1.amazonaws.com:5432/d7qvmk0t47ltii")
    conn.set_isolation_level(0)
except:
    print("Unable to connect to the database.")

cur = conn.cursor()

try:
    cur.execute("SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
    rows = cur.fetchall()
    for row in rows:
        print("dropping table: ", row[1])
        cur.execute("drop table " + row[1] + " cascade")
    cur.close()
    conn.close()
except:
    print("Error: ", sys.exc_info()[1])