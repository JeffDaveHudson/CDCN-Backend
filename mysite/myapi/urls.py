from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
urlpatterns = [

    path('', include(router.urls)),
    path('book', views.BookManage.as_view()),
    path('book/<int:id>', views.BookManage.as_view()),


    path('api/register', views.UserRegisterView.as_view(), name='register'),
    path('api/login', views.UserLoginView.as_view(), name='login'),

    path('genre', views.GenreManage.as_view()),


    # Recommendation theo user_id
    path('recommend/<int:user>', views.Recommendation.as_view()),


    #get rating by id rating
    path('rating', views.RatingManage.as_view()),
    path('rating/<int:pk>', views.RatingManage.as_view()),

     # Rating theo user_id và book_id
    path('ratingbyuserbook/<int:user>/<int:book>',
         views.RatingByUser_Book.as_view()),
    path('ratingbyuser/<int:user>', views.RatingByUser.as_view()),
         
    # Rating avg theo book_id
    path('ratingavg', views.AverageRating.as_view()),
    path('ratingavg/<int:book>', views.AverageRating.as_view()),

    path('user', views.UserManage.as_view()),
    path('user/<str:pk>', views.UserManage.as_view()),

]
