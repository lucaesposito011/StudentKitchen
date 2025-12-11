from flask import Flask, render_template, request, jsonify, session, redirect
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")  #Connessione a MongoDB
db = client["studentkitchen"]

utenti = db["utenti"]
ricette = db["ricette"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registrazione')
def pagina_registrazione():
    return render_template('registrazione.html')

@app.route('/login')
def pagina_login():
    return render_template('login.html')

@app.route('/api/registrazione', methods=['POST'])
def api_registrazione():

    dati = request.get_json()

    nome = dati.get("nome")
    cognome = dati.get("cognome")
    email = dati.get("email")
    password = dati.get("password")

    if utenti.find_one({"email": email}):
        return jsonify({"ok": False, "message": "Email già registrata! Riprova."})

    password_hash = generate_password_hash(password)

    utenti.insert_one({
        "nome": nome,
        "cognome": cognome,
        "email": email,
        "password": password_hash,
        "preferiti": []
    })

    return jsonify({"ok": True, "message": "Registrazione completata!"})

app.secret_key = "studentkitchensessionholder"  #necessaria per usare sessioni

@app.route('/api/login', methods=['POST'])
def api_login():

    dati = request.get_json()

    email = dati.get("email")
    password = dati.get("password")

    user = utenti.find_one({"email": email})
    if not user:
        return jsonify({"ok": False, "message": "Email non registrata! Riprova."})

    if not check_password_hash(user["password"], password):
        return jsonify({"ok": False, "message": "Password errata! Riprova."})

    session["email"] = email #Salvataggio sessione

    return jsonify({"ok": True, "message": "Login effettuato! Bentornato."})

@app.route('/home')
def pagina_home():
    if "email" not in session:
        return redirect("/login")
    return render_template("home.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route("/api/ricerca", methods=["POST"])
def ricerca_ricette():
    dati = request.json
    ingredienti_scelti = dati.get("ingredienti", [])

    risultati = list(ricette.find({
        "listaingredienti": {"$in": ingredienti_scelti}}))

    for r in risultati:
        r["_id"] = str(r["_id"]) #Convertire ObjectId in stringa per evitare errori JSON

    return jsonify(risultati)

@app.route("/risultati")
def pagina_risultati():
    return render_template("risultati.html")

@app.route("/ricetta/<id>")
def pagina_ricetta(id):

    ricetta = ricette.find_one({"_id": ObjectId(id)})

    ricetta["_id"] = str(ricetta["_id"])  #Convertire ObjectId in stringa per evitare errori JSON

    return render_template("ricetta.html", ricettascelta=ricetta)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
