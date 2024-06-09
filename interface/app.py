from flask import Flask, render_template, request, jsonify
import re
import requests
import sys
import os

# Ajouter le répertoire parent au chemin de recherche de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bot import traiter_message  # Importez la fonction depuis bot.py

app = Flask(__name__)


# Route pour la page d'accueil du chatbot
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Route pour traiter les messages envoyés par l'utilisateur
@app.route("/message", methods=["POST"])
def message():
    # Récupérer le message envoyé par l'utilisateur
    user_message = request.form.get("message")

    # Traiter le message en utilisant la fonction de bot.py
    response = traiter_message(user_message)

    # Renvoie la réponse au format JSON
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
