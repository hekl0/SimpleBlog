from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup', views.signup, name='signup'),
    path('addpost', views.addPost, name='addpost'),
    path('like', views.like, name='like'),
    path('dislike', views.dislike, name='dislike'),
    path('liked', views.liked_list, name='liked_list'),
]