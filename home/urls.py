from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Homepage.as_view(), name='home'),
]