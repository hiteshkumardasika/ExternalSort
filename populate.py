# populating the the table

import random, sys
import psycopg2


def create(cur, conn, size):
    cur.execute("""CREATE TABLE IF NOT EXISTS TEST(INDEX INTEGER, VALUE INTEGER, PRIMARY KEY(INDEX))""")
    cur.execute("""TRUNCATE TABLE TEST""")

    for i in range(1, size + 1):
        cur.execute("INSERT INTO TEST (INDEX,VALUE) VALUES (%s,%s)", (i, random.randint(i, sys.maxsize - i)))

    conn.commit()

#    print("Table 'TEST' with",i,"entries is created.")
