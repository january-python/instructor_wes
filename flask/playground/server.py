from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
  return render_template(
    'index.html',
    num_boxes=3,
    color="aqua"
  )

@app.route('/play/<num>')
def play2(num):
  return render_template(
    'index.html',
    num_boxes=int(num),
    color="aqua"
  )

@app.route('/play/<num>/<col>')
def play3(num, col):
  return render_template(
    'index.html',
    num_boxes=int(num),
    color=col
  )

if __name__ == "__main__":
  app.run(debug=True)