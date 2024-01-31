from datetime import datetime

from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    HttpResponseRedirect,
)
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify, first
from .models import Cat, Species, TagPost
from .forms import AddPostForm, UploadFileForm
from django.core.files.storage import default_storage




menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]


# Главная страница, которая рендрит шаблон index.html
def index(request):
    posts = Cat.published.all().order_by("title").select_related("spec")

    data = {
        "title": "Главная страница",
        "menu": menu,
        "posts": posts,
        "spec_selected": 0,
    }
    return render(request, "cats/index.html", data)


def handle_uploaded_file(file):
    with open(f"uploads/{file.name}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data["file"])
    else:
        form = UploadFileForm()
    return render(request, "cats/about.html",
                  {"title": "О сайте", "menu": menu, "form": form })


def show_post(request, post_slug):
    post = get_object_or_404(Cat, slug=post_slug)

    data = {
        "title": post.title,
        "menu": menu,
        "post": post,
        "spec_selected": 1,
    }

    return render(request, "cats/post.html", data)


def add_page(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                return redirect("home")
            except Exception as e:
                print(e)
    
    else:
        form = AddPostForm()
    
    data = {
       "menu": menu,
       "title": "Добавления статьи",
       "form": form,
       }
    return render(request, "cats/addpage.html", data)


def contact(request):
    return render(request, "cats/contact.html", {"menu": menu})


def login(request):
    return HttpResponse("Авторизация")


def show_species(request, spec_slug):
    species = get_object_or_404(Species, slug=spec_slug)
    posts = Cat.published.filter(spec_id=species.pk).select_related("spec")

    data = {
        "title": "Отображение по рубрикам",
        "menu": menu,
        "posts": posts,
        "spec_selected": species.id,
    }
    return render(request, "cats/index.html", context=data)


def show_tagpost(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Cat.Status.PUBLISHED)
    data = {
        "title": f"Тег: {tag.tag}",
        "menu": menu,
        "posts": posts,
        "cat_selected": None,
    }

    return render(request, "cats/index.html", context=data)
