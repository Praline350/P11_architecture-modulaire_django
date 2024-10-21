# Utilisation d'une image de base Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier de dépendances
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

    # Collecter les fichiers statiques pour Django
RUN python manage.py collectstatic --noinput

# Copier tout le code dans le conteneur
COPY . /app/

# Exposer le port 8000
EXPOSE 8000

# Commande pour lancer Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
