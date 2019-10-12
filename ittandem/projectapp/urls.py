import os
from django.urls import path
from .views import ProjectCreate, ProjectUpdate, ProjectDetail, ProjectDelete, ProjectList, ProjectView
from .forms import ProjectForm

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('user/<int:pk>/', ProjectList.as_view(), name='ProjectList'),
    path('create/', ProjectCreate.as_view(form_class=ProjectForm), name='ProjectCreate'),
    path('<int:pk>/update/', ProjectUpdate.as_view(), name='ProjectUpdate'),
    path('<int:pk>/delete/', ProjectDelete.as_view(), name='ProjectDelete'),
    path('user/detail/<int:pk>/', ProjectDetail.as_view(), name='ProjectDetail'),
    path('', ProjectView.as_view(), name='ProjectView'),
]