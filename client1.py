import requests

################
# RICHIEST GET #
################

my_headers = {"Content-type":"application/json"}
res = requests.get("www.example.com/todos", headers=my_headers)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")

##################
# RICHIESTA POST #
##################

to_insert = {
    "title":"Lavare i piatti",
    "completed": False,
    "userId": 123,
}
res = requests.post("www.example.com/todos", headers=my_headers, json=to_insert)
print(f"Stato HTTP: {res.status_code}")
print(f"Risposta:\n{res.json()}")
