from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpRequest, FileResponse, Http404
from django.contrib.staticfiles import finders

def about(request: HttpRequest):
    return render(
        request, 'about/about.html'
    )


def favicon(request: HttpRequest):
    path = finders.find("ico/favicon.ico")
    if not path:
        raise Http404("favicon not found")
    if not isinstance(path, str):
        path = path[0]
    return FileResponse(open(path, "rb"), content_type="image/x-icon")
