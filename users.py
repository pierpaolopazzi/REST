from flask import Flask, request, jsonify

app = Flask(__name__)

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