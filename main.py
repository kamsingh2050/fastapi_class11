from fastapi import FastAPI
    #the reason that the "from" is red is because
    #we have not installed fastAPI in this environment yet

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}