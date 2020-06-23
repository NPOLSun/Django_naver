from django.db import models

# Create your models here.

class naver_search(models.Model):
    search_word = models.CharField(max_length=20)

    def __str__(self):
        return self.search_word