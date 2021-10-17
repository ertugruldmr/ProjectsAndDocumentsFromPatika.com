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
1-) film tablosunda bulunan filmleri 
        rating değerlerine göre gruplayınız.
"""

# Writing the query
QUE_Task_1 = """
SELECT rating 
FROM film 
GROUP BY rating ; 
"""
# executing the query
cur.execute(QUE_Task_1)
# getting the data provided by query execution
Task_1 = cur.fetchall()
###################################################################

############################Task-2 ################################
"""
2-) film tablosunda bulunan filmleri
        replacement_cost sütununa göre grupladığımızda 
            film sayısı 50 den fazla olan replacement_cost değerini 
                ve 
            karşılık gelen film sayısını 
        sıralayınız.
"""

# Writing the query
QUE_Task_2 = """
SELECT replacement_cost, count(*)
FROM film 
GROUP BY replacement_cost
HAVING count(*) > 50 ;
"""
# executing the query
cur.execute(QUE_Task_2)
# getting the data provided by query execution
Task_2 = cur.fetchall()
###################################################################

############################Task-3 ################################
"""
3-)  customer tablosunda bulunan
        store_id değerlerine karşılık gelen 
            müşteri sayılarını nelerdir? 

"""

# Writing the query
QUE_Task_3 = """
SELECT store_id, count(*)
FROM customer 
GROUP BY store_id ; 
"""
# executing the query
cur.execute(QUE_Task_3)
# getting the data provided by query execution
Task_3 = cur.fetchall()
###################################################################


############################Task-4 ################################
"""
4-) city tablosunda bulunan şehir verilerini 
        country_id sütununa göre gruplandırdıktan sonra 
            en fazla şehir sayısı barındıran country_id bilgisini 
                ve
            şehir sayısını paylaşınız.
"""

# Writing the query
QUE_Task_4 = """
SELECT country_id, count(*)
FROM city 
GROUP BY country_id 
ORDER BY count(*) DESC
LIMIT 1 ;
"""
# executing the query
cur.execute(QUE_Task_4)
# getting the data provided by query execution
Task_4 = cur.fetchall()
###################################################################

# Closing 
conn.close()