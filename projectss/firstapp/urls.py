from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.base, name='base'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),  # Custom login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', views.about, name='about'),
    path('ContactUs/', views.ContactUs, name='ContactUs'),
    path('my_account/', views.my_account, name='my_account'),
    path('submit_workspace/', views.submit_workspace, name='submit_workspace'),
    path('insertws/', views.insertws, name='insertws'),
]
