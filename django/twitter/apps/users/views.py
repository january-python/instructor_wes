from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Follower

# Create your views here.
def index(req):
    if 'user_id' not in req.session:
        return redirect('users:new')

    context = {
        "users": User.objects.exclude(id=req.session['user_id'])
    }
    return render(req, 'users/index.html', context)

def new(req):
    return render(req, 'users/new.html')

def create(req):
    # validate form input
    errors = User.objects.validate(req.POST)
    # if information is invalid
    if errors:
        # display errors to user
        for error in errors:
            messages.error(req, error)
        # redirect back to the form page
        return redirect('users:new')
    # create user
    user_id = User.objects.easy_create(req.POST)
    # login
    req.session['user_id'] = user_id
    # redirect to tweets index
    return redirect('tweets:index')

def login(req):
    # take form information
    # print(req.POST)
    # send information to models to check for errors
    valid, result = User.objects.login(req.POST)
    # if errors
    if not valid:
        # display error messages
        messages.error(req, result)
        return redirect('users:new')

    # log user in
    req.session['user_id'] = result
    return redirect('tweets:index')

def logout(req):
    req.session.clear()
    return redirect('users:new')

def follow(req, followee_id):
    Follower.objects.easy_create(followee_id, req.session['user_id'])
    return redirect('users:index')