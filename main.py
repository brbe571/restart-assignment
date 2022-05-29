from fastapi import FastAPI
import queries
import hashlib

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/actors")
def all_actors():
    actors = queries.getActors()
    return actors

@app.get("/film_year")
def year_film():
    film = queries.film_year()
    return film

@app.get("/actor_named_wood")
def actor_named_wood():
    actor = queries.actor_name_wood()
    return actor

@app.get("/post_code")
def post_code():
    code = queries.postal_code()
    return code

@app.get("/city")
def id_city():
    id = queries.city_id()
    return id

@app.get("/district")
def city_district():
    district = queries.district()
    return district

@app.get("/country")
def country():
    country = queries.country()
    return country

@app.get("/film_title")
def title():
    film_title = queries.film_title()
    return film_title

@app.get("/personnel")
def personnel():
    staff = queries.staff()
    return staff

@app.get("/payment")
def payment():
    amount = queries.payment_amount()
    return amount

@app.delete("/language")
def delete_language():
    deleted_language = queries.delete_language()
    return deleted_language

@app.put("/update_category")
def update_category():
    category = queries.update_category()
    return category

@app.post("/add_language")
def add_language():
    language = queries.add_language()
    return language

@app.post("/add_actor")
def add_actor():
    actor= queries.add_actor()
    return add

@app.post("/add_country")
def add_country():
    country = queries.add_country()
    return country

@app.post("/add_city")
def add_city():
    city = queries.add_city()
    return city

@app.post("/add_category")
def add_category():
    category = queries.add_category()
    return category

@app.get("/join_on_countryid")
def join_on_countryid():
    join = queries.inner_join_city_on_country()
    return join

@app.get("/left_join_filmid")
def left_join_filmid():
    join = queries.left_join_filmid()
    return join

@app.get("/inner_join_film")
def inner_join_film():
    join = queries.inner_join_film()
    return join

@app.post("/hash_password")
def encrypt_password(password):
    sha = hashlib.sha256()
    sha.update(password.encode())
    return sha.hexdigest()


    


