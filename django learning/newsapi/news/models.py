from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length= 50)
    title = models.CharField(max_length= 100)
    description = models.CharField(max_length= 200)
    body = models.TextField()
    location = models.TextField(max_length= 120)
    publication_date = models.DateTimeField()
    active = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


    def __str__(self):
        return f"{self.author} {self.title}"
