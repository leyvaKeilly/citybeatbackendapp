from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .ai_engine import aimodel

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
        userid = q['user']
        featureSettings = q['featureSettings']
        settings = q['settings']
        data = q['data']

        dataBack = aimodel(userid, settings, featureSettings, data)
        print("data")
        print(dataBack)

    except Exception as e:
        return HttpResponseBadRequest(
            json.dumps({
                'error': 'Invalid request: {0}'.format(str(e))
            }),
            content_type="application/json"
        )

    # TODO: run the training function
    response = JsonResponse({
        'data': dataBack
    })
    response['Access-Control-Allow-Origin'] = '*'

    return response
