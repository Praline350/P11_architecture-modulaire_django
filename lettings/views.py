"""
Ce module contient les vues pour l'application lettings.

Il inclut la vue qui liste tous les lettings (`index`) ainsi que la vue qui affiche
les détails d'un letting individuel (`letting`).
"""

import logging
from django.shortcuts import render, get_object_or_404
from lettings.models import Letting


logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la liste de tous les lettings dans l'application.

    Paramètres :
        request : La requête HTTP reçue.

    Retourne :
        Une réponse HTTP avec le rendu du template de la liste des lettings.
    """
    logger.info("Affichage de la liste des lettings")
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    logger.debug(f"{len(lettings_list)} profils récupérés")
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Affiche les détails d'un letting en fonction de son ID.

    Paramètres :
        request : La requête HTTP reçue.
        letting_id : ID du letting à afficher.

    Retourne :
        Une réponse HTTP avec le rendu du template du letting ou une erreur 404.
    """

    logger.info(f"Affichage du letting {letting_id}")
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        logger.debug(f"Letting {letting_id} trouvé")
        return render(request, "lettings/letting.html", context)

    except Letting.DoesNotExist:
        logger.warning(f"Letting avec l'ID {letting_id} non trouvé")
        raise
