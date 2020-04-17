from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import requests
import json

# for database connection
#import psycopg2
#import os
#DATABASE_URL = os.environ['DATABASE_URL']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Create your views here.
# Trains the model on some data

@csrf_exempt
def hello_world(request):
    try:
        q = json.loads(request.body.decode('utf-8'))
        userid = q['userid']
        settings = q['settings']
        data = q['data']
    except Exception as e:
        return HttpResponseBadRequest(
            json.dumps({
                'error': 'Invalid request: {0}'.format(str(e))
            }),
            content_type="application/json"
        )
    
    # TODO: run the training function
    response = JsonResponse({
        'Here is the "q" parameter from the request': q
    })
    response['Access-Control-Allow-Origin'] = '*'
    # response['Access-Control-Allow-Credentials'] = 'True'
    # response["Access-Control-Allow-Methods"] = 'GET,HEAD,OPTIONS,POST,PUT'
    # response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
    return response

# def hello_world(request):
#    r = requests.get('http://httpbin.org/status/418')
#    print(r.text)
#    return HttpResponse('<pre>' + r.text + '</pre>')
