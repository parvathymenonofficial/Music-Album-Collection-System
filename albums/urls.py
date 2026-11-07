
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(
    'logout/',
    auth_views.LogoutView.as_view(next_page='login'),
    name='logout'
),

    path('', views.home, name='home'),

    path('add/', views.add_album, name='add_album'),

    path('albums/', views.view_albums, name='view_albums'),

    path('edit/<int:id>/', views.edit_album, name='edit_album'),

    path('delete/<int:id>/', views.delete_album, name='delete_album'),

    path('signup/', views.signup, name='signup'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='albums/login.html'
        ),
        name='login'
    ),

]
