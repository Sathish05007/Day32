import mysql.connector 
from db import info

try:
    mysql.connector.connect(**info)
    print("connection done")
except:
    print("not able to connect")