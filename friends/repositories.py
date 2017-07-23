# -*- coding: utf-8 -*-
import facebook
from facecrush.settings import APP_ID, APP_SECRET
from users.models import User

class FriendsRepository(object):
    def __init__(self, user_id):
        self.user_id = user_id
        # self.graph = facebook.GraphAPI(self.access_token)

    def get_access_token_by_id(self):
        user = User.objects.filter(user_id=self.user_id)
        # import ipdb; ipdb.set_trace()


    def get_all_friends(self):
        pass
        # friends = graph.get_object('/me/friends')['data']

#Transforma o token padrao de curto tempo, em um token de acesso mais longo
#O token padrao tem curta duraçao porque foi gerada por uma app web
#se fosse gerado pelo sdk do android ou ios, seria maior
# def get_long_access_token(access_token):
#     graph = facebook.GraphAPI(access_token=access_token)
#     return graph.extend_access_token(APP_ID, APP_SECRET)
