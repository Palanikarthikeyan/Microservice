from flask import Flask, render_template,jsonify
app = Flask(__name__)

@app.route("/")
def f1():
    return render_template('index.html',name = ["Karthik","Anu",'Theeb'])

@app.route("/display")
def f2():
    d = {'pA':1000,'pB':2000,'pC':3000}
    return render_template('display.html',pcost = d)

@app.route("/emp")
def f3():
    d = {'eid':101,'ename':'Mr.AB','ecost':1000,'edept':'sales'}
    return render_template('emp_display.html', emp_data = d)
@app.route("/empdata")
def f4():
    d = {'eid':101,'ename':'Mr.AB','ecost':1000,'edept':'sales'}
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug=True)