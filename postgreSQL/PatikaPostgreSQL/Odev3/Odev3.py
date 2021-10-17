# -*- coding: utf-8 -*-
"""
This is a postgresql excercise project file

Kodluyoruz / patika.dev project

Source of Tasks Link bleow  (description of language : Turkish)
https://app.patika.dev/moduller/sql/Odev3


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
1-) country tablosunda bulunan 
        country sütunundaki ülke isimlerinden 
            'A' karakteri ile başlayıp 
            'a' karakteri ile sonlananları 
        sıralayınız.
"""

# Writing the query
QUE_Task_1 = """
SELECT country
FROM country 
WHERE country LIKE 'A%a';
"""
# executing the query
cur.execute(QUE_Task_1)
# getting the data provided by query execution
Task_1 = cur.fetchall()
###################################################################

############################Task-2 ################################ 
"""
2-) country tablosunda bulunan 
        country sütunundaki ülke isimlerinden 
            en az 6 karakterden oluşan 
                ve 
            sonu 'n' karakteri ile sonlananları 
    sıralayınız.
"""

# Writing the query
QUE_Task_2 = """
SELECT country
FROM country 
WHERE country LIKE '_____%n';
"""
# executing the query
cur.execute(QUE_Task_2)
# getting the data provided by query execution
Task_2 = cur.fetchall()
###################################################################

############################Task-3 ################################ 
"""
3-) film tablosunda bulunan 
        title sütunundaki film isimlerinden 
                en az 4 adet büyük ya da küçük harf farketmesizin 
                    'T' karakteri içeren film isimlerini 
    sıralayınız.
"""

# Writing the query
QUE_Task_3 = """
SELECT title
FROM film 
WHERE title  ILIKE '%t%t%t%t%';
"""
# executing the query
cur.execute(QUE_Task_3)
# getting the data provided by query execution
Task_3 = cur.fetchall()
###################################################################

############################Task-4 ################################ 
"""
4-) film tablosunda bulunan
        tüm sütunlardaki verilerden 
            title 
                'C' karakteri ile başlayan 
                    ve 
                uzunluğu (length) 90 dan büyük olan 
                    ve 
                rental_rate 2.99  olan 
        verileri sıralayınız.
"""

# Writing the query
QUE_Task_4 = """
SELECT *
FROM film 
WHERE (title  LIKE 'C%') AND (length > 90) AND rental_rate = 2.99 ;
"""
# executing the query
cur.execute(QUE_Task_4)
# getting the data provided by query execution
Task_4 = cur.fetchall()
###################################################################
