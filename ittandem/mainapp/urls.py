from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('blog/', mainapp.blog, name='blog')

]
