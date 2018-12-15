#!/usr/bin/env python

import psycopg2
import sys

"""
Drop all tables of database you given.
"""

try:
    conn = psycopg2.connect("postgres://ucshrajlbldvmt:c2289d70e17a51fed9063a7d62299035c4a55fd7146274648c4e8ef56e8d2fb3@ec2-23-21-188-236.compute-1.amazonaws.com:5432/d88dvn90epfvqe")
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