from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^create/$", views.create, name="create"),
    url(r"^create_ajax/$", views.create_ajax, name="create_ajax"),
    url(r"^create_json/$", views.create_json, name="create_json"),
    url(r"^(?P<tweet_id>\d+)/like$", views.like, name="like"),
    url(r"^(?P<tweet_id>\d+)/unlike$", views.unlike, name="unlike"),
    url(r"^(?P<user_id>\d+)/$", views.show, name="show")
]