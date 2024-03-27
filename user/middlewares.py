from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


class AddUserToContextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = request.user if request.user.is_authenticated else None
        response = self.get_response(request)
        return response


class RedirectToLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path != reverse('login'):
            print('RedirectToLoginMiddleware')
            return HttpResponseRedirect(reverse('login'))
        return self.get_response(request)
