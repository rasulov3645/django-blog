from django.db import models

# Create your models here.
class Article(models.Model): 
	class Meta(): 
		db_table = "article"
	article_title = models.CharField(max_length=200)
	article_taxt = models.TextField()
	article_date = models.DateTimeField()
	article_likes = models.IntegerField()

