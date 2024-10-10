"""
Ce module contient les vues pour l'application profiles.

Il inclut la vue qui liste tous les profils (`index`) ainsi que la vue qui affiche
les détails d'un profil individuel (`profile`).
"""

import logging
from django.shortcuts import render, get_object_or_404
from profiles.models import Profile

# Création du logger
logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la liste de tous les profils dans l'application.

    Paramètres :
        request : La requête HTTP reçue.

    Retourne :
        Une réponse HTTP avec le rendu du template de la liste des profils.
    """

    logger.info("Affichage de la liste des profils")
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    logger.debug(f"{len(profiles_list)} profils récupérés")
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Affiche les détails d'un profil en fonction du nom d'utilisateur.

    Paramètres :
        request : La requête HTTP reçue.
        username : Le nom d'utilisateur du profil à afficher.

    Retourne :
        Une réponse HTTP avec le rendu du template de profil ou une erreur 404.
    """

    logger.info(f"Affichage du profil pour l'utilisateur : {username}")
    try:
        # Tentative de récupération du profil avec gestion des erreurs
        profile = get_object_or_404(Profile, user__username=username)
        context = {"profile": profile}
        logger.debug(f"Profil trouvé pour l'utilisateur : {username}")
        return render(request, "profiles/profile.html", context)

    except Profile.DoesNotExist:
        # Log d'avertissement si le profil n'est pas trouvé
        logger.warning(f"Profil non trouvé pour l'utilisateur : {username}")
        raise
