from fastapi import FastAPI,Response 

app = FastAPI()

@app.get("/")
def f1():
    return "Hello"

@app.get("/xmldata")
def f2():
    xml_data = """<student>
    <id>101</id>
    <name>Ram</name>
    <course>fastAPI</course>
    </student>
    """
    return Response(content=xml_data,media_type="application/xml")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8000)