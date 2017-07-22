# -*- coding: utf-8 -*-
from django.http import HttpResponse

def friends(request):
    return HttpResponse('FRIENDS PAGE!!')
