"""
Ce module contient les tests pour les vues de l'application profiles.
"""

import pytest
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profiles_index_view(client):
    """Test de la vue index qui affiche tous les profils."""

    # Créer des utilisateurs et des profils pour le test
    user1 = User.objects.create(username="user1", password="password")
    user2 = User.objects.create(username="user2", password="password")
    Profile.objects.create(user=user1, favorite_city="Paris")
    Profile.objects.create(user=user2, favorite_city="Lyon")

    # Faire une requête à la vue index
    response = client.get(reverse("profiles_index"))

    # Vérifier que la page se charge correctement (status code 200)
    assert response.status_code == 200

    # Vérifier que les profils apparaissent dans la réponse
    assert b"user1" in response.content
    assert b"user2" in response.content


@pytest.mark.django_db
def test_profile_detail_view(client):
    """Test de la vue de détail d'un profil existant."""

    # Créer un utilisateur et un profil
    user = User.objects.create(username="user1", password="password")
    Profile.objects.create(user=user, favorite_city="Paris")

    # Faire une requête à la vue de détail du profil
    response = client.get(reverse("profile", args=[user.username]))

    # Vérifier que la page se charge correctement (status code 200)
    assert response.status_code == 200

    # Vérifier que le contenu du profil apparaît dans la réponse
    assert b"user1" in response.content
    assert b"Paris" in response.content


@pytest.mark.django_db
def test_profile_detail_view_404(client):
    """Test de la vue de détail pour un profil qui n'existe pas."""

    # Faire une requête pour un profil avec un username qui n'existe pas
    response = client.get(reverse("profile", args=["inexistant"]))

    # Vérifier que la page renvoie une erreur 404
    assert response.status_code == 404
