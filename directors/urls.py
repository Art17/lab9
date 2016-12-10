from django.conf.urls import url
from . import views
from . import rest_views


urlpatterns = [
    url(r'^create/$', views.CreateView.as_view()),
    url(r'^directors/$', views.DirectorsView.as_view()),
    url(r'^directors/(\d+)/', views.DirectorView.as_view()),
    url(r'^my-admin/$', views.my_admin),

    url(r'^api/directors/$', rest_views.DirectorsAPI.as_view()),
    url(r'^api/directors/(?P<pk>[0-9]+)/$', rest_views.DirectorAPI.as_view()),
    url(r'^api/users/$', rest_views.UsersAPI.as_view()),

    url(r'get-directors/$', views.get_directors)
]