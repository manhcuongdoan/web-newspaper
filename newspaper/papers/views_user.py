from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.

def index(request):
    article_all = Article.objects.order_by('-publish_date')[:5]
    context = {'article_all': article_all}
    return render(request, 'user/index.html', context)
    #return HttpResponse(template.render(context, request))

def viewArticle(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'user/article_detail.html', {'article': article})

def viewProfile(request):
    user = request.user
    return render(request, 'user/account_detail.html', {'user': user})
