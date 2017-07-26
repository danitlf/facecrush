# -*- coding: utf-8 -*-
from django.http import JsonResponse
from repositories import FriendsRepository

def friends(request, **kwargs):
    friends = FriendsRepository(user_id=kwargs['user_id']).get_all_friends()
    return JsonResponse(friends, status=201 ,safe=False)
