from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/$', include('users.urls')),
    url(r'^friends/', include('friends.urls')),
    url(r'^matchs/', include('matchs.urls'))

]
