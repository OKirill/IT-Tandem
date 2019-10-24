from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    # path('join/', authapp.join, name='join'),
    path('logout/', authapp.logout, name='logout'),
    path('profile/<int:pk>/', authapp.UserProfile.as_view(), name='profile'),
    # path('<int:pk>/edit', authapp.edit, name='edit'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
    # path('profile/', authapp.profile, name='profile'),
    path('deal/<int:pk>/', authapp.DealUpdate.as_view(), name='deal'),
]
