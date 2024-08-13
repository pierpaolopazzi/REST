import requests

################
# RICHIEST GET #
################

my_headers = {"Content-type":"application/json"}

res = requests.get("https://jsonplaceholder.typicode.com/todos", headers=my_headers)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

res = requests.get("https://jsonplaceholder.typicode.com/todos/1", headers=my_headers)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

res = requests.get("https://jsonplaceholder.typicode.com/users/1", headers=my_headers)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

##################
# RICHIESTA POST #
##################

to_insert = {
    "userId": 3,
    "title": "Todo aggiunto #1",
    "completed": False
}
res = requests.post("https://jsonplaceholder.typicode.com/todos", headers=my_headers, json=to_insert)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

user_to_insert = {
    "name": "Giacomo Rossi",
    "username": "Il Giacomino",
    "email": "giacominopanevino@prova.com",
    "address": {
        "street": "Bond St.",
        "suite": "Apt. 556",
        "city": "Glasgow",
        "zipcode": "92998-3874",
        "geo": { "lat": "-37.3159", "lng": "81.1496" }
    },
    "phone": "1-234-567-8910",
    "website": "grindelwald.org",
    "company": {
        "name": "Corona-non-perdona",
        "catchPhrase": "Sono una principessa!",
        "bs": "gotta catch 'em all"
    }
}
res = requests.post("https://jsonplaceholder.typicode.com/users", headers=my_headers, json=user_to_insert)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

#################
# RICHIESTA PUT #
#################

to_put = {
    "userId": 499,
    "title": "Todo sostituito #1",
    "completed": False
}
res = requests.put("https://jsonplaceholder.typicode.com/todos/1", headers=my_headers, json=to_put)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")


user_to_change = {
    "name": "Babbo Pasquale",
    "username": "Pasqualino",
    "email": "pasqualinopanevino@prova.com",
    "address": {
        "street": "Bond St.",
        "suite": "Apt. 556",
        "city": "Glasgow",
        "zipcode": "92998-3874",
        "geo": { "lat": "-37.3159", "lng": "81.1496" }
    },
    "phone": "1-234-567-8910",
    "website": "grindelwald.org",
    "company": {
        "name": "Corona-non-perdona",
        "catchPhrase": "Sono una principessa!",
        "bs": "gotta catch 'em all"
    }
}
res = requests.put("https://jsonplaceholder.typicode.com/users/1", headers=my_headers, json=user_to_change)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")


####################
# RICHIESTA DELETE #
####################

res = requests.delete("https://jsonplaceholder.typicode.com/todos/5", headers=my_headers)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")