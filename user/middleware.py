from user.models import MiddlewareDetails


class NoteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if request.method == 'POST':
            # user=MiddlewareDetails.objects.values("url")
            # print(user.url)
            method = request.method
            url = request.path
            print(method)
            print(url)
            MiddlewareDetails.objects.create(request_method=method, url=url)

        return response
