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


class TagCreateMixin(FormView):
    template_name = 'tagapp/form.html'
    success_url = None
    model_tag = None
    form_class_tag = None

    def form_valid(self, form):
        print(form.cleaned_data)
        if self.request.user.id:
            self.model_tag.objects.filter(user=self.request.user).delete()
            for skill in form.cleaned_data['name']:
                skill = int(skill)
                self.model_tag.objects.create(tag_id=skill, user=self.request.user)
            messages.success(self.request, _(f'Навыки сохранены'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        skills = []
        print()
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

    success_url = '/tags/desire/'
    model_tag = Desire
    form_class_tag = TagForm


class SearchView(ListView):
    template_name = 'tagapp/search_form.html'
    model = User
    forms_filter = [SearchForm]

    def get_context_data(self, **kwargs):
        stack = ''
        field = ''
        fil = False
        sta = False
        for form_class in self.forms_filter:
            if self.request.method == form_class.method:
                if 'field' in self.request.GET:
                    if not self.request.GET['field'].isdigit() and self.request.GET['field'] != '':
                        fil = True
                if 'stack' in self.request.GET:
                    if not self.request.GET['stack'].isdigit() and self.request.GET['stack'] != '':
                        sta = True
                if fil or sta:
                    form = form_class()
                else:
                    form = form_class(self.request.GET)
                if form.is_valid():
                    if 'field' in self.request.GET:
                        field = self.request.GET['field']
                    if 'stack' in self.request.GET:
                        stack = self.request.GET['stack']
                        field = ''
                    if stack == '' and field == '':
                        field = '%'
            object_raw = User.objects.raw(
                '''select distinct * 
                    from authapp_user
                    left join tagapp_skill on authapp_user.id=tagapp_skill.user_id
                    left join tagapp_stack on tagapp_skill.tag_id=tagapp_stack.id
                    left join tagapp_field on tagapp_stack.field_id=tagapp_field.id
                    where tagapp_field.id LIKE  %s or tagapp_stack.id LIKE  %s''', [field, stack])
            user_dict = {}
            for user in object_raw:
                skills = Skill.objects.filter(user=user)
                skill_list = []
                for skill in skills:
                    fields = Stack.objects.filter(id=skill.tag.id)
                    for field in fields:
                        field_stack = field.field.name + '/' + skill.tag.name
                        skill_list.append(field_stack)
                user_dict[user] = skill_list
            kwargs['form'] = form
            kwargs['object_list'] = user_dict
        return super().get_context_data(**kwargs)
