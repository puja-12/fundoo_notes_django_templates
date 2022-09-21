from django.db import connection
from django.db.models import Count

from user.models import MiddlewareDetails


class NoteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # if request.method == 'POST':
        method = request.method
        url = request.path
        count = MiddlewareDetails.objects.values('url').annotate(Count('url'))
        # count1 = url.count("url")
        print(count, "count")

        print("values", count[0]['url__count'])
        c = count[0]['url__count']
        print(c)

        if count == 0:

            MiddlewareDetails.objects.create(request_method=method, url=url, count=count)
            print("inside")


        else:
            count =+  1
            print(count)
            a = MiddlewareDetails.objects.update( count=c)
            print("update", a)

        # response = self.get_response(request)
        return response
