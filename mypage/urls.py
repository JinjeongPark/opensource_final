from django.conf.urls import url
from mypage import views
from django.urls import path

#urlpatterns=[
 #       path('',views.index,name='index'),
#        ]

urlpatterns=[
        path('',views.index,name='index'),
        ]
