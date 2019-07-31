from django.db import models
from django.contrib.auth.models import User 

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE) 
    body = models.TextField(blank = True)
    anonymous = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now =True)
    created_at = models.DateTimeField(auto_now_add=True)