from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def blog(request):
    return render(request,'mainapp/blog_page.html')
