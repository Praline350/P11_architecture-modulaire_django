# Utilisation d'une image de base Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier le fichier de dépendances
COPY requirements.txt /app/

# Étape 4 : Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copier tout le code dans le conteneur
COPY . /app/

# Collecter les fichiers statiques pour Django
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Étape 6 : Commande pour lancer le serveur de développement Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]