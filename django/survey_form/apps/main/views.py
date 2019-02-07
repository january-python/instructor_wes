from django.shortcuts import render, redirect

# Create your views here.
def index(req):
  return render(req, 'main/index.html')

def process(req):
  req.session['full_name'] = req.POST['full_name']
  req.session['location'] = req.POST['location']
  req.session['favorite_language'] = req.POST['favorite_language']
  return redirect('/success')

def success(req):
  context = {
    'title': "Success",
    "color": "red"
  }
  return render(req, 'main/success.html', context)

def color(req, color):
  context = {
    'color': color
  }
  return render(req, 'main/colors.html', context)