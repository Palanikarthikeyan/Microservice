# from <module> import <member>
from flask import Flask, jsonify ##<== 1st Step

app = Flask(__name__) ## <== 2nd Step

@app.route("/") ## <== 3rd Step
def f1():
    return "<h3> Welcome to Flask App </h3>"

@app.route("/aboutus")
def f2():
    return "<h2> This is about us page</h2>"

@app.route("/report")
def f3():
    s="<h2> <font color='blue'> Welcome to flask micro-service</font></h2>"
    return s

@app.route("/data")
def f4():
    return jsonify({"message":"Hello from User service"})

if __name__  == '__main__':  ## <==4th Step
	app.run(debug=True,port=5001)            ## <==5th Step
