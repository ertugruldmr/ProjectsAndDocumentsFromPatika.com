# -*- coding: utf-8 -*-
"""
This is a postgresql excercise project file

Kodluyoruz / patika.dev project

Source of Tasks Link bleow  (language of description : Turkish)
https://app.patika.dev/moduller/sql/Odev1


Ertuğrul Demir
https://app.patika.dev/ertugruldmr
"""

import psycopg2
import pandas as pd
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
        title ve description 
            sütunlarındaki verileri sıralayınız.
"""
# Writing the query
QUE_Task_1 = """
SELECT title , description 
FROM film;
"""

# executing the query
cur.execute(QUE_Task_1)
# getting the data provided by query execution
Task_1 = cur.fetchall()

# Converting to DataFrame object (Optinal)
column_names = ["title", "description"]
df_task_1 = pd.DataFrame(Task_1, columns=column_names)
###################################################################

############################Task-2#################################
"""
2-) film tablosunda bulunan tüm sütunlardaki verileri 
        film uzunluğu (length) 60 dan büyük 
            VE
        75 ten küçük olma koşullarıyla sıralayınız.
"""
# Writing the query
QUE_Task_2 = """
SELECT * 
FROM film
WHERE (length > 60)  AND ( length < 75 ) ;
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
            rental_rate 0.99 
                VE 
            replacement_cost 12.99 VEYA 28.99 
    olma koşullarıyla sıralayınız.
"""
# Writing the query
QUE_Task_3 = """
SELECT * 
FROM film
WHERE rental_rate = 0.99  AND ( replacement_cost =  12.99  OR replacement_cost =  28.99   ) ;""" 
# executing the query
cur.execute(QUE_Task_3)
# getting the data provided by query execution
Task_3 = cur.fetchall()
###################################################################

############################Task-4#################################
"""
4-) customer tablosunda bulunan 
        first_name sütunundaki 
            değeri 'Mary' 
                olan müşterinin 
                    last_name sütunundaki değeri nedir?
"""
# Writing the query
QUE_Task_4 = """
SELECT last_name 
FROM customer
WHERE first_name = 'Mary' ;
""" 
# executing the query
cur.execute(QUE_Task_4)
# getting the data provided by query execution
Task_4 = cur.fetchall()
###################################################################

############################Task-5#################################
"""
5-) film tablosundaki 
        uzunluğu(length) 
            50 den büyük OLMAYIP 
                aynı zamanda 
            rental_rate değeri 2.99 veya 4.99 OLMAYAN 
        verileri sıralayınız.
"""
# Writing the query
QUE_Task_5 = """
SELECT * 
FROM film
WHERE (NOT length > 50)  AND ( NOT (rental_rate = 2.99 OR rental_rate = 4.99 ) ) ;
""" 
# executing the query
cur.execute(QUE_Task_5)
# getting the data provided by query execution
Task_5 = cur.fetchall()
###################################################################

# Closing 
conn.close()