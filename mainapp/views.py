from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# def hello_world(request):
#     return
# from django.views import View
#
#
# class HelloWorldView(View):
#     def get(self, *args):
#         return HttpResponse('Helloworld')
#
#
# def check_kwargs(request, **kwargs):
#     return HttpResponse(f'kwargs:<br>{kwargs}')
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'
