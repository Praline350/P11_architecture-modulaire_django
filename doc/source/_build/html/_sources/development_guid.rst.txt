Development Guide
=================

Ce chapitre traitera de la pipeline CI/CD, les outils de dévelopement ainsi que la conteneurisation Docker.

**Pré-requis:**

- Compte GitHub
- Compte DockerHub

**Pipeline GitHub Action**

Pour toutes modifications sur la branche 'master' du repository une pipeline sera exécuté.

Les détails de la pipeline se trouve dans le fichier github/workflow/ci.yml. 

Voici la listes des jobs éxécutés, chaques segments doit être réussi avant le lancement du prochain :

- Initialisation de python et des dépendances
- Exécution du Linting flake8
- lancement des tests et de la couverture des tests ( Necessite plus de 80% de reussite)
- Build Docker avec les tags latest et {#commit}
- Connexion DockerHub
- Push de l'images
- Deploiement sur Render (Voir chapitre 'Deploiement')