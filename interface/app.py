from flask import Flask, render_template, request, jsonify
import re
import requests

app = Flask(__name__)


# Route pour la page d'accueil du chatbot
@app.route('/', methods=['GET'])
def index():
    return render_template('interface/index.html')

# Route pour traiter les messages envoyés par l'utilisateur
@app.route('/message', methods=['POST'])



def message():
    # Récupérer le message envoyé par l'utilisateur
    user_message = request.form.get('message')

    # Traiter le message (par exemple, appeler une API externe)
    response = "Je suis un chatbot en cours de développement. Je ne peux pas encore répondre à toutes les questions."

    # Renvoie la réponse au format JSON
    return jsonify({'response': response})
