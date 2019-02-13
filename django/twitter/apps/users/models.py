from django.db import models

# Create your models here.
class UserManager(models.Manager):
    pass

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return "<User: %s>" % self.username

class Follower(models.Model):
    following = models.ForeignKey(User, related_name="followeds")
    followed_by = models.ForeignKey(User, related_name="followers")