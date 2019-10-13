from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from authapp.forms import UserRegisterForm
from authapp.forms import UserLoginForm
from django.conf import settings


def login(request):
    title = 'вход'

    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    context = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


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

def send_verify_mail(user):
    verify_link = reverse('auth:verify',
                          args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале \
    {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            print(f'Пользователь {user} активирован')
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'authapp/verification.html')
        else:
            print(f'Ошибка активации пользователя: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'Ошибка активации пользователя: {e.args}')
    return HttpResponseRedirect(reverse('main'))