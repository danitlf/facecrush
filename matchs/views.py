# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from matchs.models import Match
from matchs.serializers import MatchSerializer

@csrf_exempt
def matchs(request):
    if request.method == 'GET':
        matchs = Match.objects.all()
        serializer = MatchSerializer(matchs, many=True)
        return JsonResponse(serializer.data, safe=False)

#     if request.method == 'POST':
#         data=JSONParser().parse(request)
#         if not check_match_exists(user_one=data['user_one'], user_two=data['user_two']):
#             create_match(user_one=data['user_one'], user_two=data['user_two'])
#             return JsonResponse('match criado', status=201, safe=False)
#         return JsonResponse('match existente', status=400, safe=False)
# def check_match_exists(user_one, user_two):
#     method = Match.objects.filter
#     return len(method(user_one=user_one, user_two=user_two)) | len(method(user_one=user_two, user_two=user_one))
#
# def create_match(user_one, user_two):
#     Match(user_one=user_one, user_two=user_two).save()
