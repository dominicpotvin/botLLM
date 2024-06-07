## Projet de bot local avec Python et Flask

Ce projet implémente un bot local avec Python et Flask, offrant une interface graphique de type chatbot.

**Fonctionnalités:**

- Interaction conversationnelle avec le bot
- Interface utilisateur graphique simple
- Traitement du langage naturel basique (optionnel)
- Intégration possible avec des API externes (optionnel)

**Structure du projet:**

- `README.md`: Ce fichier décrit le projet
- `bot.py`: Script principal du bot
- `requirements.txt`: Liste des dépendances Python
- `venv`: Environnement virtuel Python (optionnel)
- `interface`:
  - `templates`: Templates HTML pour l'interface
    - `base.html`: Template de base
    - `index.html`: Template principal
  - `static`: Ressources statiques
    - `css`: Feuilles de style CSS
      - `style.css`: Style principal
    - `js`: Scripts JavaScript
      - `script.js`: Script principal
  - `app.py`: Script Flask pour l'interface

**Installation:**

1. Clonez ou téléchargez le code du projet.
2. Installez les dépendances Python dans un environnement virtuel (si nécessaire) : `pip install -r requirements.txt`

   python3 -m venv botTelepresence
   source botTelepresence/bin/activate
   pip3 install -r requirements.txt

3. Lancez le script Flask : `python app.py`
4. L'interface du chatbot devrait s'ouvrir dans votre navigateur web.

**Utilisation:**

- Tapez vos messages dans le champ de saisie et appuyez sur Entrée pour interagir avec le bot.
- Le bot répondra à vos messages en fonction de sa logique conversationnelle.

**Personnalisation:**

- Modifiez le code de `bot.py` pour implémenter la logique conversationnelle souhaitée.
- Personnalisez les templates HTML dans `interface/templates` pour adapter l'apparence de l'interface.
- Ajoutez des fonctionnalités JavaScript dans `interface/static/js` pour enrichir l'interactivité de l'interface.
- Intégrez des API externes dans `bot.py` pour étendre les capacités du bot.

**Remarques:**

- Ce projet est un point de départ et peut être développé pour répondre à vos besoins spécifiques.
- N'hésitez pas à consulter la documentation de Python et Flask pour approfondir vos connaissances.

**Étapes de démarrage et d'environnement:**

- Ouvrez un terminal et accédez au répertoire du projet.
- Créez un environnement virtuel : "python3 -m venv botTelepresence"
- Activez l'environnement virtuel : "source botTelepresence/bin/activate"
- Installez les dépendances Python : "pip3 install -r requirements.txt"
- Accédez au répertoire interface : "cd interface"
- Lancez le script Flask : "python3 app.py"
- L'interface du chatbot devrait s'ouvrir dans votre navigateur web.
- Pour désactiver l'environnement virtuel, tapez simplement "deactivate" dans le terminal.
