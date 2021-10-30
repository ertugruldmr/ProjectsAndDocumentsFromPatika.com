# -*- coding: utf-8 -*-
"""
This is a postgresql excercise project file

Kodluyoruz / patika.dev project

Source of Tasks Link bleow  (description of language : Turkish)
https://app.patika.dev/moduller/sql/Odev12


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
1-) film tablosunda 
        film uzunluğu length sütununda gösterilmektedir.
            Uzunluğu ortalama film uzunluğundan fazla 
                kaç tane film vardır?
"""
# Que
QUE_Task_1 ="""
SELECT COUNT(*)
FROM film
WHERE film.length > (
    SELECT AVG(length)
    FROM film
    ) ; 
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
2-) film tablosunda 
        en yüksek rental_rate değerine sahip 
            kaç tane film vardır?
"""
# Que
QUE_Task_2 ="""
SELECT COUNT(*)
FROM film
WHERE rental_rate = ANY(
    SELECT MAX(rental_rate)
    FROM film );
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
3-) film tablosunda 
        en düşük rental_rate ve en düşük replacement_cost 
            değerlerine sahip filmleri 
    sıralayınız.
"""
# Que
QUE_Task_3 ="""
SELECT rental_rate, replacement_cost
FROM film
WHERE ( rental_rate = ANY (SELECT MIN(rental_rate) FROM film) ) AND (replacement_cost = ANY(SELECT MIN(replacement_cost) FROM film) );
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

############################Task-4 ################################ 

# Task Description
"""
4-) payment tablosunda 
        en fazla sayıda alışveriş yapan 
            müşterileri(customer) 
    sıralayınız.
"""
# Que
QUE_Task_4 ="""
SELECT customer.customer_id, first_name, last_name, amount
FROM payment 
LEFT JOIN customer ON payment.customer_id = customer.customer_id
WHERE amount = ANY (
    SELECT MAX(amount)
    FROM payment
    ) ;
"""

# Implementation
try:
    conn = connect(param_dic)
    cur = conn.cursor()
    
    cur.execute(QUE_Task_4)
    OUTPUT_Task_4 = cur.fetchall()
except Exception as e:
    print(e)
finally:
    conn.close()
###################################################################