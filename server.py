from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Hi():
    return "Hi There Partner"

@app.route('/play/')
def BOXES():
    return render_template('index.html', times = int(3), color = 'red')

@app.route('/play/<integer>/<myColor>/')
def BOXES1(integer, myColor):

    return render_template('index.html', times = int(integer), color = myColor)


if __name__=="__main__":
    app.run(debug=True)