import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_lettings_index_view(client):
    """Test de la vue index qui affiche tous les lettings."""
    
    # Créer des objets Letting avec des adresses différentes
    address1 = Address.objects.create(
        number=123,
        street="Rue de la Paix",
        city="Paris",
        state="IDF",
        zip_code="75001",
        country_iso_code="FR"
    )
    
    address2 = Address.objects.create(
        number=124,
        street="Rue de l'Église",
        city="Lyon",
        state="ARA",
        zip_code="69001",
        country_iso_code="FR"
    )
    
    Letting.objects.create(title="Letting 1", address=address1)
    Letting.objects.create(title="Letting 2", address=address2)

    # Faire une requête à la vue index
    response = client.get(reverse('lettings_index'))
    
    # Vérifier que la page se charge correctement (status code 200)
    assert response.status_code == 200
    
    # Vérifier que les letings apparaissent dans la réponse
    assert b"Letting 1" in response.content
    assert b"Letting 2" in response.content


@pytest.mark.django_db
def test_letting_detail_view(client):
    """Test de la vue de détail pour un letting spécifique."""
    
    # Créer un letting pour le test
    address = Address.objects.create(
        number=123,
        street="Rue de la Paix",
        city="Paris",
        state="IDF",
        zip_code="75001",
        country_iso_code="FR"
    )
    letting = Letting.objects.create(title="Letting Test", address=address)

    # Faire une requête à la vue de détail du letting
    response = client.get(reverse('letting', args=[letting.id]))
    
    # Vérifier que la page se charge correctement (status code 200)
    assert response.status_code == 200
    
    # Vérifier que le contenu du letting apparaît dans la réponse
    assert b"Letting Test" in response.content
    assert b"Rue de la Paix" in response.content


@pytest.mark.django_db
def test_letting_detail_view_404(client):
    """Test de la vue de détail pour un letting qui n'existe pas."""
    
    # Faire une requête à un letting qui n'existe pas
    response = client.get(reverse('letting', args=[999]))  # 999 est un ID qui n'existe pas

    # Vérifier que la page renvoie une erreur 404
    assert response.status_code == 404
