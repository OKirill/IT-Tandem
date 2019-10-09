import authapp.views as authapp
from django.urls import path

app_name = 'authapp'

urlpatterns = [
    # path('login/', authapp.login, name='login'),
    path('join/', authapp.register, name='register'),
    # path('<int:pk>/', authapp.UserProfile.as_view(), name='profile'),
    # path('<int:pk>/edit', authapp.edit, name='edit'),
]
