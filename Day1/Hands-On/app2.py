from flask import Flask ##<== 1st Step

app = Flask(__name__) ## <== 2nd Step

@app.route("/") ## <== 3rd Step
def f1():
    return "<h3> Welcome to Flask App </h3>"

@app.route("/aboutus")
def f2():
    return "<h2> This is about us page</h2>"

@app.route("/report/<dept>")
def f3(dept):
    return f"<h3> Selected dept page is:{dept}</h3>"

@app.route("/user/<int:user_id>")
def f4(user_id):
    return f"User ID is: {user_id}"

if __name__  == '__main__':  ## <==4th Step
	app.run(debug=True,port=5001)            ## <==5th Step
