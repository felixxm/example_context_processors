from django.conf import settings

from . import __version__


def metadata(request):
    return {"version": __version__, "environment": settings.ENVIRONMENT}
