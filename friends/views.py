# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from repositories import FriendsRepository
from rest_framework.parsers import JSONParser
from matchs.models import Match

def friends(request, **kwargs):
    friends = FriendsRepository(user_id=kwargs['user_id']).get_all_friends()
    return JsonResponse(friends, status=201 ,safe=False)

@csrf_exempt
def friends_like(request):
    if request.method == 'POST':
        ative, passive = JSONParser().parse(request).items()
        if not Match.objects.filter(user_one=ative[1], user_two=passive[1]):
            import ipdb; ipdb.set_trace()
            #existe like de user_two em user_one?
            mutual = Match.objects.filter(user_one=passive[1], user_two=ative[1])
            if mutual:
                mutual.status = True
                return JsonResponse("match entre{} e {}".format(ative[1], passive[1]) ,safe=False)
            else:
                Match(user_one=ative[1], user_two=passive[1]).save()
                return JsonResponse("{} deu like em {}".format(ative[1], passive[1]) ,safe=False)
        else:
            return JsonResponse("voce ja deu match nessa pessoa", safe=False)
    else:
        return JsonResponse('required POST method')
