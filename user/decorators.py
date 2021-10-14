from django.http import HttpResponse
from django.shortcuts import redirect


def authenticated_user(main_func):

    def wrapper_func(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('home')

        else:
            return main_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_groups=[]):

    def decorator(main_func):

        def wrapper_func(request, *args, **kwargs):
            group = None

            if request.user.groups.exists():

                group = request.user.groups.all()[0].name

            if group in allowed_groups:
                return main_func(request, *args, **kwargs)

            return HttpResponse('You are not allowed to access this page')
        return wrapper_func
    return decorator


def admin_only_access(main_func):
    def wrapper_func(request, *args, **kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'member':
            return redirect('user-profile')

        if group == 'admin':
            return main_func(request, *args, **kwargs)

    return wrapper_func
