import os
from django.urls import path
from .views import SearchCreate
from .forms import TestForm

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [

    path('', SearchCreate.as_view(form_class=TestForm), name='django_select2'),

]