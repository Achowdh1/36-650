import subprocess
import sys

def install(package):
    #if pip doesn't work, try pip3 in the following statement
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("psycopg2")

import psycopg2


def execQuery(q):
    conn = psycopg2.connect(host="localhost", port="5432", user="postgres", password="7135", 
                            database="postgres"
                        )
    cur = conn.cursor()
    cur.execute(q)
    print("Unformatted Results:")
    print (cur.description)
    print("\n\n Formatted Results:")
    for row in cur: print (row)
    cur.close()
    conn.close()

def display(tname = 'hw5_employees'):
    execQuery('select * from ' + tname + ' limit 10;')