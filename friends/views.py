# -*- coding: utf-8 -*-
from django.http import HttpResponse
from repositories import FriendsRepository

def friends(request, **kwargs):
    # graph = facebook.GraphAPI(access_token="EAACEdEose0cBANXyPVeETNvIPsVT9WTA70NTuFu91bR5oIg6dm68RcD71chMYTBO30NbhZCCDvzWpLZAEZB8qq6V4XnelXsQsG1AaDm90mjQyoEZCGbq3VUb2DasbofXeE9GcxPzFe99dQhPgA49VZBvdQb9lZBTVM8be4bWjLtvv2x69r6uyyZAB13QXC79aIZD", version='2.1')
    FriendsRepository(user_id=kwargs['user_id']).get_access_token_by_id()
    return HttpResponse('FRIENDS PAGE!!' + kwargs['user_id'])
