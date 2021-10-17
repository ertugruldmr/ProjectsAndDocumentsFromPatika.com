# -*- coding: utf-8 -*-
"""
This is a postgresql excercise project file

Kodluyoruz / patika.dev project

Source of Tasks Link bleow  (description of language : Turkish)
https://app.patika.dev/moduller/sql/Odev4


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
        replacement_cost sütununda bulunan 
            birbirinden farklı değerleri 
sıralayınız.
"""

# Writing the query
QUE_Task_1 = """
SELECT DISTINCT replacement_cost
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
        replacement_cost sütununda 
            birbirinden farklı 
    kaç tane veri vardır?
"""

# Writing the query
QUE_Task_2 = """
SELECT  COUNT( DISTINCT replacement_cost)
FROM film ;
"""
# executing the query
cur.execute(QUE_Task_2)
# getting the data provided by query execution
Task_2 = cur.fetchall()
###################################################################

############################Task-3 ################################ 
"""
3-) film tablosunda bulunan
        film isimlerinde (title) 
            kaç tanesini T karakteri ile başlar 
                ve aynı zamanda 
            rating 'G' ye eşittir?
"""

# Writing the query
QUE_Task_3 = """
SELECT  COUNT(*)
FROM film 
WHERE  (title LIKE 'T%') AND (rating='G');
"""
# executing the query
cur.execute(QUE_Task_3)
# getting the data provided by query execution
Task_3 = cur.fetchall()
###################################################################

############################Task-4 ################################ 
"""
4-) country tablosunda bulunan 
        ülke isimlerinden (country) 
            kaç tanesi 5 karakterden oluşmaktadır?
"""

# Writing the query
QUE_Task_4 = """
SELECT  COUNT(*)
FROM country 
WHERE  (country LIKE '_____');
"""
# executing the query
cur.execute(QUE_Task_4)
# getting the data provided by query execution
Task_4 = cur.fetchall()
###################################################################

############################Task-5 ################################ 
"""
5-) city tablosundaki
        şehir isimlerinin kaçtanesi 
            'R' 
                veya 
            r 
    karakteri ile biter?
"""

# Writing the query
QUE_Task_5 = """
SELECT  COUNT(*)
FROM city 
WHERE  (city ILIKE '%R');
"""
# executing the query
cur.execute(QUE_Task_5)
# getting the data provided by query execution
Task_5 = cur.fetchall()
###################################################################