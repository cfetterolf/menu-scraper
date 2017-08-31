from django.conf.urls import url
from scrape import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^detail/$', views.DetailPageView.as_view()),
]
