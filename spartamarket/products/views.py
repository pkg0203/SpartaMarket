from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (
    require_GET,
    require_POST,
    require_http_methods,
)
from django.contrib.auth.decorators import login_required
from .models import Products, Comments, HashTag
from .forms import ProductsForm, CommentsForm
from django.db.models import Q, Count
import ctypes
SPECIAL_CHAR = list("[~!@\#$%^&*\()\=+|\\/:;?""<>']")


@require_GET
def show(request):
    if request.user.is_authenticated:
        products = Products.objects.all().order_by('-pk')
        context = {
            "products": products
        }
        return render(request, "products/show.html", context)
    else:
        ctypes.windll.user32.MessageBoxW(0, "로그인이 필요합니다!", "Error", 16)
        return redirect("accounts:login")


@require_GET
def search_and_sort(request):
    if request.user.is_authenticated:
        search = request.GET.get('search')
        sort = request.GET.get('sort')
        if sort == "recent":
            products = Products.objects.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search) |
                Q(hashtags__title__exact=search) |
                Q(author__username__icontains=search)
            ).order_by('-pk')
        elif sort == "jjim":
            products = Products.objects.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search) |
                Q(hashtags__title__exact=search) |
                Q(author__username__icontains=search)
            ).annotate(jjim_count=Count('jjimed')).order_by('-jjim_count')
        context = {
            "products": products
        }
        return render(request, "products/show.html", context)
    else:
        ctypes.windll.user32.MessageBoxW(0, "로그인이 필요합니다!", "Error", 16)
        return redirect("accounts:login")


@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "GET" and request.user.is_authenticated:
        form = ProductsForm()
        context = {
            "form": form,
        }
        return render(request, "products/create.html", context)
    elif request.method == "POST":
        form = ProductsForm(request.POST)
        hashtags = request.POST.get('hashtag').split()
        # Hashtag 특수문자 검사
        for hashtag in hashtags:
            if hashtag in SPECIAL_CHAR:
                ctypes.windll.user32.MessageBoxW(
                    0, "해시태그에 특수문자가 섞여있습니다.", "Error", 16
                )
                return render(request, 'products:show')
        # Hashtag에 특수문자가 없고, form이 유효한 경우
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            for hashtag in hashtags:
                hash_obj, created = HashTag.objects.get_or_create(
                    title=hashtag)
                product.hashtags.add(hash_obj)

        return redirect("products:show")
    else:
        ctypes.windll.user32.MessageBoxW(0, "로그인이 필요합니다!", "Error", 16)
        return redirect("accounts:login")


@require_GET
def detail(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, pk=pk)
        product.is_viewed += 1
        product.save()
        comments = product.comments.all().order_by('-pk')
        form = CommentsForm()
        context = {
            "product": product,
            "form": form,
            "comments": comments
        }
        return render(request, "products/detail.html", context)
    else:
        ctypes.windll.user32.MessageBoxW(0, "로그인이 필요합니다!", "Error", 16)
        return redirect("accounts:login")


@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == "GET" and request.user.is_authenticated:
        form = ProductsForm(instance=product)
        context = {
            'form': form,
            'product': product,
        }
        return render(request, "products/update.html", context)

    elif request.method == "POST":
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
        return redirect('products:detail', product.pk)
    else:
        ctypes.windll.user32.MessageBoxW(0, "로그인이 필요합니다!", "Error", 16)
        return redirect("accounts:login")


@require_POST
def delete(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect("products:show")


@require_POST
def create_comment(request, pk):
    form = CommentsForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.products = get_object_or_404(Products, pk=pk)
        comment.save()
    return redirect('products:detail', comment.products.pk)


@require_POST
def delete_comment(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    product = comment.products
    comment.delete()
    return redirect('products:detail', product.pk)


@require_http_methods(["GET", "POST"])
def update_comment(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    if request.method == "GET" and request.user.is_authenticated:
        form = CommentsForm(instance=comment)
        context = {
            "form": form
        }
        return render(request, "products/comment_update.html", context)
    elif request.method == "POST":
        form = CommentsForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
        return redirect('products:detail', comment.products.pk)
    else:
        ctypes.windll.user32.MessageBoxW(0, "로그인이 필요합니다!", "Error", 16)
        return redirect("accounts:login")


@require_POST
def jjim(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.user in product.jjimed.all():
        request.user.jjim.remove(product)
    else:
        request.user.jjim.add(product)
    return redirect('products:detail', product.pk)
