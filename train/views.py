from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


# Trains the model on some data
def hello_world(request):
    userid = request.POST.get('userid', '0')
    settings = request.POST.get('settings', {})
    data = request.POST.get('data', False)
    # TODO: run the training function
    return JsonResponse({
        'Here is the "q" parameter from the request': request.GET.get('q', '')
    })


# Sends the database data to the client
def hello_world2(request):
    # TODO: connect to the PostgreSQL database
    # TODO: fetch the data from postgres
    # TODO: return the data as JSON to the client
