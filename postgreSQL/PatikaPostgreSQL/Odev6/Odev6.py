# -*- coding: utf-8 -*-
"""
This is a postgresql excercise project file

Kodluyoruz / patika.dev project

Source of Tasks Link bleow  (description of language : Turkish)
https://app.patika.dev/moduller/sql/Odev6


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
        rental_rate sütunundaki değerlerin 
            ortalaması nedir?
"""

# Writing the query
QUE_Task_1 = """
SELECT  AVG(rental_rate)
FROM film ;
"""
# executing the query
cur.execute(QUE_Task_1)
# getting the data provided by query execution
Task_1 = cur.fetchall()
###################################################################

############################Task-2 ################################ 
"""
2-) film tablosunda bulunan
        filmlerden kaçtanesi 
            'C' karekteri ile başlar?
"""

# Writing the query
QUE_Task_2 = """
SELECT  SUM(rental_rate)
FROM film 
WHERE title LIKE 'C%';
"""
# executing the query
cur.execute(QUE_Task_2)
# getting the data provided by query execution
Task_2 = cur.fetchall()
###################################################################

############################Task-3 ################################ 
"""
3-) film tablosunda bulunan filmlerden 
        rental_rate değeri 
            0.99 a eşit olan 
                en uzun (length) film 
                    kaç dakikadır?
"""

# Writing the query
QUE_Task_3 = """
SELECT  MAX(length)
FROM film 
WHERE rental_rate = 0.99;
"""
# executing the query
cur.execute(QUE_Task_3)
# getting the data provided by query execution
Task_3 = cur.fetchall()
###################################################################

############################Task-4 ################################ 
"""
4-) film tablosunda bulunan
        filmlerin uzunluğu 150 dakikadan büyük olanlarına ait 
            kaç farklı replacement_cost değeri
vardır?
"""

# Writing the query
QUE_Task_4 = """
SELECT  COUNT(DISTINCT replacement_cost)
FROM film 
WHERE length > 150;
"""
# executing the query
cur.execute(QUE_Task_4)
# getting the data provided by query execution
Task_4 = cur.fetchall()
###################################################################

# Closing 
conn.close()