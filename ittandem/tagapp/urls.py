import os
from django.urls import path
from .views import SkillCreate
from .forms import TagForm

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [

    path('', SkillCreate.as_view(form_class=TagForm), name='SkillCreate'),
    # path('', get_name, name='get_name'),
]