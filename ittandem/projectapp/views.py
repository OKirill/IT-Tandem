from django.views.generic import DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from authapp.models import User
from .models import Project
from .forms import ValidPk, ValidSlug
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q


class ProjectGetMixin(object):

    def get(self, *args, **kwargs):
            project_id = kwargs['pk']
            for project in Project.objects.filter(pk=project_id):
                owner = project.owner.id
            if owner != self.request.user.id:
                messages.success(self.request, _(f'Вы не имеете права редактировать данный контент'))
                return HttpResponseRedirect('/')
            return super().get(self.request, *args, **kwargs)


class ProjectView(ListView):
    """Отображение всех проектов"""
    model = Project
    template_name = 'projectapp/project_list.html'


class ProjectList(LoginRequiredMixin, ListView):
    """Отображение проектов конткретного пользователя"""
    model = Project
    slug = 'user__username__icontains'
    pk_field = 'owner__id'
    model_form_test = User
    template_name = 'projectapp/project_list.html'

    def get_queryset(self):
        query = Q()
        if 'pk' in self.kwargs:
            form = ValidPk(self.kwargs)
            form.fields['pk'].queryset = self.model_form_test.objects
            if form.is_valid():
                query = Q((self.pk_field, self.kwargs['pk']))
        if 'slug' in self.kwargs:
            form = ValidSlug(self.kwargs)
            form.fields['slug'].queryset = self.model_form_test.objects
            if form.is_valid():
                query = Q((self.slug, self.kwargs['slug']))
        return super().get_queryset().filter(query)


class ProjectCreate(FormView):
    """Создание проекта"""
    template_name = 'projectapp/formcreate.html'
    success_url = reverse_lazy('project:ProjectView')

    def get(self, *args, **kwargs):
        if not self.request.user.id:
            messages.success(self.request, _(f'Необходимо войти или зарегестрироваться'))
            return HttpResponseRedirect('/')
        return super().get(self.request, *args, **kwargs)

    def form_valid(self, form):
        instance = Project.objects.create(owner=self.request.user, name=form.cleaned_data['title'], desc=form.cleaned_data['desc'])
        instance.tags.set(form.cleaned_data['tags'])
        messages.success(self.request, _(f'Проект сохранен'))
        return super().form_valid(form)


class ProjectUpdate(SuccessMessageMixin, ProjectGetMixin, LoginRequiredMixin, UpdateView):
    """Обновление проекта"""
    success_url = reverse_lazy('project:ProjectView')
    model = Project
    template_name = 'projectapp/formcreate.html'
    fields = ['name', 'short_desc', 'desc', 'tags']
    success_message = _('Проект изменен')


class ProjectDetail(DetailView):
    """Класс отображения одного проекта"""
    model = Project
    template_name = 'projectapp/project_detail.html'


class ProjectDelete(LoginRequiredMixin, ProjectGetMixin, DeleteView):
    """Класс удаления проекта"""
    success_url = reverse_lazy('project:ProjectView')
    template_name = 'projectapp/project_confirm_delete.html'
    model = Project

    def get_success_url(self):
        messages.success(self.request, _('Товар удален'))
        return self.success_url.format(**self.object.__dict__)