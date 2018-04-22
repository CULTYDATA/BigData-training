
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra import ReadTimeout

import uuid
import logging

import time
from threading import Thread, RLock


cardinality = 60
verrou = RLock()


def shift(l, n):
    return l[n:] + l[:n]

def getAvailablePort(ports):
    with verrou:
        pok = 0
        for port in shift(ports, 1):
            try:
                Cluster(['192.168.99.100'],port).connect('system_traces')
                pok = port
                break
            except:
                pass       
        print("AVAILABLE PORT : " + str(pok))
        return pok



def getDemoSession():
    cluster = Cluster(['192.168.99.100'],getAvailablePort([9042,9043,9044]))
    session = cluster.connect('demo')
    session.execute('USE demo')
    return session

def batchExecution(records = 100):
    UUIDS = []
    i = 0
    while i < records:
        UUIDS.append(uuid.uuid1());
        i += 1;
    
    counter = 1
    for id in UUIDS:
        try:
            getDemoSession().execute(
                """
                INSERT INTO demo.persons (id, num, familyName, firstName, age, address, phone)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (id, counter, "j1", "j2", 40, "paris", "+33687453287")
            )
            counter += 1;
        except:
            getDemoSession().execute(
                """
                INSERT INTO demo.persons (id, num, familyName, firstName, age, address, phone)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (id, counter, "j1", "j2", 40, "paris", "+33687453287")
            )
            counter += 1;
            pass
    print(UUIDS)
    print("BATCH END")


def clearAll():
    getDemoSession().execute("DROP TABLE IF EXISTS Persons")
    getDemoSession().execute("CREATE TABLE Persons (id uuid, num int, familyName varchar, firstName varchar, age int, address varchar,phone varchar,PRIMARY KEY(id,familyName))")
    print("ALL HAVE BEEN CLEARED AND INITIALIZED")

def doGet():
    while True:   
        try:
            future = getDemoSession().execute_async("SELECT count(*) FROM Persons")
            res = future.result()
            print("-----------") 
            print(res[0]) 
            print("-----------") 
        except:
            future = getDemoSession().execute_async("SELECT count(*) FROM Persons")
            res = future.result()
            print("-----------") 
            print(res[0]) 
            print("-----------") 
            logging.exception("Query timed out:")
            pass

        if res[0].count == cardinality:
            break


        
### RUNTIME

clearAll()


# Create threads
try:
    Thread(target=doGet).start()
except:
   print("Error: unable to start thread")

try:
    Thread(target=batchExecution(cardinality/3)).start()
except:
   print("Error: unable to start thread")

try:
    Thread(target=batchExecution(cardinality/3)).start()
except:
   print("Error: unable to start thread")

try:
    Thread(target=batchExecution(cardinality/3)).start()
except:
   print("Error: unable to start thread")
    


exit(0)
















