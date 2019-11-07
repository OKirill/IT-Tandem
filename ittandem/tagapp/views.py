from django.views.generic import FormView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views.generic import UpdateView, CreateView, ListView
# from django.contrib.auth.mixins import PermissionRequiredMixin
from authapp.models import User
from .forms import TagForm, SearchForm
# from django.forms.models import inlineformset_factory
from tagapp.models import Skill, Desire, Stack
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


class TagCreateMixin(FormView):
    template_name = 'tagapp/form.html'
    success_url = None
    model_tag = None
    form_class_tag = None

    def get(self, request):
        return HttpResponseRedirect('/')

    def form_valid(self, form):
        if self.request.user.id:
            self.model_tag.objects.filter(user=self.request.user).delete()
            for skill in form.cleaned_data['name']:
                self.model_tag.objects.create(tag=skill, user=self.request.user)
            messages.success(self.request, _(f'Навыки сохранены'))
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        skills = []
        for skill in self.model_tag.objects.filter(user=self.request.user):
            skills.append(skill.tag_id)
        kwargs['form'] = self.form_class_tag(initial={'name': skills})
        return kwargs


class SkillCreate(TagCreateMixin):
    template_name = 'tagapp/form.html'
    success_url = '/tags/skill/'
    model_tag = Skill
    form_class_tag = TagForm


class DesireCreate(TagCreateMixin):
    template_name = 'tagapp/form.html'
    success_url = '/tags/desire/'
    model_tag = Desire
    form_class_tag = TagForm


class SearchMixin(ListView):
    template_name = 'tagapp/search_form.html'
    model = User
    forms_filter = [SearchForm]
    search_form = None
    model_tag = None

    def get_queryset(self):
        queryset = super().get_queryset()
        users = Skill.objects.values('user_id').distinct()
        sta = False
        for form_class in self.forms_filter:
            if self.request.method == form_class.method:
                if 'stack' in self.request.GET:
                    if not self.request.GET['stack'].isdigit() and self.request.GET['stack'] != '':
                        sta = True
                if sta:
                    self.search_form = form_class()
                else:
                    self.search_form = form_class(self.request.GET)
                if self.search_form.is_valid():
                    if 'stack' in self.request.GET:
                        if self.search_form.cleaned_data['stack']:
                            stack = self.search_form.cleaned_data['stack']
                            users = self.model_tag.objects.filter(tag__in=stack).values('user_id').distinct()

                queryset = queryset.filter(id__in=users)

                paginator = Paginator(queryset, 4)  # Show 1 contacts per page
                page = self.request.GET.get('page')

                queryset = paginator.get_page(page)

        return queryset

    def get_context_data(self, **kwargs):
        kwargs['form'] = self.search_form
        return super().get_context_data(**kwargs)


class SearchSkill(SearchMixin):
    model_tag = Skill


class SearchDesire(SearchMixin):
    model_tag = Desire
