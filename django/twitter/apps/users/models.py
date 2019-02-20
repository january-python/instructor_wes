from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['first_name']) < 2:
            errors.append("First name must be at least 2 characters long.")
        if len(form['last_name']) < 2:
            errors.append("Last name must be at least 2 characters long.")
        if len(form['username']) < 2:
            errors.append("Username must be at least 2 characters long.")
        if len(form['password']) < 8:
            errors.append("Password must be at least 2 characters long.")
        if not EMAIL_REGEX.match(form['email']):
            errors.append("Must be a valid email address")

        existing_emails = User.objects.filter(email=form['email'])
        if existing_emails:
            errors.append("Email aleardy in use")
        
        existing_usernames = User.objects.filter(username=form['username'])
        if existing_usernames:
            errors.append("Username already in use")
        return errors

    def easy_create(self, form):
        # hash password
        hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        # create user
        user = User.objects.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            username = form['username'],
            email = form['email'],
            pw_hash = hashed_pw,
        )
        # return id
        return user.id

    def login(self, form):
        # check for existence of email in db
        existing_users = User.objects.filter(email=form['email'])
        if existing_users:
            user = existing_users[0]
            if bcrypt.checkpw(form['password'].encode(), user.pw_hash.encode()):
                return (True, user.id)
        return (False, "Email or password incorrect")

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    def __repr__(self):
        return "<User: %s>" % self.username
    
    def __str__(self):
        return "<User: %s>" % self.username

class Follower(models.Model):
    following = models.ForeignKey(User, related_name="followeds")
    followed_by = models.ForeignKey(User, related_name="followers")