from django.contrib.auth import get_user_model

def name(request):
    if request.user.is_authenticated:
        username = request.user.username
        return {'username': username}
    else:
        return {}
