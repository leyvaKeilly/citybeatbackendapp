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
