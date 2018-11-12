from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_list.as_view(), name='post_list'),
    path('post/<int:pk>/', views.Post_Detail.as_view(), name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.Post_Edit.as_view(), name='post_edit'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),

]