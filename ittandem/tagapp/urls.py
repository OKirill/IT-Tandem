import os
from django.urls import path
from .views import SkillCreate, DesireCreate, SearchView
from .forms import TagForm, SearchForm

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [

    path('skill/', SkillCreate.as_view(form_class=TagForm), name='SkillCreate'),
    path('desire/', DesireCreate.as_view(form_class=TagForm), name='DesireCreate'),
    path('search/',  SearchView.as_view(), name='DesireCreate')

]