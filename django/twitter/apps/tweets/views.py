from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Tweet
from ..users.models import User

# Create your views here.
def index(req):
    if 'user_id' not in req.session:
        return redirect('users:new')

    context = {
        "tweets": Tweet.objects.filter(Q(creator__follower_references__user_from=req.session['user_id'])|Q(creator=req.session['user_id'])).order_by("-created_at"),
        "user": User.objects.get(id=req.session['user_id'])
    }
    return render(req, "tweets/index.html", context)

def create(req):
    errors = Tweet.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
    else:
        Tweet.objects.easy_create(req.POST, req.session['user_id'])
    return redirect('tweets:index')

def like(req, tweet_id):
    Tweet.objects.add_like(req.session['user_id'], tweet_id)
    return redirect('tweets:index')

def unlike(req, tweet_id):
    Tweet.objects.remove_like(req.session['user_id'], tweet_id)
    return redirect('tweets:index')

def show(req, user_id):
    context = {
        "user": User.objects.get(id=user_id),
    }
    return render(req, 'tweets/show.html', context)