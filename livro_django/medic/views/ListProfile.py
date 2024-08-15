from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def list_view(request):
    return HttpResponse('<h1>Lista!</h1>')