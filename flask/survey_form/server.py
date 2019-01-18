from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'a;lkjsdfhdsfokweokjsdflkjawe;lkj'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/success')
def success():
  return render_template('success.html')

@app.route('/process', methods=['POST'])
def process():
  session['name'] = request.form['name']
  session['location'] = request.form['location']
  session['favorite_language'] = request.form['favorite_language']
  return redirect('/success')

if __name__ == "__main__":
  app.run(debug=True)