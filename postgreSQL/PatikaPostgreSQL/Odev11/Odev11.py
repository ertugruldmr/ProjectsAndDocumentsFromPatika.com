# -*- coding: utf-8 -*-
"""
This is a postgresql excercise project file

Kodluyoruz / patika.dev project

Source of Tasks Link bleow  (description of language : Turkish)
https://app.patika.dev/moduller/sql/Odev11


Ertuğrul Demir
https://app.patika.dev/ertugruldmr
"""

import psycopg2
import sys


# Connection
param_dic = {
"database" : "dvdrental",
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

###################################################################
#                           TASKS                                 #
###################################################################

############################Task-1 ################################ 

# Task Description
"""
1-) actor ve customer tablolarında bulunan
        first_name sütunları için 
            tüm verileri sıralayalım.
"""
# Que
QUE_Task_1 ="""
(
SELECT first_name
FROM actor
)
UNION
(
SELECT first_name
FROM customer
 )
"""

# Implementation
try:
    conn = connect(param_dic)
    cur = conn.cursor()
    
    cur.execute(QUE_Task_1)
    OUTPUT_Task_1 = cur.fetchall()
except Exception as e:
    print(e)
finally:
    conn.close()
###################################################################

############################Task-2 ################################ 

# Task Description
"""
2-) actor ve customer tablolarında bulunan
        first_name sütunları için 
            kesişen verileri sıralayalım.
"""
# Que
QUE_Task_2 ="""
(
SELECT first_name
FROM actor
)
INTERSECT
(
SELECT first_name
FROM customer
 )
"""

# Implementation
try:
    conn = connect(param_dic)
    cur = conn.cursor()
    
    cur.execute(QUE_Task_2)
    OUTPUT_Task_2 = cur.fetchall()
except Exception as e:
    print(e)
finally:
    conn.close()
###################################################################

############################Task-3 ################################ 

# Task Description
"""
3-) actor ve customer tablolarında bulunan 
        first_name sütunları için 
            ilk tabloda bulunan 
                ancak 
            ikinci tabloda bulunmayan 
    verileri sıralayalım.
"""
# Que
QUE_Task_3 ="""
(
SELECT first_name
FROM actor
)
EXCEPT
(
SELECT first_name
FROM customer
 )
"""

# Implementation
try:
    conn = connect(param_dic)
    cur = conn.cursor()
    
    cur.execute(QUE_Task_3)
    OUTPUT_Task_3 = cur.fetchall()
except Exception as e:
    print(e)
finally:
    conn.close()
###################################################################


############################Task-3 ################################ 

# Task Description
"""
4-) İlk 3 sorguyu tekrar eden veriler için de yapalım.
"""
# Que


QUE_Task_4_1 ="""
(
SELECT first_name
FROM actor
)
UNION ALL
(
SELECT first_name
FROM customer
 )
"""


QUE_Task_4_2 ="""
(
SELECT first_name
FROM actor
)
INTERSECT ALL
(
SELECT first_name
FROM customer
 )
"""

QUE_Task_4_3 ="""
(
SELECT first_name
FROM actor
)
EXCEPT ALL
(
SELECT first_name
FROM customer
 )
"""


# Implementation
try:
    conn = connect(param_dic)
    cur = conn.cursor()
    
    cur.execute(QUE_Task_4_1)
    OUTPUT_Task_4_1 = cur.fetchall()
    
    cur.execute(QUE_Task_4_2)
    OUTPUT_Task_4_2 = cur.fetchall()
    
    cur.execute(QUE_Task_4_3)
    OUTPUT_Task_4_3 = cur.fetchall()
except Exception as e:
    print(e)
finally:
    conn.close()
###################################################################





