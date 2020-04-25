from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
#import requests
import json
from .ai_engine import aimodel


@csrf_exempt
def hello_world(request):
    try:
        # getting data from request
        q = json.loads(request.body.decode('utf-8'))
        userid = q['user']
        featureSettings = q['featureSettings']
        settings = q['settings']
        data = q['data']

        # running ai algorithm
        dataBack = aimodel(userid, settings, featureSettings, data)
        print(dataBack)

    except Exception as e:
        return HttpResponseBadRequest(
            json.dumps({
                'error': 'Invalid request: {0}'.format(str(e))
            }),
            content_type="application/json"
        )

    # return response to frontend
    response = JsonResponse({
        'data': dataBack
    })
    response['Access-Control-Allow-Origin'] = '*'

    return response
