from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def root():
    return {"message":"Hello World"}

@app.get('/fastapi')
def read_root():
    return {"message": "Hello, FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

def divider(a:int,b:int)->float:
   return a/b
print('Result: ',divider(24,4))

if __name__ == "__main__":
 uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
