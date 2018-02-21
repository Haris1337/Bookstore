from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
	title = models.CharField(max_length = 150)
	price = models.IntegerField()

	def __str__(self):
		return self.title

class Purchase(models.Model):
	user = models.ForeignKey(User, related_name='user_purchase')
	book = models.ForeignKey(Book, related_name='book_purchase')
	address = models.CharField(max_length=250)
	price = models.IntegerField()
	

