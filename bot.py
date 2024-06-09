import os
import openai
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier config.env
load_dotenv(
    "/mnt/d/Projects/chatBot/config.env"
)  # Remplacez par le chemin réel vers config.env

# Définir la clé API OpenAI à partir des variables d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")


def traiter_message(message):
    try:
        # Utiliser l'API OpenAI pour générer une réponse avec GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Spécifiez le modèle GPT-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            max_tokens=150,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"


import os
import openai
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier config.env
load_dotenv(
    "/mnt/d/Projects/chatBot/config.env"
)  # Remplacez par le chemin réel vers config.env

# Définir la clé API OpenAI à partir des variables d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")


def traiter_message(message):
    try:
        # Utiliser l'API OpenAI pour générer une réponse avec GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Spécifiez le modèle GPT-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            max_tokens=150,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"
