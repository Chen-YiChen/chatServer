from django.conf.urls import url
from chatData import views

urlpatterns = [
        url(r'^login/$', views.login),
]
