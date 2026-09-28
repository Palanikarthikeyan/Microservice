from flask import Flask
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('demo1.db')
conn.execute("create table if not exists emp(id INTEGER,name TEXT)")
conn.close()

@app.route("/enroll")
def f1():
    conn = sqlite3.connect("demo1.db")
    conn.execute("insert into emp(id,name) values(?,?)",(102,"Leo"))
    conn.commit()
    conn.close()
    return "Employee Enrollment is done"

@app.route("/display")
def f2():
    conn = sqlite3.connect('demo1.db')
    cursor = conn.execute("select *from emp")
    records = cursor.fetchall()
    conn.close()
    return str(records)
    

if __name__ == '__main__':
    app.run(debug=True)