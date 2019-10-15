from django import forms
# from django.utils.translation import gettext_lazy as _
# from django.urls import reverse_lazy
from authapp.models import User
from tagapp.models import Stack
from .models import Project
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django_select2.forms import Select2MultipleWidget
from django.utils.translation import gettext_lazy as _


class ProjectForm(forms.Form):
        title = forms.CharField(label=_('Назавание:'))
        desc = forms.CharField(label=_('Описание:'), widget=forms.Textarea())
        tags = forms.ModelMultipleChoiceField(label='Стек заний', queryset=Stack.objects.all(), widget=Select2MultipleWidget)


class ValidPk(forms.Form):
    pk = forms.ModelChoiceField(queryset=None, required=True)


class ValidSlug(forms.Form):
    slug = forms.ModelChoiceField(queryset=None, required=True)
