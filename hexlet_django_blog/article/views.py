from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse


class IndexView(View):

    def get(self, request, *args, **kwargs):
#        return HttpResponse('Hello, articles!')
        tag = 'python'
        article_id = 42
        return redirect(reverse('tags', args={tag, article_id}))

def tags(request, tags, article_id):
    return render(request,
                  'article/index.html',
                  context={'tags': tags, 'article_id': article_id})
