from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def handler404(request, exception):
    return render(request, "errors/404.html", status=404)


def handler500(request):
    return render(request, "errors/500.html", status=500)
