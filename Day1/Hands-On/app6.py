from flask import Flask,redirect,url_for,request
app  = Flask(__name__)

@app.route("/")
def f1():
    return "<h1>Welcome</h1>"

@app.route("/display/<name>")
def fdisplay(name):
    return f"Welcome to {name}"

@app.route("/mylogin",methods = ['POST','GET'])
def f2():
    if request.method == 'POST':
        user_name = request.form['nv']
        return redirect(url_for('fdisplay',name=user_name))
    else:
        user_name = request.args.get('nv')
        return redirect(url_for('fdisplay',name = user_name))
    
if __name__ == '__main__':
    app.run(debug=True) 