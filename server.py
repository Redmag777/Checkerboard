from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def board ():
    return render_template ('index.html')
@app.route('/<int:x>')
def board2 (x):
    return render_template ('index2.html', x=x)
@app.route('/<int:x>/<int:y>')
def board3 (x, y):
    return render_template ('index3.html', x=x, y=y)

if __name__=="__main__":
   app.run(debug=True)