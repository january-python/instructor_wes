from django.db import models
from ..users.models import User

# Create your models here.
class TweetManager(models.Manager):
    def validate(self, form):
        errors = []

        if len(form['content']) < 1:
            errors.append("Tweet must be at least 1 character long.")
        if len(form['content']) > 255:
            errors.append("Tweet must be no more than 255 characters long.")

        return errors

    def easy_create(self, form, user_id):
        user = User.objects.get(id=user_id)
        Tweet.objects.create(
            content=form['content'],
            creator=user
        )
    
    def add_like(self, user_id, tweet_id):
        user = User.objects.get(id=user_id)
        tweet = Tweet.objects.get(id=tweet_id)
        user.liked_tweets.add(tweet)
    
    def remove_like(self, user_id, tweet_id):
        user = User.objects.get(id=user_id)
        tweet = Tweet.objects.get(id=tweet_id)
        user.liked_tweets.remove(tweet)

class Tweet(models.Model):
    content = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="tweets")
    users_liked = models.ManyToManyField(User, related_name="liked_tweets")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TweetManager()