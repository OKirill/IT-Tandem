from django.views.generic import FormView
# from django.utils.translation import gettext_lazy as _
# from django.contrib import messages
# from django.views.generic import UpdateView, CreateView
# # from django.contrib.auth.mixins import PermissionRequiredMixin
# # from authapp.models import User
# from .forms import TestForm
# # from django.forms.models import inlineformset_factory
# from mainapp.models import Skill, Desire
# # from django.contrib.auth.mixins import LoginRequiredMixin
#
#
# class TagCreateMixin(FormView):
#     template_name = 'tagapp/form.html'
#     # success_url = None
#     # model_tag = Skill
#     # form_class_tag = None
#
#     def form_valid(self, form):
#         if self.request.user.id:
#             # self.model_tag.objects.filter(user=self.request.user).delete()
#             for skill in form.cleaned_data['tag']:
#                 print(skill)
#                 # self.model_tag.objects.create(tag_id=skill.id, user=self.request.user)
#                 # messages.success(self.request, _(f'Навыки сохранены'))
#         return super().form_valid(form)
#
#     # def get_context_data(self, **kwargs):
#     #     kwargs = super().get_context_data(**kwargs)
#     #     skills = []
#     #     for skill in self.model_tag.objects.filter(user=self.request.user):
#     #         skills.append(skill.tag_id)
#     #     kwargs['form'] = self.form_class_tag(initial={'name': skills})
#     #     return kwargs
#
#


class SearchCreate(FormView):
    template_name = 'search/form.html'
    success_url = '/search/'