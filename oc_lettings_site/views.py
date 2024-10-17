"""
Ce module contient les vues pour l'application profiles.

Il inclut les vue de l'index ainsi que les vues personnalisé pour les pages errors(404, 500).
"""

import logging
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "index.html")


def handler404(request, exception):
    logger.error(f"Erreur 404 : Page non trouvée pour {request.path}")
    return render(request, "errors/404.html", status=404)


def handler500(request):
    logger.error("Erreur 500 : Erreur serveur", exc_info=True)
    return render(request, "errors/500.html", status=500)


def test_log_view(request):
    try:
        return 1 / 0
    except ZeroDivisionError as e:
        logger.error("Erreur de division par zéro", exc_info=e)
        return HttpResponse("Une erreur est survenue.", status=500)
