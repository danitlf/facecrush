from django.conf.urls import url
from matchs import views

urlpatterns = [
    url(r'^', views.matchs)

]
