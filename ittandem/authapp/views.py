from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from authapp.forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('login'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('login'))
    else:
        register_form = UserRegisterForm()
    context = {'title': 'регистрация',
               'register_form': register_form,
               }
    return render(request, 'authapp/register.html', context)