from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField(editable= True)
    Creation_date = models.DateTimeField(auto_now_add = True)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Image = models.ImageField(upload_to="Thumb/",default="Thumb/Default.png",)
    slug = models.SlugField(allow_unicode=True,default=None)
    
    
    def taste_snippet(self):
        return (self.body[:20])