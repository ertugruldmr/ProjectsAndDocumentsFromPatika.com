# -*- coding: utf-8 -*-
"""
This is a postgresql excercise project file

Kodluyoruz / patika.dev project

Source of Tasks Link bleow  (description of language : Turkish)
https://app.patika.dev/moduller/sql/Odev8


Ertuğrul Demir
https://app.patika.dev/ertugruldmr
"""

import psycopg2
import sys


# Connection
param_dic = {
    #"database" : "dvdrental",
    "user" : "postgres", 
    "password" : "postgre",
    "host" : "localhost", 
    "port" : "5432"
}
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn
# Connecting to Database
conn = connect(param_dic)
# Taking the Referance
cur = conn.cursor()

###################################################################
#                           TASKS                                 #
###################################################################

############################Task-1 ################################ 
param_dic = {
"database" : "test",
"user" : "postgres", 
"password" : "postgre",
"host" : "localhost", 
"port" : "5432"
}

"""
1-) test veritabanınızda 
        employee isimli sütun bilgileri 
            id(INTEGER), 
            name VARCHAR(50), 
            birthday DATE,
            email VARCHAR(100) 
        olan bir tablo oluşturalım.
"""
# Writing the query
QUE_Task_1 ="""
CREATE DATABASE test;
"""

QUE_Task_1_1 = """
CREATE TABLE employee(
    id          INT PRIMARY KEY     NOT NULL,
    name        VARCHAR(50)         NOT NULL,
    birthday    DATE                NOT NULL,
    email       VARCHAR(50)         NOT NULL
    )
"""

# Implementation

# Executinng the sql queries
try:
    conn.set_isolation_level( psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT )
# executing the query
    cur.execute(QUE_Task_1)
    conn.commit()
    conn.close()


except Exception as e :
    print(e)
finally:
    conn.close()


try:
    conn = connect(param_dic)
    cur = conn.cursor()
    
    cur.execute(QUE_Task_1_1)
    conn.commit()   
    conn.close()
except Exception as e :
    print(e)
finally:
    conn.close()
     
###################################################################

############################Task-2 ################################ 

"""
2-) Oluşturduğumuz employee tablosuna 
        'Mockaroo' servisini kullanarak 
            50 adet veri 
    ekleyelim.
"""
# Implementation

# All the records in the txt file as sql query 
with open('random50record.txt',encoding = 'utf-8') as f:
    records = f.readlines()
conn = connect(param_dic)
cur = conn.cursor()

for record in records:
    try:
    # executing the query
        cur.execute(record)
    # getting the data provided by query execution
        conn.commit() 
    except Exception as e :
        if type(e) == type(psycopg2.errors.UniqueViolation):       
            cur.execute("TRUNCATE TABLE employee;")
            cur.execute(record)
            conn.commit()
        
conn.close()
###################################################################


############################Task-3 ################################ 

"""
3-) Sütunların her birine göre
        diğer sütunları güncelleyecek 
            5 adet UPDATE işlemi 
    yapalım.
"""
QUE_Task_3 = """
UPDATE 
    employee
SET
    name = 'Ertuğrul',
    birthday = '1915-10-24',
    email = 'ertugrul@solvey.conference'
WHERE
    id = 1
"""

# Implementation
conn = connect(param_dic)
cur = conn.cursor()

try:
    cur.execute(QUE_Task_3)
    conn.commit()
except Exception as e:
    print(e)
finally:
    conn.close()
###################################################################


############################Task-4 ################################ 

"""
3-) Sütunların her birine göre
        ilgili satırı silecek 
            5 adet DELETE işlemi 
    yapalım.
"""
QUE_Task_4_0 = """
INSERT INTO 
    employee(id,name,birthday,email)
VALUES
    (51,'Edward ','1891-11-22','manipulator@master.psychology')
"""
QUE_Task_4 = """
DELETE 
FROM
    employee
WHERE
    email = 'manipulator@master.psychology'
"""

# Implementation
conn = connect(param_dic)
cur = conn.cursor()

try:
    cur.execute(QUE_Task_4)
    conn.commit()
except Exception as e:
    print(e)
finally:
    conn.close()
###################################################################