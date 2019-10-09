from django import forms
# from django.utils.translation import gettext_lazy as _
# from django.urls import reverse_lazy
# from authapp.models import User
from mainapp.models import Tag
# from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django_select2.forms import Select2MultipleWidget


class TagForm(forms.Form):

    name = forms.ModelMultipleChoiceField(label='фронтенд', queryset=Tag.objects.all(), widget=Select2MultipleWidget)
    name1 = forms.ModelMultipleChoiceField(label='бэкенд', queryset=Tag.objects.all(), widget=Select2MultipleWidget)