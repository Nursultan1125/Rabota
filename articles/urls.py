from django.conf.urls import url
from django.contrib import admin
from articles import views as article_views


urlpatterns = [
    url(r'^(?P<id>\w+)/$', article_views.get_artcile, name='get_article'),
]