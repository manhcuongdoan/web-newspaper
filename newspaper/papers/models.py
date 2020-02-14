from django.db import models

# Create your models here.
class Category (models.Model):
    category_name = models.CharField(max_length=30)
    category_description = models.TextField(max_length=200)
    def __str__(self):
        return self.category_name

class Reporter (models.Model):
    reporter_name = models.CharField(max_length=30)
    reporter_info = models.TextField()
    file = models.ImageField(upload_to='static/images', verbose_name='Image Reporter') 
    def __str__(self):
        return self.reporter_name
class Article (models.Model): 
    title = models.CharField(max_length=50)
    publish_date = models.DateTimeField('date published')
    summary = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    page_content = models.TextField()
    file = models.ImageField(upload_to='static/images', verbose_name='Image article')  
    def __str__(self):
        return self.title

