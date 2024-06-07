# Importez les bibliothèques nécessaires
import re
import requests

# Définissez des fonctions pour traiter les messages de l'utilisateur
def traiter_message(message):
    # Effectuez un traitement du langage naturel basique (optionnel)
    message = message.lower()
    message = re.sub(r"[^\w\s]", "", message)

    # Répondez au message de l'utilisateur en fonction de sa logique conversationnelle
    if message == "bonjour":
        return "Bonjour à vous !"
    elif message == "comment vas-tu ?":
        return "Je vais bien, merci ! Et vous ?"
    else:
        return "Je ne comprends pas bien votre message."

# Boucle principale
while True:
    # Recevez le message de l'utilisateur
    message_utilisateur = input("Utilisateur : ")

    # Traitez le message de l'utilisateur
    reponse_bot = traiter_message(message_utilisateur)

    # Affichez la réponse du bot
    print(f"Bot : {reponse_bot}")
