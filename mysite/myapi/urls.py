from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
urlpatterns = [

    path('', include(router.urls)),
    path('book', views.BookManage.as_view()),
    path('book/<int:id>', views.BookManage.as_view()),

    path('api/register', views.UserRegisterView.as_view(), name='register'),
]
