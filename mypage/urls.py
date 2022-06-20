from django.conf.urls import url
from mypage import views
from django.urls import path
from django.conf.urls import include
#app_name='mypage'
#urlpatterns=[
 #       path('',views.index,name='index'),
#        ]

urlpatterns=[
        path('',views.index,name='index'),
        path('profile.html/',views.profile,name='profile'),
        path('hobby.html/',views.hobby,name='hobby'),
        path('index.html/',views.index,name='home'),
        path('favorite_song.html/',views.favorite_song,name='favorite_song'),
        ]

