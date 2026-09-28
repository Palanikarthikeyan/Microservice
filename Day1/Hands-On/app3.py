from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def f1():
    return "<h1> Welcome to Flask App</h1>"

@app.route("/visitor/<vname>")
def f2(vname):
    return f"<h2> Hello...{vname} </h2>"
@app.route("/app/demo")
def f3():
    return "<h2> This is demo App </h2>"

@app.route("/U1")
def f4():
    '''build URL building invoke f2 method'''
    return redirect(url_for('f2',vname = "Raj"))

@app.route("/U2")
def f5():
    return redirect(url_for('f3'))


if __name__ == '__main__':
    app.run(debug = True,port=5002)