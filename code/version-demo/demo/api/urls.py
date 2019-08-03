from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # path('users/', views.UsersView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/users/$',views.UsersView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/parser/$', views.ParserView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/userInfo/$', views.UserInfoView.as_view()),
]
