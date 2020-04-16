from django.shortcuts import render
from django.http import JsonResponse
import requests

# for database connection
#import psycopg2
#import os
#DATABASE_URL = os.environ['DATABASE_URL']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Create your views here.
# Trains the model on some data


def hello_world(request):
    userid = request.POST.get('userid')
    settings = request.get('settings')
    data = request.get('data')
    # TODO: run the training function
    response = JsonResponse({
        'Here is the "q" parameter from the request': userid,
        'settings': settings,
        'data': data
    })
    response['Access-Control-Allow-Origin'] = '*'

    return response

# def hello_world(request):
#    r = requests.get('http://httpbin.org/status/418')
#    print(r.text)
#    return HttpResponse('<pre>' + r.text + '</pre>')
