from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# model 추가
from .models import Sweeple, Delivery
# random 함수 추가
import random

@csrf_exempt
def action(request):
    if request.method == 'POST':
        # 미친 대문자만 됨?
        req = json.loads(request.body)
        # # get action from json
        # action = req.get('queryResult').get('action')
        # # return a fulfillment message
        
        # 인텐트를 파악합니다
        intent = req.get('queryResult').get('intent').get('displayName')

        
        # 인텐트에 맞게 URL로 보냅니다.
        if intent == "sweeple ad":
            return ad(request)
        elif intent == "sweeple order":
            params = req.get('queryResult').get('parameters')
            return create_delivery(request, params)


def ad(request):
    sweeples = Sweeple.objects.all()
    item = random.choice(sweeples)
    response = {'fulfillmentText': item.taste + ' 스위플은 어떠신가요? ' + item.description}
    return JsonResponse(response, safe=False)


def create_delivery(request, params):
    
    taste = params.get('taste')
    name = params.get('name')
    number = params.get('number')
    item = Delivery(taste = taste, name=name, number=number)
    item.save()
    
    response = {
        'fulfillmentText' : '감사합니다. 주문번호는 {} 입니다.'.format(item.id),
          "outputContexts": [
            {
              "name": "projects/sweeple-delivery-bot-saxdfa/agent/sessions/ec79f53c-31b2-3a18-998f-32cb63c3a6f2/contexts/order",
              "lifespanCount": 1,
              "parameters": {
                "del_number": item.id
              }
            }
      ]
    }
    
    return JsonResponse(response, safe=False)


