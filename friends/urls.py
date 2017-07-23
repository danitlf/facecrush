from django.conf.urls import url
from friends import views

urlpatterns = [
    url(r'(?P<user_id>[0-9]{1,100})/$', views.friends),

]
