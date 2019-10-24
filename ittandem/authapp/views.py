from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView, View
from .models import User, Deal
from tagapp.forms import TagForm
from tagapp.models import Skill, Desire
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from authapp.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse
from authapp.forms import UserRegisterForm
from authapp.forms import UserEditForm


class DealUpdate(LoginRequiredMixin, View):

    model = Deal

    def post(self, request, *args, **kwargs):
        print('id', kwargs['pk'], self.request.POST.get('add'))
        if self.request.POST.get('add'):
            self.model.objects.create(user=self.request.user, partner=get_object_or_404(User, pk=kwargs['pk']))

        if self.request.POST.get('confirm'):
            queryset = self.model.objects.filter(partner=self.request.user, user=get_object_or_404(User, pk=kwargs['pk']))
            queryset.update(status=True)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'authapp/profile.html'
    form_class_tag = TagForm
    model_tag_skill = Skill
    model_tag_desire = Desire

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        if self.request.user.id == self.kwargs['pk']:
            skills = []
            for skill in self.model_tag_skill.objects.filter(user=self.request.user):
                skills.append(skill.tag_id)
            kwargs['form_skill'] = self.form_class_tag(initial={'name': skills})
            desires = []
            for desire in self.model_tag_desire.objects.filter(user=self.request.user):
                desires.append(desire.tag_id)
            kwargs['form_desire'] = self.form_class_tag(initial={'name': desires})

            user_bids = Deal.objects.filter(partner=self.request.user, status=False)
            kwargs['user_bids'] = user_bids



        else:
            field_skill = []
            skills = self.request.user.skills.all()
            for skill in skills:
                title = skill.tag.field.name + '/' + skill.tag.name
                field_skill.append(title)
            field_desire = []
            desires = self.request.user.desires.all()
            for desire in desires:
                title = desire.tag.field.name + '/' + desire.tag.name
                field_desire.append(title)

            button_style = ''
            find1 = Deal.objects.filter(user_id=self.request.user.id, partner_id=self.kwargs['pk'])
            find2 = Deal.objects.filter(partner_id=self.request.user.id, user_id=self.kwargs['pk'])
            if not find1 and not find2:
                button_style = 'add'


            contact_view = False

            if find1:
                contact_view = find1.first().status
            elif find2:
                contact_view = find2.first().status
                if not contact_view:
                    button_style = 'confirm'



            kwargs['button_style'] = button_style
            kwargs['contact_view'] = contact_view
            kwargs['field_desire'] = field_desire
            kwargs['field_skill'] = field_skill
        return kwargs


def login(request):
    title = 'вход'

    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))

    context = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = UserRegisterForm()

    context = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', context)


def profile(request):
    return render(request, 'authapp/profile.html')


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)

    context = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', context)


