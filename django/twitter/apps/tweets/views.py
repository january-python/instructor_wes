from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.core import serializers
import json
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

def create_ajax(req):
    errors = Tweet.objects.validate(req.POST)
    if errors:
        context = {
            'error_list': errors
        }
        return render(req, 'tweets/index_errors.html', context, status=400)
    else:
        context = {
            'tweet': Tweet.objects.easy_create(req.POST, req.session['user_id'])
        }
    return render(req, 'tweets/tweet.html', context)

def create_json(req):
    # this is unfinished, we'd need to custom tailor the return information so we can easily create the html on the js side of things
    errors = Tweet.objects.validate(req.POST)
    if errors:
        return HttpResponse(json.dumps(errors), status=400, content_type="application/json")
    
    tweet = Tweet.objects.easy_create(req.POST, req.session['user_id'])
    return HttpResponse(serializers.serialize('json', [tweet,]), status=200, content_type="application/json")

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