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


if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)

