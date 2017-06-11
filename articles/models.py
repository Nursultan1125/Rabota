from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_content = models.TextField()
    article_date_create = models.DateTimeField(auto_now_add=True)
    article_date_update = models.DateTimeField(auto_now=True)
    article_author = models.ForeignKey(User)
    article_image = models.ImageField(upload_to='images/news/', verbose_name='Изображение новости')
#     artcle_likes = models.IntegerField(default=0)
#     article_content=models.ForeignKey(Commenst)
#

    def get_article_anons(self):
        return self.article_content[:300]
#
# class Commenst(models.Model):
#     comments_content = models.TextField()
#     comments_author = models.ForeignKey(User)
#     comments_date_create = models.DateTimeField(auto_now_add=True)