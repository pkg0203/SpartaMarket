from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (
    require_GET,
    require_POST,
    require_http_methods,
)
from django.contrib.auth.decorators import login_required
from .models import Products, Comments
from .forms import ProductsForm, CommentsForm
from django.db.models import Q,Count
import ctypes


@require_GET
def show(request):
    if request.user.is_authenticated:
        products = Products.objects.all().order_by('-pk')
        print("-show-")
        print(products)
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
        if sort=="recent" :
            products = Products.objects.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search) |
                Q(author__username__icontains=search)
            ).order_by('-pk')
        elif sort == "jjim":
            products = Products.objects.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search) |
                Q(author__username__icontains=search)
            ).annotate(jjim_count=Count('jjimed')).order_by('-jjim_count')
        context = {
            "products": products
        }
        return render(request,"products/show.html", context)
    

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "GET":
        form = ProductsForm()
        context = {
            "form": form,
        }
        return render(request, "products/create.html", context)
    elif request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
        return redirect("products:show")


@require_GET
def detail(request, pk):
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


@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == "GET":
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
    if request.method == "GET":
        form = CommentsForm(instance=comment)
        context = {
            "form": form
        }
        return render(request, "products/comment_update.html", context)
    else:
        form = CommentsForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
        return redirect('products:detail', comment.products.pk)


@require_POST
def jjim(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.user in product.jjimed.all():
        request.user.jjim.remove(product)
    else:
        request.user.jjim.add(product)
    return redirect('products:detail', product.pk)
