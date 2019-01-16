from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', some_value="&amp;")

@app.route('/process', methods=['POST'])
def process():
  print("*" * 80)
  print(request.form)
  print(request.form['name'])
  print(request.form['email'])
  print("*" * 80)
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)