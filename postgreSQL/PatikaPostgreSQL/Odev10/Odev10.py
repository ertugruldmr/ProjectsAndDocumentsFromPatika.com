# -*- coding: utf-8 -*-
"""
This is a postgresql excercise project file

Kodluyoruz / patika.dev project

Source of Tasks Link bleow  (description of language : Turkish)
https://app.patika.dev/moduller/sql/Odev10


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
1-) city tablosu ile country tablosunda bulunan
        şehir (city) ve ülke (country) isimlerini 
            birlikte görebileceğimiz 
                LEFT JOIN 
sorgusunu yazınız.
"""
# Que
QUE_Task_1 ="""
SELECT city, country 
FROM city
LEFT JOIN country ON city.country_id = country.country_id;
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
2-) customer tablosu ile payment tablosunda bulunan
        payment_id ile 
            customer tablosundaki 
                first_name ve last_name isimlerini 
                    birlikte görebileceğimiz 
                        RIGHT JOIN 
sorgusunu yazınız.
"""
# Que
QUE_Task_2 ="""
SELECT payment_id, first_name,  last_name
FROM customer
RIGHT JOIN payment ON payment.customer_id = customer.customer_id;
"""

# Implementation
try:
    conn = connect(param_dic)
    cur = conn.cursor()
    
    cur.execute(QUE_Task_1)
    OUTPUT_Task_2 = cur.fetchall()
except Exception as e:
    print(e)
finally:
    conn.close()
###################################################################

############################Task-3 ################################ 

# Task Description
"""
3-) customer tablosu ile rental tablosunda bulunan
        rental_id ile 
            customer tablosundaki 
                first_name ve last_name isimlerini 
                    birlikte görebileceğimiz 
FULL JOIN sorgusunu yazınız.
"""
# Que
QUE_Task_3 ="""
SELECT rental_id, first_name,  last_name
FROM customer
FULL JOIN rental ON rental.customer_id = customer.customer_id;
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