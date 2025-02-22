from django.http import HttpResponse
from django.contrib.auth.models import Group


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        admin_group = Group.objects.get(name='admin')
        user_groups = user.groups.all()
        if admin_group in user_groups:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized')

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            user = request.user
            user_groups = user.groups.all()[0]
            user_groups_names = user_groups.name
            if user_groups_names in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized')

        return wrapper_func

    return decorators
