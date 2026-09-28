from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def f1():
    return render_template('index.html',name = ["Karthik","Anu",'Theeb'])

@app.route("/display")
def f2():
    d = {'pA':1000,'pB':2000,'pC':3000}
    return render_template('display.html',pcost = d)


if __name__ == '__main__':
    app.run(debug=True,port=5001)