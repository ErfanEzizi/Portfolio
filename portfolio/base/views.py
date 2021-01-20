from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse
from .forms import PostForm
from .filters import PostFilter
from .models import *

# Create your views here.


def home(request):
    content = Post.objects.filter(active=True, featured=True)[0:3]

    myFilter = PostFilter()
    return render(request, 'index.html', {
        "posts": content,
        "filter": myFilter,
    })


def all_posts(request):
    content = Post.objects.filter(active=True)

    myFilter = PostFilter(request.GET, queryset=content)
    content = myFilter.qs

    page = request.GET.get('page')

    paginator = Paginator(content, 3)

    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)
    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    return render(request, 'allposts.html', {
        "posts": content,
        "filter": myFilter,
    })


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {
        "post": post,
    })


def profile(request):
    return render(request, 'profiel.html')


def message(request):
    if request.method == 'POST':
        template = render_to_string('send_mail.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['erfanazizitd@gmail.com']

        )
        email.fail_silently = False
        email.send()
        return HttpResponse('Message sent!')

# crud


@login_required(login_url="home")
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('all_post')

    return render(request, "post_form.html", {
        'form': form,
    })


@login_required(login_url="home")
def updatePost(request, pk):
    post = Post.objects.get(id=pk)

    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('all_post')

    return render(request, "post_form.html", {
        'form': form,
    })


@login_required(login_url="home")
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "POST":
        post.delete()
        return redirect('all_post')

    return render(request, 'delete.html', {
        "item": post
    })
