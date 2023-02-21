from django.db import models


# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=255, default="NO VALUE")
    content = models.CharField(max_length=255, default="NO VALUE")
    author = models.CharField(max_length=255, default="NO VALUE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# auto_now_add : Time when an instance of the BlogPost model is CREATED.
# auto_now : Time when an instance of the BlogPost model is SAVED.
