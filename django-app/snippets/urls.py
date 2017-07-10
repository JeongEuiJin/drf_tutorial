from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SnippetList.as_view(),name='snippet-list'),
    url(r'^(?P<pk>\d+)/$', views.SnippetDetail.as_view(),name='snippet-detail'),
    url(r'^(?P<pk>\d+)/highlight/$', views.SnippetHighlight.as_view(),name='snippet-highlight'),

]
