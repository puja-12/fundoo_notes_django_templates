from django.db import connection

from user.models import MiddlewareDetails


class NoteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request,*args,**kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # response = self.get_response(request)

        # user=MiddlewareDetails.objects.values("url")
        # print(user.url)
        if request.method == 'POST':
            method = request.method
            url = request.path
            count = url.count("url")
            # print(count , "jfdvj")
            # print(method)
            # print(url)
            if count <= 0:
                # count = url.count("url")
                MiddlewareDetails.objects.create(request_method=method, url=url,count=count)
                # print(count)
            else:


                count = count + 1
                # print(count)

        response = self.get_response(request)
        return response
