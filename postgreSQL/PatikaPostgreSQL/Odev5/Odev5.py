# -*- coding: utf-8 -*-
"""
This is a postgresql excercise project file

Kodluyoruz / patika.dev project

Source of Tasks Link bleow  (description of language : Turkish)
https://app.patika.dev/moduller/sql/Odev5


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
# Connecting to Database
conn = connect(param_dic)
# Taking the Referance
cur = conn.cursor()

###################################################################
#                           TASKS                                 #
###################################################################

############################Task-1 ################################ 
"""
1-) film tablosunda bulunan
            ve 
        film ismi (title) 'n' karakteri ile biten 
        en uzun (length) 5 filmi sıralayınız.
"""

# Writing the query
QUE_Task_1 = """
SELECT  *
FROM film 
WHERE title LIKE '%n' 
ORDER BY length DESC
LIMIT 5;
"""
# executing the query
cur.execute(QUE_Task_1)
# getting the data provided by query execution
Task_1 = cur.fetchall()
###################################################################

############################Task-2 ################################ 
"""
2-) film tablosunda bulunan
        ve 
    film ismi (title) 'n' karakteri ile biten 
    en kısa (length) 
        ikinci 5 filmi sıralayınız.
"""

# Writing the query
QUE_Task_2 = """
SELECT  *
FROM film 
WHERE title LIKE '%n' 
ORDER BY length ASC
OFFSET 5
LIMIT 5;
"""
# executing the query
cur.execute(QUE_Task_2)
# getting the data provided by query execution
Task_2 = cur.fetchall()
###################################################################

############################Task-3 ################################ 
"""
3-) customer tablosunda bulunan 
    last_name sütununa göre azalan yapılan sıralamada 
        store_id 1 olmak koşuluyla 
            ilk 4 veriyi sıralayınız.
"""

# Writing the query
QUE_Task_3 = """
SELECT  *
FROM customer 
WHERE store_id = 1
ORDER BY last_name DESC
LIMIT 4;
"""
# executing the query
cur.execute(QUE_Task_3)
# getting the data provided by query execution
Task_3 = cur.fetchall()
###################################################################

