from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# connect database
def get_db():
    conn = sqlite3.connect("emp.db")
    return conn

# Create table
conn = get_db()
conn.execute("""create table if not exists emp(
    id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age NUMBER,dept TEXT)""")
conn.commit()
conn.close()

# Request datamodel
class Emp(BaseModel):
    name: str
    age: int
    dept: str

# Insert an emp details
@app.post("/emps")
def f1(emp: Emp,conn = Depends(get_db)):
    cursor = conn.execute("insert into emp(name,age,dept) values(?,?,?)",(emp.name,emp.age,emp.dept))
    conn.commit()
    emp_id = cursor.lastrowid
    conn.close()
    return {"message":"Emp added successfully","id":emp_id}

# Get all emps
@app.get("/emps")
def f2(conn = Depends(get_db)):
    rows = conn.execute("select *from emp").fetchall()
    conn.close()
    return {"emps":rows}

# Get one emp by emp_id
# -----------------------
@app.get("/emp/{emp_id}")
def get_emp(emp_id: int):
    conn = get_db()
    row = conn.execute("select *from emp where id = ?",(emp_id,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code = 404,detail="Emp not found")
    return {'emp':row}

# update an emp record
@app.put("/emps/{emp_id}")
def update_emp(emp_id: int,emp: Emp):
    conn = get_db()
    cursor = conn.execute("""update emp SET name=?,age=?,dept=? where id = ?""",(emp.name,emp.age,emp.dept,emp_id))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    if updated == 0:
        raise HTTPException(status_code=404,detail="Emp Not Found")
    return {"message":"Emp records updated successfully"}

# Delete a particular emp 
# -------------------------    
@app.delete("/emps/{emp_id}")
def delete_emp(emp_id: int):
    conn = get_db()
    cursor = conn.execute("delete from emp where id = ?", (emp_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Emp Not Found")
    return {"message": "Emp deleted successfully"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8001)
    
    