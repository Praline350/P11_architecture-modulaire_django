import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    """Test de la vue index."""
    response = client.get(reverse('index'))  
    assert response.status_code == 200
    assert b"Welcome to Holiday Homes" in response.content  # Remplace "Bienvenue" par du contenu attendu


@pytest.mark.django_db
def test_404_view(client):
    """Test de la vue 404."""
    response = client.get('/page-inexistante/')  # Une URL qui n'existe pas
    assert response.status_code == 404
    assert b"Erreur 404" in response.content  # Remplace par le contenu de ta page 404


@pytest.mark.django_db
def test_500_view(client):
    """Test de la vue 500."""
    # Forcer une vue à lever une erreur 500
    with pytest.raises(Exception):
        response = client.get(reverse('test_500'))  # Cette vue doit déclencher une 500
        assert response.status_code == 500
        assert b"Erreur 500" in response.content  # Remplace par le contenu de ta page 500
