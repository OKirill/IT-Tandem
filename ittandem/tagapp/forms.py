from django import forms
# from django.utils.translation import gettext_lazy as _
# from django.urls import reverse_lazy
# from authapp.models import User
from .models import Stack
from django_select2.forms import Select2MultipleWidget, ModelSelect2Widget

# NUMBER_CHOICES = [
#
# ]
# for field in Field.objects.all():
#     stacks = Stack.objects.filter(field=field)
#     for stack in stacks:
#         title = field.name + '/' + stack.name
#         NUMBER_CHOICES.append((stack.id, title))


class TagForm(forms.Form):

    # name = forms.MultipleChoiceField(label='Навыки', choices=NUMBER_CHOICES, widget=Select2MultipleWidget)
    name = forms.ModelMultipleChoiceField(label='Технология', queryset=Stack.objects.all(), widget=Select2MultipleWidget, required=False)


class SearchForm(forms.Form):
    method = 'GET'

    stack = forms.ModelMultipleChoiceField(label='Технология', queryset=Stack.objects.all(), widget=Select2MultipleWidget, required=False)
    # field = forms.ModelChoiceField(
    #     queryset=Field.objects.all(),
    #     label='Направление',
    #     widget=ModelSelect2Widget(
    #         search_fields=['name__icontains'],
    #         max_results=500,
    #         attrs={'data-minimum-input-length': 0,
    #                'onchange': '$("#id_stack").empty();'},
    #     ),
    #     required=False
    # )
    #
    # stack = forms.ModelChoiceField(
    #     queryset=Stack.objects.all(),
    #     label='Стэк',
    #     widget=ModelSelect2Widget(
    #         search_fields=['name__icontains'],
    #         dependent_fields={'field': 'field'},
    #         max_results=500,
    #         attrs={'data-minimum-input-length': 0},
    #     ),
    #     required=False
    # )
