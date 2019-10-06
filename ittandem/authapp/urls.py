from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    # path('login/', authapp.login, name='login'),
    # path('join/', authapp.join, name='join'),
    # path('<int:pk>/', authapp.UserProfile.as_view(), name='profile'),
    # path('<int:pk>/edit', authapp.edit, name='edit'),
]
