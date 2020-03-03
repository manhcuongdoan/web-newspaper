from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms_staff import *
from django.http import HttpResponse

# ====================================== Manage article ================================
@login_required
def listArticle(request):
    if request.user.is_staff:
        article_all =  Article.objects.all()
        return render(request, 'staff/article/list.html', {'article_all': article_all})
    else:
        return HttpResponse("you don't have permission to access")

@login_required
def createArticle(request):
    if request.user.is_staff:
        form = ArticleForm()
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('article-list')
        return render(request, 'staff/article/form.html', {'form': form})
    else:
        return HttpResponse("you don't have permission to access")


@login_required
def updateArticle(request, id):
    if request.user.is_staff:
        article = get_object_or_404(Article, pk=id)
        form = ArticleForm(instance=article)

        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('article-list')
                
        return render(request, 'staff/article/form.html', {'form': form})
    else:
        return HttpResponse("you don't have permission to access")

@login_required
def deleteArticle(request, id):
    if request.user.is_staff:
        article = get_object_or_404(Article, pk=id)
        article.delete()
        return redirect('article-list')
    else:
        return HttpResponse("you don't have permission to access")

# ==================================== Manage categories ========================


@login_required
def listCategory(request):
    if request.user.is_staff:
        categories = Category.objects.all()
        return render(request, 'staff/category/list.html', {'categories': categories} )    
    else:
        return HttpResponse("you don't have permission to access")

@login_required
def createCategory(request):
    if request.user.is_staff:
        form = CategoryForm()

        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('category-list')

        return render(request, 'staff/category/form.html', {'form': form})
    else:
        return HttpResponse("you don't have permission to access")

@login_required
def updateCategory(request,id):
    if request.user.is_staff:
        category = get_object_or_404(Category, pk=id)
        form = CategoryForm(instance=category)

        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('category-list')
                
        return render(request, 'staff/category/form.html', {'form': form})
    else:
        return HttpResponse("you don't have permission to access")

@login_required
def deleteCategory(request,id):
    if request.user.is_staff:
        category = get_object_or_404(Category, pk=id)
        category.delete()
        return redirect('category-list')
    else:
        return HttpResponse("you don't have permission to access")


# ============================== Manage Reporter =======================================
@login_required
def listReporter(request):
    if request.user.is_staff:
        reporters = Reporter.objects.all()
        return render(request, 'staff/reporter/list.html', {'reporters': reporters})
    else:
        return HttpResponse("you don't have permission to access")
@login_required
def createReporter(request):
    if request.user.is_staff:
        form = ReporterForm()
        if request.method == 'POST':
            form = ReporterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('reporter-list')
        return render(request, 'staff/reporter/form.html', {'form': form})
    else:
        return HttpResponse("you don't have permission to access")

@login_required
def updateReporter(request, id):
    if request.user.is_staff:
        reporters = get_object_or_404(Reporter, pk=id)
        form = ReporterForm(instance=reporters)

        if request.method == 'POST':
            form = ReporterForm(request.POST,request.FILES ,instance=reporters)
            if form.is_valid():
                form.save()
                return redirect('reporter-list')
        return render(request, 'staff/reporter/form.html', {'form': form})
    else:
        return HttpResponse("you don't have permission to access")

@login_required
def deleteReporter(request, id):
    if request.user.is_staff:
        reporter = get_object_or_404(Reporter, pk=id)
        reporter.delete()
        return redirect('reporter-list')
    else:
        return HttpResponse("you don't have permission to access")