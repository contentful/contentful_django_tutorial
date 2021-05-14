from django.http import Http404
from django.shortcuts import render
from .models import client

# Create your views here.

def home(request):
    return render(request, 'index.html', {
        'blogs': client.entries(
            {'content_type': 'blogPost', 'include': 3}
        ),'projects': client.entries(
            {'content_type': 'project', 'include': 3}
        ),'testimonials': client.entries(
            {'content_type': 'testimonial', 'include': 3, 'limit': 3}
        )

    })


def blogs(request):
    return render(request, 'blog.html', {
        'blogs': client.entries(
            {'content_type': 'blogPost', 'include': 3}
        )
    })

def blog_by_slug(request, slug):
    try:
        blog = client.entries(
            {'content_type': 'blogPost', 'fields.slug': slug, 'include': 3}
        )[0]
        return render(request, 'blog/post.html', {'blog': blog})
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))

def projects(request):
    return render(request, 'projects.html', {
        'projects': client.entries(
            {'content_type': 'project', 'include': 3}
        )
    })

def project_by_slug(request, slug):
    try:
        project = client.entries(
            {'content_type': 'project', 'fields.slug': slug, 'include': 3}
        )[0]
        return render(request, 'projects/project.html', {'project': project})
    except IndexError:
        raise Http404('Project not found for slug: {0}'.format(slug))
