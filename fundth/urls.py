from django.conf.urls import patterns, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # ex: /fundth/
    url(r'^$', views.index, name='index'),
]
