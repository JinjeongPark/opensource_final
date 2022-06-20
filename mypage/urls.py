from django.conf.urls import url
from mypage import views
from django.urls import path

urlpatterns=[
        path(r'^$',views.index,name='index'),
        ]
