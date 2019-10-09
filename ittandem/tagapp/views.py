from django.shortcuts import render

# Create your views here.
from .forms import TagForm
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View, ListView
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class SkillCreate(FormView):
    template_name = 'tagapp/form.html'
    success_url = '/'

    def form_valid(self, form):
        print(self.request.user.username)
        if self.request.user.id:
            messages.success(self.request, _('Навыки добавлены'))
            for i in form.cleaned_data['name']:
                print(i.id)
            for i in form.cleaned_data['name1']:
                print(i.id)
        return super().form_valid(form)


