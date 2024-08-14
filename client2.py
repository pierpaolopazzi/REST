import requests

################
# RICHIEST GET #
################

#api_url= "http://jsonplaceholder.typicode.com"
api_url= "http://localhost:5000"
my_headers = {"Content-type":"application/json"}

print("GET /todos")
res = requests.get(f"{api_url}/todos", headers=my_headers)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

print("\n")
print("GET /todos/1")
res = requests.get(f"{api_url}/todos/1", headers=my_headers)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

print("\n")
print("GET /users/1")
res = requests.get(f"{api_url}/users/1", headers=my_headers)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

##################
# RICHIESTA POST #
##################

print("\n")
print("POST /todos")
to_insert = {
    "userId": 3,
    "title": "Todo aggiunto #1",
    "completed": False
}
res = requests.post(f"{api_url}/todos", headers=my_headers, json=to_insert)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")


print("\n")
print("POST /users")
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
res = requests.post(f"{api_url}/users", headers=my_headers, json=user_to_insert)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

#################
# RICHIESTA PUT #
#################

print("\n")
print("PUT /todos/1")
to_put = {
    "userId": 499,
    "title": "Todo sostituito #1",
    "completed": False
}
res = requests.put(f"{api_url}/todos/1", headers=my_headers, json=to_put)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

print("\n")
print("PUT /users/1")
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
res = requests.put(f"{api_url}/users/1", headers=my_headers, json=user_to_change)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")


####################
# RICHIESTA DELETE #
####################

print("\n")
print("DELETE /todos/5")
res = requests.delete(f"{api_url}/todos/5", headers=my_headers)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")


###################
# NUOVE RICHIESTE #
###################

# Recuperare i todos dell'utente con id 1
print("\n")
print("GET /users/1/todos")
res = requests.get(f"{api_url}/users/1/todos", headers=my_headers)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")


# Inserire un nuovo todo per l’utente 1
print("\n")
print("POST /users/1/todos")
to_insert_new = {
    "title": "Riordinare gli appunti",
    "completed": True, 
    "userId": 1
}
res = requests.post(f"{api_url}/users/1/todos", headers=my_headers, json=to_insert_new)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta dal Server:\n{res.json()}")