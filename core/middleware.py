
import datetime

class MyMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response
        
    def __call__(self, request):
        response = self._get_response(request)
        user = request.user
        user.last_login = datetime.datetime.now()
        user.save()
        return response