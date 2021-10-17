# -*- coding: utf-8 -*-
"""
This is a postgresql excercise project file

Kodluyoruz / patika.dev project

Source of Tasks Link bleow  (description of language : Turkish)
https://app.patika.dev/moduller/sql/Odev2


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
        tüm sütunlardaki verileri 
            replacement cost değeri 
                12.99 dan büyük eşit 
                    ve 
                16.99 küçük 
        olma koşuluyla sıralayınız ( BETWEEN - AND yapısını kullanınız.)
"""

# Writing the query
QUE_Task_1 = """
SELECT *
FROM film 
WHERE  (replacement_cost BETWEEN 12.99 AND 16.99) AND (NOT replacement_cost = 16.99);
"""
# executing the query
cur.execute(QUE_Task_1)
# getting the data provided by query execution
Task_1 = cur.fetchall()
###################################################################

############################Task-2################################# 
"""
2-) actor tablosunda bulunan 
        first_name ve last_name sütunlardaki verileri 
            first_name 
                'Penelope'  veya 'Nick' veya 'Ed' 
    değerleri olması koşuluyla sıralayınız. ( IN operatörünü kullanınız.)
"""

# Writing the query
QUE_Task_2 = """
SELECT first_name , last_name
FROM actor 
WHERE  first_name IN ('Penelope','Nick','Ed');
"""
# executing the query
cur.execute(QUE_Task_2)
# getting the data provided by query execution
Task_2 = cur.fetchall()
###################################################################

############################Task-3################################# 
"""
3-) film tablosunda bulunan
        tüm sütunlardaki verileri 
            rental_rate 0.99, 2.99, 4.99 
                VE 
            replacement_cost 12.99, 15.99, 28.99 
olma koşullarıyla sıralayınız. ( IN operatörünü kullanınız.)
"""

# Writing the query
QUE_Task_3 = """
SELECT * 
FROM film
WHERE rental_rate IN (0.99, 2.99, 4.99) AND replacement_cost IN (12.99, 15.99, 28.99 );
"""
# executing the query
cur.execute(QUE_Task_3)
# getting the data provided by query execution
Task_3 = cur.fetchall()
###################################################################

