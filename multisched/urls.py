from django.conf.urls import url
from .views import hello_view

urlpatterns = [
    url(r'^say-hello$', hello_view, name='hello_view'),
]