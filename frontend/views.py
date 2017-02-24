from django.http import Http404
from django.shortcuts import render
from .models import client

# Create your views here.

def posts(request):
    return render(request, 'posts/all.html', {
        'posts': client.entries(
            {'content_type': 'post', 'include': 3}
        )
    })

def post_by_slug(request, slug):
    try:
        post = client.entries(
            {'content_type': 'post', 'fields.slug': slug, 'include': 3}
        )[0]
        return render(request, 'posts/post.html', {'post': post})
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))



