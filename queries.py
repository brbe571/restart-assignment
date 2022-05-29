import sqlite3
import time
from datetime import datetime


def getActors():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM actor LIMIT 5;")
        actors = cursor.fetchall()
        return actors
        

def film_year():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM film ORDER BY release_year ASC LIMIT 10;")
        film = cursor.fetchall()
        return film
        

def actor_name_wood():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute(f"SELECT  actor.first_name, actor.last_name FROM actor WHERE actor.last_name = 'WOOD';")
        name = cursor.fetchall()
        return name
        

def postal_code():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM address WHERE address.postal_Code = '61117';")
        post_code = cursor.fetchall()
        return post_code
        

def city_id():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM address WHERE address.city_id = '167';")
        id = cursor.fetchall()
        return id
        

def district():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT address.district FROM address WHERE address.address = '1913 Hanoi Way';")
        district = cursor.fetchall()
        return district
        

def country():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM country limit 10;")
        country = cursor.fetchall()
        return country
        

def film_title():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT film.title FROM film limit 5;")
        film = cursor.fetchall()
        return film
        

def staff():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT staff_id, first_name, last_name FROM staff LIMIT 2;")
        staff = cursor.fetchall()
        return staff
        

def payment_amount():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM payment ORDER BY payment.amount DESC LIMIT 10;")
        amount = cursor.fetchall()
        return amount
       

def delete_language():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("DELETE FROM language WHERE language.name = 'French';")
        delete_language = cursor.fetchall()
        return delete_language
        

def update_category():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("UPDATE category SET name='Doco' WHERE category.name='Documentary';")
        category = cursor.fetchall()
        return category
        

def add_language():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO language (language_id, name, last_update) VALUES (7,'Welsh', '2019-03-17')")
        connect.commit()
        print(cursor.rowcount, "record inserted.")
        
    
def add_actor():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO actor (actor_id, first_name, last_name, last_update) VALUES (202,'Johnny', 'Depp', '2022-05-26')")
        connect.commit()
        print(cursor.rowcount, "record inserted.")
        

def add_country():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO country (country_id, country, last_update) VALUES (110, 'Wales', '2022-05-26')")
        connect.commit()
        print(cursor.rowcount, "record inserted.")
        

def add_city():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO city (city_id, city, country_id, last_update) VALUES (601, 'Auckland', 68, '2022-05-26')")
        connect.commit()
        print(cursor.rowcount, "record inserted.")
        

def add_category():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO category (category_id, name, last_update) VALUES (17, 'romcom', '2022-05-26')")
        connect.commit()
        print(cursor.rowcount, "record inserted.")
        

def inner_join_city_on_country():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM city INNER JOIN COUNTRY ON city.country_id = country.country_id')
        result = cursor.fetchall();
        print(result)
        connect.commit()
        

def left_join_filmid():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM film LEFT JOIN film_actor ON film.film_id = film_actor.film_id')
        result = cursor.fetchall();
        print(result)
        connect.commit()
     

def inner_join_film():
    with sqlite3.connect("sakila.db") as connect:
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM film_actor INNER JOIN film_category ON film_actor.film_id=film_category.film_id ORDER BY film_id;')
        result = cursor.fetchall();
        print(result)
        connect.commit()
       


