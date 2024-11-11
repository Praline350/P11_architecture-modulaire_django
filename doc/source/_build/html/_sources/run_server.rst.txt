Run local server
================

Développement local
-------------------


Le linting et les tests sont gérer avec Pytest, Coverage et Flake8. Le fichier setup.cfg est le fichier de parametrage des ses outils.

Le fichier .coveragerc contient les paramètres de la couverture des tests. ::

        cd Python-OC-Lettings-FR/
    
        # Pour lancer les tests ainsi que coverage
        # le dossier .htmlcov contient les sorties de la couverture Coverage
        
        pytest
        
        # Pour lancer le linting 
        
        Flake8
    
Pour lancer le serveur de développement il est necessaire de **collecter les fichiers statiques:** ::

        python manage.py collectstatic
        python manage.py runserver
        
Le serveur de développement se lance sur http://localhost:8000 ou 127.0.0.1:8000


Run with Docker Image 
---------------------

Il est possible de récupéré l’image de docker de l’application via le DockerHub public.

Ce lancement requiert plusieurs pré-requis :

- L’application DockerDesktop
- Un compte DockerHub

**Récupération de l’image public**

Pour pouvoir lancer l’image présente dans le repository distant vous devez tout d’abord **installer Docker Desktop**. ::

        # Powershell
        # Lorsque le DockerDesktop est lancé.
        
        
        # Pour voir et vérifier les images présentes localement
        docker images
        
        
        # Pour récupérer l'image du dockerhub
        docker pull edwin350/oc_lettings:latest
        
        # Pour lancer l'application
        docker run -it -e "PORT=8000" -e "DEBUG=0" -p 8000:8000 edwin350/oc_lettings:latest

- docker run -it : lance l’image en mode intéractif
- -e ‘PORT=8000’ -e ‘DEBUG=0’ : Intialise les variables d’environnement
- -p 8000:8000 : définie le port utilisé
- edwin350/oc_lettings:latest : Nom et tag de l’image à utiliser

L’application devrais être disponnible à l’adresse : localhost:8000 (ou en fonction du port définie)

