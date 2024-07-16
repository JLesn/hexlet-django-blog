# hexlet_django_blog/views.py
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse

class IndexView(TemplateView):

    template_name = "index.html"

    def redirect(self, request):
        return redirect(reverse('tags', kwargs={tags: 'python', article_id: '42'}))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

def about(request):
    return render(request, 'about.html')
