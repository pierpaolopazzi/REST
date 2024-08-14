from flask import Flask, request, jsonify


app = Flask(__name__)

todos = [
    {"userId": 1, "id": 1, "title": "Fare la spesa", "completed": False},
    {"userId": 1, "id": 2, "title": "Studiare per l'esame", "completed": True},
    {"userId": 2, "id": 3, "title": "Riordinare gli appunti", "completed": True},
    {"userId": 2, "id": 4, "title": "Andare a correre", "completed": False},
]


def _find_next_id(): 
    return max(todo["id"] for todo in todos) + 1


def _find_todo_by_id(t_id):
    for todo in todos:
        if todo["id"] == t_id or todo["id"] == int(t_id):
            return todo
    return None
    

@app.before_request
def check_cont_type_json():
    if not request.is_json:
        return {"errore": "Content-type non supportato (deve essere JSON)"}, 415


# ----- TODOS -----


# Recupera tutti i Todo
@app.get("/todos")
def get_todos():
    return jsonify(todos), 200


# Recupera un Todo dato il suo ID
# Se non lo trova, restituisce un
# oggetto JSON vuoto, ovvero {}, e
# risponde con stato HTTP 404
@app.get("/todos/<t_id>")
def get_todo_by_id(t_id):
    to_return = _find_todo_by_id(t_id)
    if not to_return:
        return jsonify({}), 404 # error
    else:
        return jsonify(to_return), 200 # OK
              


# Crea un nuovo Todo, del quale l'id
# viene impostato al successivo id disponibile
# (come se fosse un autoincrementante)
@app.post("/todos")
def add_todo():
    todo = request.json
    todo["id"] = _find_next_id()
    todos.append(todo)
    return todo, 201



# Modifica/Sostituisce un Todo esistente,
# restituendo al Client la risorsa modificata
# e lo stato HTTP 201
@app.put("/todos/<t_id>")
def put_todo(t_id):
    todo = request.json
    old_todo = _find_todo_by_id(t_id)
    if not old_todo:
        return jsonify({"message":"Not found"}), 404
    todos.remove(old_todo)
    todos.append(todo)
    return todo, 201


# Elimina un Todo esistente
@app.delete("/todos/<t_id>")
def delete_todo(t_id):
    to_return = _find_todo_by_id(t_id)
    if not to_return:
        return jsonify({"message": "Not found"}), 404
    todos.remove(to_return)
    return jsonify({"message": "OK"}), 200


users = [
    {
        "id": 1,
        "name": "Mario Rossi",
        "username": "MR",
        "email": "mario.rossi@test.com",
        "address": {
            "street": "Regent St.",
            "suite": "Apt. 1",
            "city": "London",
            "zipcode": "121212",
            "geo": {"lat": "59.8333129", "lng": "13.592"},
        },
        "phone": "123-456-789",
        "website": "unife.it",
        "company": {
            "name": "Università degli studi di Ferrara",
            "catchPhrase": "ReST",
            "bs": "API",
        },
    },
    {
        "id": 2,
        "name": "Giacomino Iacopino",
        "username": "LB",
        "email": "giacomino@icorti.com",
        "address": {
            "street": "St. James Park",
            "suite": "It's a Park Bro",
            "city": "London",
            "zipcode": "12134342",
            "geo": {"lat": "94.8312366", "lng": "1221.5971991"},
        },
        "phone": "987-654-321",
        "website": "unife.it",
        "company": {
            "name": "Università degli Studi di Ferrara",
            "catchPhrase": "ReST",
            "bs": "API",
        },
    },
]

def _find_next_user_id():
    # Estraggo tutti gli id esistenti
    ids = sorted(user["id"] for user in users)

    # trovo il primo numero mancante
    for i in range(1, len(ids)+1):
        if i not in ids:
            return i
    # se non ci sono buchi, restituisco il successivo
    return len(ids)+1



def _find_user_by_id(u_id):
    for user in users:
        if user["id"] == u_id or user["id"] == int(u_id):
            return user
    return None

@app.before_request
def check_cont_type_json():
    if not request.is_json:
        return {"errore" : "Content-type non supportato (deve essere JSON)"}, 415


# ------ USERS -------

@app.get("/users")
def get_user():
    return jsonify(users), 200

@app.get("/users/<u_id>")
def get_user_by_id(u_id):
    to_return = _find_user_by_id(u_id)
    if not to_return:
        return jsonify({}), 404
    else:
        return jsonify(to_return), 200
    
@app.post("/users")
def add_user():
    user = request.json
    user["id"] = _find_next_user_id()
    users.append(user)
    return user, 201

@app.put("/users/<u_id>")
def put_user(u_id):
    new_change = request.json
    user_to_change = _find_user_by_id(u_id)
    if not user_to_change:
        return jsonify({"Message":"Not found"}), 404
    users.remove(user_to_change)
    users.append(new_change)
    return new_change, 201

@app.delete("/users/<u_id>")
def delete_user(u_id):
    to_return = _find_user_by_id(u_id)
    if not to_return:
        return jsonify({"Message":"Not found"}), 404
    users.remove(to_return)
    return jsonify({"Message":"OK"}), 200

if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)

