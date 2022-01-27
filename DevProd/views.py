import os
from django.http import JsonResponse
from .settings.env_status import Env

def get_status(request):
    return JsonResponse({"env": Env.environment})
    #return os.environ['My_server_version']