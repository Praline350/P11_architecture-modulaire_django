from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente un profil d'utilisateur dans l'application.

    Attributs :
        user : Un objet User lié au profil.
        favorite_city : Une chaîne de caractères représentant la ville préférée de l'utilisateur.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "oc_lettings_site_profile"
