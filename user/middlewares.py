class AddUserToContextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = request.user if request.user.is_authenticated else None
        response = self.get_response(request)
        return response
