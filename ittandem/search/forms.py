
# from django import forms
# from .models import Tag
from django import forms
# from django.utils.translation import gettext_lazy as _
# from django.urls import reverse_lazy
from authapp.models import User
from search.models import Tag, Parent
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django_select2.forms import Select2MultipleWidget, ModelSelect2Widget


# class TestForm(forms.Form):
#
#     tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(parent_id__isnull=True))
#     tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(parent_id__isnull=False), widget=Select2MultipleWidget)
#
#     def __init__(self, *args, **kwargs):
#         super(TestForm, self).__init__(*args, **kwargs)
#
#         if 0 == len(self.data):
#             # clear queryset if we just show a form
#             self.fields['tag'].queryset = Tag.objects.none()
#
#         # assign a widget to second select field
#         self.fields['tag'].widget = ChainedSelectWidget(
#             parent_name='parents',         # the name of parent field
#             app_name='search',            # the name of model's application
#             model_name='tag',          # the name of a model with the method
#             method_name='chained_relation', # the name of queryset method
#             )


class TestForm(forms.Form):
    country = forms.ModelChoiceField(
        queryset=Parent.objects.filter(),
        label=u"Country",
        widget=ModelSelect2Widget(
            search_fields=['name__icontains'],
            dependent_fields={'parent': 'parents'},
        )
    )

    city = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        label=u"City",
        widget=ModelSelect2Widget(
            search_fields=['name__icontains'],
            dependent_fields={'parent': 'parent'},
            max_results=500,
        )
    )