from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Homepage.as_view(), name='home'),
    url(r'^contact/$', views.Contact.as_view(), name='contact'),
    url(r'^contact/success/$', views.ContactSuccess.as_view(), name='contact-success'),
]