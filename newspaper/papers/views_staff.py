from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms_staff import *


# ====================================== Manage article ================================
@login_required
def listArticle(request):
    article_all =  Article.objects.all()
    return render(request, 'staff/article/list.html', {'article_all': article_all})
    

@login_required
def createArticle(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article-list')
    return render(request, 'staff/article/form.html', {'form': form})



@login_required
def updateArticle(request, id):
    article = get_object_or_404(Article, pk=id)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article-list')
            
    return render(request, 'staff/article/form.html', {'form': form})

@login_required
def deleteArticle(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    return redirect('article-list')


# ==================================== Manage categories ========================


@login_required
def listCategory(request):
    categories = Category.objects.all()
    return render(request, 'staff/category/list.html', {'categories': categories} )    


@login_required
def createCategory(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')

    return render(request, 'staff/category/form.html', {'form': form})


@login_required
def updateCategory(request,id):
    category = get_object_or_404(Category, pk=id)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')
            
    return render(request, 'staff/category/form.html', {'form': form})


@login_required
def deleteCategory(request,id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('category-list')



# ============================== Manage Reporter =======================================
@login_required
def listReporter(request):
    reporters = Reporter.objects.all()
    return render(request, 'staff/reporter/list.html', {'reporters': reporters})

@login_required
def createReporter(request):
    form = ReporterForm()
    if request.method == 'POST':
        form = ReporterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reporter-list')
    return render(request, 'staff/reporter/form.html', {'form': form})


@login_required
def updateReporter(request, id):
    reporters = get_object_or_404(Reporter, pk=id)
    form = ReporterForm(instance=reporters)

    if request.method == 'POST':
        form = ReporterForm(request.POST,request.FILES ,instance=reporters)
        if form.is_valid():
            form.save()
            return redirect('reporter-list')
    return render(request, 'staff/reporter/form.html', {'form': form})


@login_required
def deleteReporter(request, id):
    reporter = get_object_or_404(Reporter, pk=id)
    reporter.delete()
    return redirect('reporter-list')