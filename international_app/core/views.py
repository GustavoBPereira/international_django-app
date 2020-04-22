from django.shortcuts import render

from international_app.core.forms import PostForm


def index(request):
    form = PostForm()
    return render(request, 'index.html', {form: 'form'})
