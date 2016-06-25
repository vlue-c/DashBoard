from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_page, name='login_page'),
    url(r'^main$', views.login, name='login'),
    url(r'^signup$', views.signup_page, name='signup'),
]
