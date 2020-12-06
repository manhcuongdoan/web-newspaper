from django.urls import path, include
from . import views_user, views_staff, views

urlpatterns = [

    # ================================= Log in ============================================
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup), 


    # ================================= Account ============================================
    path('accounts/profile', views_user.viewProfile),

    # ================================= User page =========================================
    path('', views_user.index, name='home'),
    path('article/<int:article_id>', views_user.viewArticle, name='view-article'),


    # ========================== Staff page ===============================================
    
    # Manage Article
    path('staff', views_staff.listArticle, name='article-list'),
    path('staff/article_create', views_staff.createArticle, name='article-create'),
    path('staff/article_update/<int:id>', views_staff.updateArticle, name='article-update'),
    path('staff/article_delete/<int:id>', views_staff.deleteArticle, name='article-delete'),


    # Manage categories
    path('staff/category_list', views_staff.listCategory, name='category-list'),
    path('staff/category_create', views_staff.createCategory, name='category-create'),
    path('staff/category_update/<int:id>', views_staff.updateCategory, name='category-update'),
    path('staff/category_delete/<int:id>', views_staff.deleteCategory, name='category-delete'),


    #Manage reporter
    path('staff/reporter_list', views_staff.listReporter, name='reporter-list'),
    path('staff/reporter_create', views_staff.createReporter, name='reporter-create'),
    path('staff/reporter_update/<int:id>', views_staff.updateReporter, name='reporter-update'),
    path('staff/reporter_delete/<int:id>', views_staff.deleteReporter, name='reporter-delete'),   

]