from fastapi import FastAPI
app = FastAPI()
@app.get("/sucharitha")
async def read_root():
    return {"Message": "sucharitha"}