from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# model 추가
from .models import Sweeple
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
        if intent == "스위플광고":
            return ad(request)


def ad(request):
    sweeples = Sweeple.objects.all()
    item = random.choice(sweeples)
    fulfillmentText = {'fulfillmentText': item.taste + ' 스위플은 어떠신가요? ' + item.description}
    return JsonResponse(fulfillmentText, safe=False)

