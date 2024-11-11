Quickstart Guide
================

**Prérequis**

- Compte GitHub avec accès en lecture à ce repository
- Git CLI pour cloner le dépôt
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` dans votre shell exécute l'interpréteur Python spécifié ci-dessus (à moins qu'un environnement virtuel ne soit activé).

1. **Cloner le repository** ::

    cd /path/to/put/project/in
    git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git::

2. **Créer l'environnement virtuel** ::

    cd /path/to/Python-OC-Lettings-FR
    python -m venv venv
    apt-get install python3-venv (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
    
    # macOs/Linus 
    Activer l'environnement source venv/bin/activate
    #Window
    Activer l'environnement source venv/Scripts/activate

3. **Install les dépendances dans l'env** ::
        
    pip install -r requirements.txt

4. **Créer un fichier `.env` à la racine du projet, puis ajouter les lignes suivantes** ::

    SECRET_KEY={VOTRE CLEF SECRET DJANGO}
    SENTRY_DSN={LIEN DSN POUR SENTRY} 
    DOCKER_USERNAME={VOTRE USERNAME POUR DOCKERHUB}
    DOCKER_PASSWORD{MOT DE PASSE POUR DOCKERHUB}
    
    # Les variables DOCKER_ sont nécessaires uniquement pour la création
      d'images Docker et sont optionnelles pour le lancement en local.

**Journalisation Sentry**

Pour avoir la journalisation des erreurs avec sentry:

- Créer un compte sur sentry
- Récupérer le sentry_DSN et le copier dans le .env

Vous pourrez alors avoir accès au logs d'erreurs sur votre Dashboard Sentry

