from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def action(request):
    # if request.method == 'post':
        # build a request object
        req = json.loads(request.body)
        # get action from json
        action = req.get('queryResult').get('action')
        # return a fulfillment message
        fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}
        # return response
        return JsonResponse(fulfillmentText, safe=False)
    
