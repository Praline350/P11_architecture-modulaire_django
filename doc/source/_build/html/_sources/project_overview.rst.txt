Project Overview
================
Project Description
-------------------

**Orange County Lettings** est une start-up dans le secteur de la location de biens immobiliers. Le site permet de consulter plusieurs lieux de location ainsi que les profils des utilisateurs.

Ce projet appartient au parcours de formation OpenClassrooms pour le parcours "Développeur d'application Python".

Cette documentation est un guide d'utilisation pour le développement. Il contient toutes les informations nécessaires au bon fonctionnement de l’application en local, ainsi que pour le déploiement automatisé via sa pipeline CI/CD.


Technical Overview
------------------

La projet s'articule autour de plusieurs technologies :

- **Python / Django** : pour le développement backend de l'application
    - **Tests** : réalisés avec Pytest et Coverage pour la couverture de code
    - **Linting** : utilisation de Flake8 pour vérifier la conformité du code
    - **WSGI** : Gunicorn pour le serveur d'application en production
    - **StaticFiles** : Module WhiteNoise pour servir les fichiers statiques
- **Github / GitAction** : pour le versionning et la gestion de la pipeline CI
- **Sentry** : pour la journalisation et le suivi des erreurs
- **Docker** : pour la conteneurisation de l'application
- **Render** : pour le déploiement de l'application en production

**Options d'utilisation** :

- **En local** : avec le serveur de développement de Django
- **En local via Docker** : pour une configuration plus proche de la production
- **Déploiement via Render** : en production pour l'utilisation finale

